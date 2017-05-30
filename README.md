# IntroCompatiblizer
This program assists beginners with adding an intro to Movie Maker webcam WMV videos, and mp4 on linux

## System Requirements

## How to Use
* You can run the program using the icon "Intro Combatiblizer"
* Make sure file in Intro folder in your Videos folder in your profile is same resolution and frame rate as original video

## Changes
(2017-05-29)
* added separate Delay button
-- deprecated done_flag in favor of done_flags and flag_index
* Changed MP4Box command to use -cat for both video files (instead of -add <file1> -cat <file2>) so that delay works properly (not sure why didn't, but some sites suggest -cat <file1> -cat <file2> is proper syntax)
* Go back to preferring MP4Box (revert to MP4Box, if present, when an MP4 is about to be worked on)
-- deprecated converter_exe_path (instead, use exe_by_package[converter_package]
* allow multiple filetypes for intro (for all types in Intro folder, matching videos will be listed)
-- deprecated introVideoFileString, required_dotext
* get_dotext and get_filenamenoext: use splitext
* get_dotext should return nothing (not filename) when no dot is present
* changed methods and many variables to underscore naming instead of camelhump
* (2017-02-26) switched from ffmpeg to MP4Box (only when run on linux) to avoid outdated packages which have contat errors and slowness (due to distro retaining old versions of ffmpeg)
* (2017-02-26) the blank version of the Add Intro button shoud show a message instead of crashing when no files are present
* (2017-02-26) create folders needed, to avoid crash on move file if destination folder didn't exist
* (2017-02-26) detect profile path and use cross-platform pathing

## Known Issues
* May have issues with apostraphe or other special characters in filename

## Developer Notes
* ffmpeg contact only works using a listfile (other methods failed, which is reason wmvappend was used by this program for a while).
MP4Box is used since ffmpeg concat is still rather slow and has bad timestamp errors. These problems are due to old packages (distro's fault) according to http://video.stackexchange.com/questions/15468/non-monotonous-dts-on-concat-ffmpeg

* tried converting wmv to mp4 with below info, but vlc says video is 640x482 (but "display" resolution 640x480), and flowblade says framerate is 125 fps:

cd $HOME/Videos/without-intro
thisvideofolder=converted-mp4
mkdir $thisvideofolder
thisname=x.wmv
ffmpeg -i "$thisname" -c:v libx264 -crf 18 -c:a aac "$thisvideofolder/${thisname%.wmv}.mp4"

### old notes (no longer applicable)
* On Windows you can get wmvappend.exe from WM Format SDK
* If you acquire wmvappend.exe, please read EULA.txt (End-User License Agreement) and WMFormatSDK_eula.txt before using, and do not distribute it with this program without permission from Microsoft.
* ffmpeg cannot join the files. The problem is that concat doesn't seem to work. Instead, only the intro is used in the resulting file. The concat protocol is apparently not used anymore. I tried both an ffmpeg from 2009 and from 2012 and neither work.
One of the developers answered this problem (only first video is copied) by saying that concat protocol is deprecated,
and that the concat demuxer should be used instead. I cannot figure out how to do this or find any examples.
* The only line in the program D:\Projects-kivy\IntroCompatiblizer\introcompatiblizer.py
that doesn't work is the line where the program uses the ffmpeg command (line 126 makes the command and stores it in the batchLine variable)
HOW TO FIX: Just change the ffmpeg line--the variable batchLine stores the specific ffmpeg command. Where literal quotes are needed, \" is used (for example, "ffmpeg -i \"filename.wmv\"").
This wouldn't work (neither would copy /b) so I used WMVAppend.exe instead.

