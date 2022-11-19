# Program To Read video
# and Extract Frames
import cv2
import re
import os

# Function to extract frames
def FrameCapture(path):
	
	# Path to video file
	vidObj = cv2.VideoCapture(path)

	# Used as counter variable
	count = 0

	# checks whether frames were extracted
	success = 1

	while (success):
		
		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()
		name = './data2/' + str(count) + '.jpg'
		print(name)
  
		# Saves the frames with frame-count
		cv2.imwrite(name, image)
		
		count += 1

# Driver Code
if __name__ == '__main__':
	###
	#input
	#debug
	###
	# Calling the function
	FrameCapture("mov/mov.mp4")

