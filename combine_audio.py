import os
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
import moviepy.editor as mp


import argparse
"""
# make a command-line argument parser & add various parameters
parser = argparse.ArgumentParser(description="Python script to add audio to video clip")
parser.add_argument("-v", "--video-file", help="Target video file")
parser.add_argument("-a", "--audio-file", help="Target audio file to embed with the video")
parser.add_argument("-s", "--start", help="Start duration of the audio file, default is 0", default=0, type=int)
parser.add_argument("-e", "--end", help="The end duration of the audio file, default is the length of the video file", type=int)
parser.add_argument("-c", "--composite", help="Whether to add to the existing audio in the video", action="store_true", default=False)
parser.add_argument("-f", "--volume-factor", type=float, default=1.0, help="The volume factor to multiply by the volume of the audio file, 1 means no change, below 1 will decrease volume, above will increase.")
#debug
# parse the arguments
args = parser.parse_args()
print(args)"""

#get video paths
videoPath = os.path.dirname(os.path.abspath(__file__))+"/mov/mov.mp4"
videoPath2 = os.path.dirname(os.path.abspath(__file__))+"/mov2/movieColor.m4v"
print(('set paths'))
#create video variabels
my_clip = mp.VideoFileClip(r"%s" % videoPath)
my_clip2 = mp.VideoFileClip(r"%s" % videoPath2)
print(('get clips'))
#save audio
audioPath = os.path.dirname(os.path.abspath(__file__))+"/mov/movie_audio.mp3"
print(('save audio'))
#my_clip.audio.write_audiofile(r"%s" %audioPath)

audio_clip = mp.AudioFileClip(audioPath)
print(('split clip'))
#end = my_clip.end
#audio_clip = audio_clip.subclip(0, end)
print(('set audio'))
# add the final audio to the video
final_clip = my_clip2.set_audio(audio_clip)
print(('save video'))
#save video
final_clip.write_videofile(r"movie_audio.mp4")