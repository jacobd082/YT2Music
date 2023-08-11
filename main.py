# YouTube2Music
# Made by Jacob Drath (jacobdrath.co / @Jacobd082 on Twitter / @jacobd082 on GitHub)
# Open source as of August 2023
# Licensed under the Apache License, Version 2.0 (the "License")
# Feel free to contribute or fork improvements!
# The dependencies of this project are known to break frequently and I will do my best to update them quickly.
# Thanks for using YT2Music!


# Define a class that has a bunch of colors to use.
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Welcome Message
# Importing takes a moment, so this shows a "Please wait" message
print("__     _________ ___  __  __           _      ")
print("\ \   / /__   __|__ \|  \/  |         (_)     ")
print(" \ \_/ /   | |     ) | \  / |_   _ ___ _  ___ ")
print("  \   /    | |    / /| |\/| | | | / __| |/ __|")
print("   | |     | |   / /_| |  | | |_| \__ \ | (__ ")
print("   |_|     |_|  |____|_|  |_|\__,_|___/_|\___|")
print("YouTube video downloader\nPlease wait...")

# Import Dependencies
try :
    from pytube import YouTube # Used for fetching the video
except :
    print(c.FAIL + "An error occurred while importing pytube. Please reinstall or update YT2MUSIC. If this issue is still here, report an issue." + c.ENDC)
    sys.exit(0)

try :
    from moviepy.editor import * # Used for converting the video
except :
    print(c.FAIL + "An error occurred while importing moviepy. Please reinstall or update YT2MUSIC. If this issue is still here, report an issue." + c.ENDC)
    sys.exit(0)

# System
import os
import sys

input("Press [ENTER] to begin.")
print("\n")

# Project Name: Used for name of file
# TODO: Make sure that Windows and Linux are able to have spaces in file names.
projectName = input(c.BOLD+"Enter a project name:\n"+c.ENDC)
print("\n")

# YouTube URL: Get video from here.
urlToUse = input(c.BOLD+"Enter YouTube URL:\n"+c.ENDC)
print("\n")

# Tests to make sure that the link is valid and that pytube is working properly.
try :
    yt = YouTube(urlToUse)
except :
    print(c.FAIL + "Invalid YouTube URL. If this URL is valid, try updating or reinstalling YT2MUSIC." + c.ENDC)
    sys.exit(0)

# Make sure that the user has the correct video
input(f"{c.BOLD}Verify:{c.ENDC} Press enter if you trying to use \"{yt.title}\"")
print("\n")

# Ask the user how to video should be in the end.
action = input(f"Do you want to download a {c.UNDERLINE}A{c.ENDC}udio or a {c.UNDERLINE}V{c.ENDC}ideo?")
print("\n")

# Get path for download
path = input(f"{c.BOLD}Where would you like to download this file?{c.ENDC} (Don't put a '/' after last directory.)\n{os.path.expanduser('~')}/")
path = os.path.expanduser('~') + "/" + path

# Start downloading
print(f"\n{c.OKGREEN}Starting...{c.ENDC}")
print(f"{c.OKBLUE}Downloading video...{c.ENDC}")
if (action.lower().startswith("a")):
    # Audio (No comments here b/c the prints are explaining.)
    try :
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path, 'temporary_feel_free_to_delete.mp4')
    except:
        print(c.FAIL + "Something went wrong while downloading this video. If this issue persists, try updating or reinstalling YT2MUSIC." + c.ENDC)
        sys.exit(0)
    print(f"{c.OKBLUE}Converting File...{c.ENDC}")
    video = VideoFileClip(path+"/temporary_feel_free_to_delete.mp4")
    try:
        video.audio.write_audiofile(f"{path}/{projectName}.mp3")
    except:
        print(c.FAIL + "Something went wrong while converting this video. Make sure that your path is valid. If this issue persists, try updating or reinstalling YT2MUSIC." + c.ENDC)
        sys.exit(0)
    print(f"{c.OKBLUE}Clearing temporary file...{c.ENDC}")
    os.remove(path+'/temporary_feel_free_to_delete.mp4')
else :
    # Video
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)


print(f"\n{c.OKCYAN}DONE{c.ENDC}")

# Odd issue sometimes makes script not stop.
sys.exit(0)