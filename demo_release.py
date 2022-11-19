
import argparse
import matplotlib.pyplot as plt
import re
import os
from colorizers import *

from multiprocessing import Process


def parseFrame(img,name, export):
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--img_path', type=str, default=img)
	parser.add_argument('--use_gpu', action='store_true', help='whether to use GPU')
	parser.add_argument('-o','--save_prefix', type=str, default='saved', help='will save into this file with {eccv16.png, siggraph17.png} suffixes')
	opt = parser.parse_args()
	useGpu = False
	# load colorizers
	#colorizer_eccv16 = eccv16(pretrained=True).eval()
	colorizer_siggraph17 = siggraph17(pretrained=True).eval()
	if(useGpu):
		#colorizer_eccv16.cuda()
		colorizer_siggraph17.cuda()

	# default size to process images is 256x256
	# grab L channel in both original ("orig") and resized ("rs") resolutions
	img = load_img(opt.img_path)
	(tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
	if(useGpu):
		tens_l_rs = tens_l_rs.cuda()

	# colorizer outputs 256x256 ab map
	# resize and concatenate to original L channel
	img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig),dim=1))
	#out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
	out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())
	#newName = name.split(".")[0]+'.jpg'
	#plt.imsave('%s_eccv16.png'%opt.save_prefix, out_img_eccv16)
	plt.imsave(export+name, out_img_siggraph17) #REDO plt.imsave(export+str(ct)+'.png', out_img_siggraph17) 
 
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def parse_begin(images, export, image_folder):
    for image in images:
        parseFrame(image_folder+image,image, export)
        print(image)
def pp(f):
    print(f)
if __name__ == '__main__':
    ### Arguments
	"""	
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--img_path', type=str, default=img)
	parser.add_argument('--use_gpu', action='store_true', help='whether to use GPU')
	parser.add_argument('-o','--save_prefix', type=str, default='saved', help='will save into this file with {eccv16.png, siggraph17.png} suffixes')
	opt = parser.parse_args()
 	"""
 
	#input
	#output
	#IgnoreDuplicates (for a rerun)
	#clean data
	#Max Core Count	
	#debug
    ###
    
	corelimit = os.cpu_count()
	print('Cores used %d'%corelimit)
	processes = []

	ignore_duplicates = True

	image_folder = os.path.dirname(os.path.abspath(__file__))+"/data2/"
 
	export_folder = os.path.dirname(os.path.abspath(__file__))+"/dataColor/"
	images_ignored = [img for img in sorted_alphanumeric(os.listdir(export_folder))
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]
	print('images ignored %d' % len(images_ignored))
 
	images_total = [img for img in sorted_alphanumeric(os.listdir(image_folder))
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]
	print('images total %d' % len(images_total))


	images =  images_total if (ignore_duplicates==False) else list(set(images_total).difference(images_ignored))
	print('remaining images %d' % len(images))
	imageCutCount = len(images)/corelimit
	print(images)
	print(imageCutCount)
	if(len(images)>0):
		for i in range(corelimit):
		
			split_images=images[int(imageCutCount*i): (len(images)) if (i==corelimit-1) else(int(imageCutCount*(i+1))  )]

			print('registering process %d' % i)
			print(split_images)
			print('split images %d' % len(split_images))
			print('split images start: '+ str(int(imageCutCount*i)) +': end: '+str((len(images))) if (i==corelimit-1) else(int(imageCutCount*(i+1))))
	
			processes.append( Process(target=parse_begin, args=(split_images, export_folder, image_folder,) ) )
			
		for proc in processes:
			proc.start()
		for proc  in processes:
			proc.join()
	else:
		print('No images are available to process')