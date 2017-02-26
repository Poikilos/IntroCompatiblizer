# IntroCompatiblizer
This program assists beginners with adding an intro to Movie Maker webcam WMV videos, and mp4 on linux

## System Requirements
Windows: wmvappend.exe (such as from WM Format SDK)

## How to Use
You can run the program using the icon "Intro Combatiblizer"

## Known Issues
* The only line in the program D:\Projects-kivy\IntroCompatiblizer\introcompatiblizer.py
that doesn't work is the line where the program uses the ffmpeg command (line 126 makes the command and stores it in the batchLine variable)
HOW TO FIX: Just change the ffmpeg line--the variable batchLine stores the specific ffmpeg command. Where literal quotes are needed, \" is used (for example, "ffmpeg -i \"filename.wmv\"").
This wouldn't work (neither would copy /b) so I used WMVAppend.exe instead.
* May have issues with apostraphe or other special characters in filename

## Developer Notes
* If you acquire wmvappend.exe, please read EULA.txt (End-User License Agreement) and WMFormatSDK_eula.txt before using, and do not distribute it with this program without permission from Microsoft.
* ffmpeg cannot join the files. The problem is that concat doesn't seem to work. Instead, only the intro is used in the resulting file. The concat protocol is apparently not used anymore. I tried both an ffmpeg from 2009 and from 2012 and neither work.
One of the developers answered this problem (only first video is copied) by saying that concat protocol is deprecated,
and that the concat demuxer should be used instead. I cannot figure out how to do this or find any examples.

