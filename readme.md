# IntroCompatiblizer
This program helps beginners add an intro to Movie Maker
webcam WMV videos on Windows, and to mp4 videos on GNU+Linux systems.

## System Requirements
- Windows: ffmpeg.exe in same directory (formerly wmvappend.exe)
- Linux: gpac (MP4Box)
- A Kivy virtual environment (on Windows, replace `~` with
  `%USERPROFILE%` and ignore lines starting with `#`):
```
python -m pip install --upgrade --user pip virtualenv setuptools
python -m virtualenv ~/kivy_venv
source ~/kivy_venv/bin/activate
# pip install Cython==0.29.9
# ^ FAILS (0.29.10 which worked before also fails)
# pip install --no-binary kivy
# ^ FAILS: "ERROR: You must give at least one requirement
#   to install (see "pip help install")"
pip install Cython
pip install git+https://github.com/kivy/kivy.git@master
# ^ installs v2.0.0rc3, git-855c963 as of Fedora 32 (2020-06-18)
```

## How to Use
- You can run the program using the icon "Intro Combatiblizer"
- Make sure file in Intro folder in your Videos folder in your profile
  is same resolution and frame rate as original video

## Known Issues
- [ ] Fork [ffpb](https://github.com/althonos/ffpb) to work with a Kivy
  progress bar.
  - or https://pypi.org/project/ffmpeg-progress/
  - or manually-coded: https://stackoverflow.com/a/7641175/4541104
- [ ] Add ability to process videos (such as offset time) even if no
  intro is present.
- [ ] May have issues with apostraphe or other special characters in
  filename.

## Developer Notes
- ffmpeg concat only works using a listfile (other methods failed,
  which is reason wmvappend was used by this program for a while).
  - MP4Box is used since ffmpeg concat is still rather slow and has bad
    timestamp errors. These problems are due to old packages (distro's
    fault) according to
    <http://video.stackexchange.com/questions/15468/non-monotonous-dts-on-concat-ffmpeg>
  - example lastList.txt file:
```
ffconcat version 1.0
file '/home/owner/Videos/Intro/Intro - SeanMauer Video Intro 2014-06-10c (640x480p30).mp4'
file '/home/owner/Videos/without-intro/2017-05-14 15-48-18.mp4'
```
- I tried converting wmv to mp4 with below info, but vlc says that the
  video is 640x482 (but "display" resolution 640x480), and flowblade
  says that the framerate is 125 fps:

```
cd $HOME/Videos/without-intro
thisvideofolder=converted-mp4
mkdir $thisvideofolder
thisname=x.wmv
ffmpeg -i "$thisname" -c:v libx264 -crf 18 -c:a aac "$thisvideofolder/${thisname%.wmv}.mp4"
```

### Old Notes (no longer applicable)
* On Windows you can get wmvappend.exe from WM Format SDK
* If you acquire wmvappend.exe, please read EULA.txt (End-User License
  Agreement) and WMFormatSDK_eula.txt before using, and do not
  distribute it with this program without permission from Microsoft.
* ffmpeg cannot join the files. The problem is that concat doesn't seem
  to work. Instead, only the intro is used in the resulting file. The
  concat protocol is apparently not used anymore. I tried both an
  ffmpeg from 2009 and from 2012 and neither work. One of the
  developers answered this problem (only first video is copied) by
  saying that concat protocol is deprecated, and that the concat
  demuxer should be used instead. I cannot figure out how to do this or
  find any examples.
* The only line in the program
  D:\Projects-kivy\IntroCompatiblizer\introcompatiblizer.py that
  doesn't work is the line where the program uses the ffmpeg command
  (line 126 makes the command and stores it in the batchLine variable)
  - HOW TO FIX: Just change the ffmpeg line--the variable batchLine
  stores the specific ffmpeg command. Where literal quotes are needed,
  \" is used (for example, "ffmpeg -i \"filename.wmv\""). - This
  wouldn't work (neither would copy /b) so I used WMVAppend.exe
  instead.

