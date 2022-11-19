# importing libraries
import os
import cv2
from PIL import Image
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

###
#input
#output
#merge audio
#export Name
#debug
###

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("dataColor")
path = os.path.dirname(os.path.abspath(__file__))+"/dataColor/"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))
# print(num_of_images)

for file in os.listdir('.'):
	#print(file)
	if file!=".DS_Store":
		im = Image.open(os.path.join(path, file))
		width, height = im.size
		mean_width += width
		mean_height += height
	# im.show() # uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required because the video frame needs
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# embedded into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# print(mean_height)
# print(mean_width)

# Resizing of the images to give
# them same width and height
"""
for file in os.listdir('.'):
	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
		# opening image using PIL Image
		im = Image.open(os.path.join(path, file))

		# im.size includes the height and width of image
		width, height = im.size
		print(width, height)

		# resizing
		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
		imResize.save( file, 'JPEG', quality = 95) # setting quality
		# printing each resized image name
		print(im.filename.split('\\')[-1], " is resized")

"""
# Video Generating function
def generate_video():
	image_folder = os.path.dirname(os.path.abspath(__file__))+"/dataColor/" # make sure to use your folder
	video_name = 'testColor.avi'
	os.chdir(os.path.dirname(os.path.abspath(__file__))+"/mov2/")
	
	images = [img for img in sorted_alphanumeric(os.listdir(image_folder))
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]
	
	# Array images should only consider
	# the image files ignoring others if any
	print(len(images))

	frame = cv2.imread(os.path.join(image_folder, images[0]))
	print('imread done')
	# setting the frame width, height width
	# the width, height of first image
	height, width, layers = frame.shape
	fourcc = cv2.VideoWriter_fourcc(*'a\0\0\0')
	video = cv2.VideoWriter(video_name, 0, 23.976, (width, height))

	# Appending the images to the video one by one
	for image in images:
		print(image)
		video.write(cv2.imread(os.path.join(image_folder, image)))
	
	# Deallocating memories taken for window creation
	print('release')
	cv2.destroyAllWindows()
	video.release() # releasing the video generated
	print('convert')
	#convert_avi_to_mp4(os.path.dirname(os.path.abspath(__file__))+"/mov2/"+video_name, 'finalProduct')


def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    return True

# Calling the generate_video function
generate_video()

