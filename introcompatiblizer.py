#!/usr/bin/env python
deps_enable = True
python_basename="python"  # could also be python3
require_wmv_enable = False
require_MP4Box_enable = False
badIntroExts = ["txt", "sfk", "xml"]
okIntroExts = ["wmv", "mp4"]
startup_errors = list()
setupNote = """
#sudo dnf install python-virtualenv
python -m pip install --upgrade --user pip setuptools virtualenv
python -m virtualenv ~/kivy_venv
source ~/kivy_venv/bin/activate
python -m pip install cython
python -m pip install kivy
#python -m pip install kivy_examples
##"Gstreamer is not included, so if you would like to use media playback
##with kivy, you should install ffpyplayer like so"
#python -m pip install ffpyplayer
#-<https://kivy.org/doc/stable/installation/installation-linux.html>
"""
try:
    input = raw_input
except NameError:
    pass

def view_traceback():
    ex_type, ex, tb = sys.exc_info()
    print(min_indent+str(ex_type))
    print(min_indent+str(ex))
    traceback.print_tb(tb)
    del tb


try:
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.app import App
    from kivy.lang import Builder
    #from kivy.clock import Clock
except ImportError:
    deps_enable = False
    
    view_traceback()
    print("If Kivy is missing from your system,")
    print("try the following commands in terminal:")
    print("")
    print("If you are on Windows:")
    print("Go to http://expertmultimedia.com/usingpython")
    print(" then click 'Install Kivy for Python 3'")
    print("")
    print("Otherwise:")
    print(setupNote)
    exit(1)
    print("If you are on a debian-based distro:")
    # print("sudo add-apt-repository ppa:kivy-team/kivy")
    # print("sudo apt-get update")
    print("sudo apt-get remove python-kivy python3-kivy")
    # print("sudo apt-get install python-setuptools python-pygame"
    #       " python-opengl python-gst0.10 python-enchant"
    #       " gstreamer0.10-plugins-good python-dev build-essential"
    #       " libgl1-mesa-dev-lts-quantal libgles2-mesa-dev-lts-quantal"
    #       " python-pip")
    
    # The next commented print command is a modified one-line python3
    # version of instruction at
    # <https://kivy.org/docs/installation/installation.html> under
    # "Development Version"
    # print("sudo apt-get install python3-setuptools python3-pygame"
    #       " python3-opengl python3-gst-1.0 python3-enchant"
    #       " gstreamer0.10-plugins-good python3-dev build-essential"
    #       " libgl1-mesa-dev libgles2-mesa-dev python3-pip")
    # # but python3-pygame doesn't exist so follow
    # # <http://askubuntu.com/questions/401342/
    # # how-to-download-pygame-in-python3-3>:
    # sudo apt-get install mercurial
    # hg clone https://bitbucket.org/pygame/pygame
    # cd pygame
    # sudo apt-get install python3-dev python3-setuptools \
    #  python3-numpy libsdl-dev libsdl-image1.2-dev \
    #  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    #  libportmidi-dev \
    #  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
    # python3 config.py
    # python3 setup.py build
    # sudo python3 setup.py install

    print("sudo apt-get install python-setuptools python-pygame python-opengl python-gst0.10 python-enchant gstreamer0.10-plugins-good python-dev build-essential libgl1-mesa-dev-lts-quantal libgles2-mesa-dev-lts-quantal python-pip")
    print("sudo apt-get install python-pip") # python3-pip")
    print("sudo python -m pip install --upgrade pip")
    print("sudo python -m pip install cython")
    print("sudo python -m pip install --upgrade pip wheel setuptools")
    print("sudo python -m pip install docutils pygments")
    print("sudo python -m pip install kivy --no-cache-dir")
    print("")
    #see also (don't seem to exist though google groups page linked below says is solution): gstreamer-python and gstreamer-devel
    print("If you are on Fedora etc use the following instructions which are a modified limited non-buildozer version of line from https://groups.google.com/forum/#!topic/kivy-users/t9248qRFvNM:")
    print("sudo dnf install python-devel ffmpeg-libs SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel portmidi-devel libavdevice libavc1394-devel zlibrary-devel ccache mesa-libGL mesa-libGL-devel")
    #Next line resolves: gcc: error: /usr/lib/rpm/redhat/redhat-hardened-cc1: No such file or directory
    print("sudo dnf install redhat-rpm-config")
    #http://download.opensuse.org/repositories/home:/thopiekar:/kivy/
    #doesn't contain anything for Fedora (even old fedora version folders linked from  )
    #print("sudo python3 -m pip install --upgrade pip")
    #print("sudo python3 -m pip install cython")
    #print("sudo python3 -m pip install --upgrade pip wheel setuptools")
    #print("sudo python3 -m pip install docutils pygments")
    # pypiwin32 kivy.deps.sdl2 kivy.deps.glew")
    
    #print("cd $HOME/Downloads")
    #print("wget https://kivy.org/downloads/appveyor/kivy/Kivy-1.9.2.dev0-cp35-cp35m-win_amd64.whl")
    #print("sudo python3 -m pip install Kivy-1.9.2.dev0-cp35-cp35m-win_amd64.whl")
    #print("If 'not a supported wheel on this platform, then:")
    #print("wget https://kivy.org/downloads/appveyor/kivy/Kivy-1.9.2.dev0-cp35-cp35m-win32.whl")
    #print("sudo python3 -m pip install Kivy-1.9.2.dev0-cp35-cp35m-win32.whl")
    print("sudo python -m pip install --upgrade pip")
    print("sudo python -m pip install cython")
    print("sudo python -m pip install --upgrade pip wheel setuptools")
    print("sudo python -m pip install docutils pygments")
    print("sudo python -m pip install kivy --no-cache-dir")
    # pypiwin32 kivy.deps.sdl2 kivy.deps.glew"
    input("Press enter to exit...")

if not deps_enable:
    exit(1)

import traceback
import time

import sys
import os
#from os import path
profile_path = None
if 'USERPROFILE' in os.environ:  # if os_name=="windows":
    profile_path = os.environ['USERPROFILE']
else:
    profile_path = os.environ['HOME']



videos_path =  os.path.join(profile_path, "Videos")
finished_videos_path = os.path.join(videos_path,"without-intro")
skipped_videos_path = os.path.join(videos_path,"finished")
intros_path = os.path.join(videos_path,"Intro")
if os.path.isdir(videos_path):
    if not os.path.isdir(finished_videos_path):
        os.makedirs(finished_videos_path)
    if not os.path.isdir(skipped_videos_path):
        os.makedirs(skipped_videos_path)
    if not os.path.isdir(intros_path):
        os.makedirs(intros_path)

converter_package = "gpac"  # MP4Box command (see below for syntax)
if require_wmv_enable:
    converter_package = "ffmpeg"
#done_flag = " (with Intro)"
done_flags = list()
done_flags.append(" (with Intro)")
done_flags.append(" (with Delay)")
os_name = "posix"
exe_by_package = dict()
exe_by_package["ffmpeg"] = "ffmpeg"
exe_by_package["gpac"] = "MP4Box"
#NOTE: exe_by_package full paths are detected below:

if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")):
    exe_by_package["ffmpeg"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")
    os_name = "windows"
elif os.path.isfile("/usr/bin/ffmpeg"):
    exe_by_package["ffmpeg"] = "ffmpeg"  # no full path is needed if in bin
    os_name = "posix"
elif os.path.isfile("/usr/local/bin/ffmpeg"):
    exe_by_package["ffmpeg"] = "/usr/local/bin/ffmpeg" 
    os_name = "posix"
elif os.path.isfile("ffmpeg.exe"):
    exe_by_package["ffmpeg"] = "ffmpeg.exe"
    os_name = "windows"
elif os.path.isfile("ffmpeg"):
    exe_by_package["ffmpeg"] = "ffmpeg"
    os_name = "posix"
else:
    if require_wmv_enable:
        deps_enable=False
    startup_errors.append("If you need WMV support, please place ffmpeg")
    startup_errors.append(" in the current directory or install the ffmpeg")
    startup_errors.append(" package in order to use this program.")

#if not require_wmv_enable:
#if os_name == "windows":
#    converter_package = "ffmpeg"
#else:
if os.path.isfile("/usr/bin/MP4Box"):
    exe_by_package["gpac"] = "MP4Box"  # no full path is needed if in bin
    os_name = "posix"
elif os.path.isfile("/usr/local/bin/MP4Box"):
    exe_by_package["gpac"] = "/usr/local/bin/MP4Box"
    os_name = "posix"
else:
    if require_MP4Box_enable:
        deps_enable = False
        print("Refusing to continue without MP4Box at any of these locations:")
        print("  /usr/bin/MP4Box")
        print("  /usr/local/bin/MP4Box")
        input("(press enter to exit)")
    startup_errors.append("If you need mp4 support, please install MP4Box")
    startup_errors.append("via gpac package.")
        
if not deps_enable:
    exit(1)

intro_paths = list()

def get_extensions(include_dot_enable=True):
    results = list()
    for original_name in intro_paths:
        name = original_name.lower()
        filename, extension = os.path.splitext(name)
        if len(extension) > 0:
            results.append(extension)
    return results

def is_compatible(name):
    result = False
    extensions = get_extensions()
    for extension in extensions:
        if name[:-len(extension)].lower() == extension:
            result = True
            break
    return result

def get_compatible_intro(video_path):
    result = None
    video_ext_lower = os.path.splitext(video_path)[1].lower()
    if len(video_ext_lower) > 0:
        for intro in intro_paths:
            if video_ext_lower == os.path.splitext(intro)[1].lower():
                result = intro
                break
    return result

folder_path = intros_path
if os.path.isdir(folder_path):
    for sub_name in os.listdir(folder_path):
        sub_path = os.path.join(folder_path, sub_name)
        if sub_name[:1] == "." or not os.path.isfile(sub_path):
            continue
        basename = os.path.splitext(sub_name)[0]
        if "intro" not in sub_name.lower():
            continue
        if os.path.splitext(sub_path)[1].lower() not in badIntroExts:
            intro_paths.append(sub_path)
files = list()
currentItem = -1

Builder.load_string('''
<MainForm>:
    cols: 1

    BoxLayout:
        id: mainBoxLayout
        orientation: 'vertical'
        Button:
            id: detectVideosButton
            size_hint: (1, 0.1)
            text: 'Refresh'
            on_press: root.detect_videos()
        Label:
            id: statusLabel
            size_hint: (1, 0.1)
            text: ''
        Button:
            id: addIntroButton
            size_hint: (1, 0.1)
            text: ''
            on_press: root.add_intro()
        Button:
            id: addDelayButton
            size_hint: (1, 0.1)
            text: ''
            on_press: root.add_delay()
        BoxLayout:
            id: delayBoxLayout
            orientation: 'horizontal'
            size_hint: (1, 0.1)
            Label:
                id: delayLabel
                size_hint: (0.25, 1.0)
                text: 'Delay Audio (ms):'
            TextInput:
                id: delayTextInput
                size_hint: (0.75, 1.0)
                text: '300.00'
        Button:
            id: skipVideoButton
            size_hint: (1, 0.1)
            text: ''
            on_press: root.skip_video()
        Button:
            id: saveLogButton
            size_hint: (1, 0.1)
            text: 'Save Log to Documents'
            on_press: root.save_log()
        Button:
            id: getSkippedVideosBackButton
            size_hint: (1, 0.1)
            text: ''
            opacity: 0.0
            on_press: root.recall_skipped_videos()

        BoxLayout:
            orientation: 'vertical'
            id: videoListView
''')

def any_in(needles, haystack):
    result = False
    for needle in needles:
        if needle in haystack:
            result = True
            break
    return result

class MainForm(BoxLayout):
    # this_app = None
    add_intro_enable = True
    gpac_enable = False
    lastLabel = None
    
    def get_dotext(self, filename):
        #last_dot_index = filename.rfind(".")
        #wholeStringCount = len(filename)
        #result = None
        #if (last_dot_index >= 0):
        #    #fromEndCount = last_dot_index - wholeStringCount
        #    #make it positive:
        #    #fromEndCount *= 1
        #    #get end only (part before ':' is what to remove):
        #    result = filename[last_dot_index:]
        #else:
        #    result = ""
        return os.path.splitext(filename)[1]

    def get_filenamenoext(self, filename):
        return os.path.splitext(filename)[0]
    
    def pushS(self, msg):
        thisLabel = Label(text=msg)
        self.ids.videoListView.add_widget(thisLabel)
        self.lastLabel = thisLabel
        # formerly self.ids.videoListView.item_strings.append(msg)
        # back when ListView was in Kivy (it is missing from 2.0rc3-git)
    
    def changeLastS(self, msg):
        # formerly:
        # item_count = len(self.ids.videoListView.item_strings)
        # self.ids.videoListView.item_strings[item_count-1] = msg

        if self.lastLabel is not None:
            self.lastLabel.text = msg

    def detect_videos(self):
        """
        Detect the videos that are available to process in the
        videos_path. This occurs when clicking the "Refresh" button and
        possibly after certain operations.
        """
        global files
        global videos_path
        global currentItem
        global startup_errors
        for msg in startup_errors:
            self.pushS(msg)
        startup_errors[:] = []
        if os.path.isdir(intros_path):
            if len(intro_paths) > 0:
                subs = os.listdir(videos_path)
                # while len(files) > 0 : files.pop()
                del files[:]
                # del files[:] # is same as files[:] = []
                # ^ (as desired, neither change the list reference)
                # files[:] = []
                unfinished_count = 0
                for sub_name in subs:
                    sub_path = os.path.join(videos_path,sub_name)
                    if os.path.isfile(sub_path):
                        intro_path = get_compatible_intro(sub_path)
                        if intro_path is not None:
                            #(if there is a compatible intro)
                            if not any_in(done_flags, sub_name):
                                files.append(sub_name)
                                #self.pushS(sub_path)
                                unfinished_count += 1
                if unfinished_count < 1:
                    self.ids.statusLabel.text = (
                        "No unfinished videos found in "+videos_path
                    )
                    self.ids.addIntroButton.text = ""
                    self.ids.addDelayButton.text = ""
                    self.ids.skipVideoButton.text = ""
                    currentItem = -1
                else:
                    currentItem = 0
                    self.ids.statusLabel.text = (
                        str(unfinished_count)
                        + " video(s) Found. Opened:\n"
                        + files[currentItem]
                    )
                    self.ids.addIntroButton.text = "Add Intro"
                    self.ids.addDelayButton.text = "Add Delay"
                    self.ids.skipVideoButton.text = "Skip This File"
            else:
                self.ids.statusLabel.text = (
                    "Error: " + intros_path + " must contain intro"
                    " video files (" + str(badIntroExts)
                    + " are ignored)"
                )
        else:
            self.ids.statusLabel.text = (
                "Error: " + intros_path + " is missing--place intro"
                " videos there."
            )
    
    def add_delay(self):
        self.add_intro_enable = False
        try:
            self.add_intro()
        except:
            print(str(sys.exc_info()))
            pass
        self.add_intro_enable = True
    
    def add_intro(self):
        global finished_videos_path
        global videos_path
        global currentItem
        global files
        global exe_by_package
        global converter_package
        flag_index = 0
        if not self.add_intro_enable:
            flag_index = 1
        if currentItem >= 0 and currentItem < len(files):
            sub_name = files[currentItem]
            src_path = os.path.join(videos_path,sub_name)
            intro_path = get_compatible_intro(src_path)
            src_moved_path = os.path.join(finished_videos_path,
                                          sub_name)
            new_index = 1
            # make sure file does not already exist (avoid overwriting):
            while (os.path.isfile(src_moved_path)):
                new_index += 1
                # Start at 2 intentionally:
                next_name = (self.get_filenamenoext(sub_name) + " ("
                             + str(new_index) + ")"
                             + self.get_dotext(sub_name))
                src_moved_path = os.path.join(finished_videos_path,
                                              next_name)
            dst_path = os.path.join(
                videos_path,
                (self.get_filenamenoext(sub_name)
                 + done_flags[flag_index]
                 + self.get_dotext(sub_name))
            )
            try:
                if currentItem >= 0:
                    badCharI = videos_path.find("'")
                    if badCharI < 0:
                        badCharI = finished_videos_path.find("'")
                        if badCharI < 0:
                            src_moved_path = src_moved_path.replace("'",
                                                                    "")
                            dst_path = dst_path.replace("'", "")
                            if src_path != src_moved_path:
                                os.rename(src_path, src_moved_path)
                            # GOAL: combine intro_path with
                            # src_moved_path and save result as dst_path
                            # ffmpeg -i concat:"intro_path|src_moved_path" "dst_path"
                            listfile_name = "IntroCompatiblizer-last_list.txt"
                            listfile_path = os.path.join(profile_path, listfile_name)
                            listFile = open(listfile_path, 'w')
                            listFile.write("ffconcat version 1.0\n")
                            if self.add_intro_enable:
                                listFile.write("file '" + intro_path + "'\n")
                            # listFile.write("stream\n")
                            listFile.write("file '" + src_moved_path + "'\n")
                            # listFile.write("stream\n")
                            listFile.close()
                            # batchLine = exe_by_package[converter_package]+" -i \"concat:"+intro_path+"|"+src_moved_path+"\" -c copy \""+dst_path+"\""
                            # batchLine = exe_by_package[converter_package]+" -i \""+listfile_path+"\" -c copy \""+dst_path+"\""
                            # batchLine = "copy /b \"" + intro_path + "\" + \"" + src_moved_path + "\" \"" + dst_path + "\""
                            # see also MP4Box -add 1.mp4 -cat 2.mp4 -cat 3.mp4 NameofNewCombinedFile.mp4
                            # see also mencoder firstmovie.mp4 secondmovie.mp4 -ovc copy -oac copy -of lavf format=mp4 mergedclip.mp4
                            prev_converter_package = converter_package
                            
                            if self.get_dotext(src_moved_path) == ".mp4":
                                converter_package = "gpac"
                                if not self.gpac_enable:
                                    self.pushS("ERROR: Cannot convert mp4 without gpac  ")
                                    self.pushS("(need MP4Box command in /usr/bin or /usr/local/bin)")
                                
                            if converter_package == "ffmpeg":
                                delay_command = ""
                                if len(self.ids.delayTextInput.text.strip()) > 0:
                                    try:
                                        delay_f = float(self.ids.delayTextInput.text)
                                        if delay_f > 0.0:
                                            delay_command = " -itsoffset " + str(delay_f/1000.0)
                                    except:
                                        print("Could not finish getting delay:\n" + str(sys.exc_info()))
                                batchLine = exe_by_package[converter_package] + " -f concat" + delay_command + " -safe 0 -auto_convert 1 -i \"" + listfile_path + "\" -c copy \"" + dst_path + "\""
                            else:
                                delay_command = ""
                                if len(self.ids.delayTextInput.text.strip()) > 0:
                                    try:
                                        delay_f = float(self.ids.delayTextInput.text)
                                        if delay_f != 0.0:
                                            delay_command = " -delay 2=" + str(int(delay_f))
                                    except:
                                        print("Could not finish getting delay:\n" + str(sys.exc_info()))
                                if self.add_intro_enable:
                                    batchLine = exe_by_package[converter_package] + " -cat \"" + intro_path + "\"" + delay_command + " -cat \"" + src_moved_path + "\" \"" + dst_path + "\""
                                else:
                                    batchLine = exe_by_package[converter_package] + delay_command + " -add \"" + src_moved_path + "\" \"" + dst_path + "\""
                            if (converter_package != prev_converter_package):
                                converter_package = prev_converter_package
                            last_cmd_path = os.path.join(profile_path, "IntroCompatiblizer-last_command.txt")
                            outs = open(last_cmd_path, 'w')
                            outs.write(batchLine + "\n")
                            outs.close()
                            self.pushS("(Creating...) "+dst_path)
                            self.set_button_usability(False)
                            self.ids.statusLabel.text = "Please wait..."
                            self.ids.mainBoxLayout.do_layout()  # force refresh
                            try:
                                os.system(batchLine)
                                self.set_button_usability(True)
                                self.changeLastS("Done "+dst_path)
                                # self.pushS("Creating " + dst_path
                                #            + "...OK")
                            except:
                                self.ids.statusLabel.text = (
                                    "Could not finish.\n"
                                    + str(sys.exc_info())
                                )
                        else:
                            self.pushS("Cannot have single quote in"
                                       " finished videos path.")
                            self.pushS("(Nothing was done)")

                    else:
                        self.pushS("Cannot have single quote in"
                                   " videos path.")
                        self.pushS("(Nothing was done)")
                    self.detect_videos()
                else:
                    # self.pushS("Nothing to do (push refresh or move"
                    #            " file back from "
                    #            + finished_videos_path + " to "
                    #            + videos_path + ").")
                    self.ids.statusLabel.text = (
                        "Nothing to do (push refresh or move file back"
                        " from " + finished_videos_path + " to "
                        + videos_path + ")."
                    )
            except:
                # traceback.print_exc()
                # print(traceback.format_exc(), file=sys.stderr,
                #       flush=True)
                self.pushS(traceback.format_exc())
        else:
            self.ids.statusLabel.text = (
                "Nothing to do (push refresh or move file back from "
                + finished_videos_path + " to " + videos_path + ")."
            )

    def set_button_usability(self, usable_enable):
        this_opacity = 1.0
        if not usable_enable:
            this_opacity=  .5
        self.ids.detectVideosButton.opacity = this_opacity
        self.ids.detectVideosButton.disabled = not usable_enable
        # self.ids.detectVideosButton.canvas.ask_update()
        self.ids.addIntroButton.opacity = this_opacity
        self.ids.addIntroButton.disabled = not usable_enable
        # self.ids.addIntroButton.canvas.ask_update()
        self.ids.addDelayButton.opacity = this_opacity
        self.ids.addDelayButton.disabled = not usable_enable
        # self.ids.addDelayButton.canvas.ask_update()
        self.ids.skipVideoButton.opacity = this_opacity
        self.ids.skipVideoButton.disabled = not usable_enable
        # self.this_app.update()
        # none of this stuff below refreshes the widgets :(
        # self.ids.skipVideoButton.canvas.ask_update()
        # self.ids.getSkippedVideosBackButton.opacity = this_opacity
        # self.ids.getSkippedVideosBackButton.disabled = not usable_enable
        # self.ask_update() #no attribute exception
        # self.ids.videoListView.ask_update() #no attribute exception
        # self.ids.videoListView.canvas.ask_update()
        # self.canvas.ask_update()
        # this_layout = self.ids.mainBoxLayout
        # self.remove_widget(self.ids.mainBoxLayout)
        # self.add_widget(this_layout)
        # self.ids.mainBoxLayout.do_layout()
        # self.ids.skipVideoButton.update_canvas()
        # self.update_canvas()
        # time.sleep(.2)  # allow window to refresh (?)
        
    def save_log(self):
        logs_path = os.path.join(profile_path, "Documents")
        log_path = os.path.join(logs_path,
                                "IntroCompatiblizer-output.log")
        outs = open(log_path, 'w')
        for widget in self.ids.videoListView.children:
            outs.write(widget.text + "\n")
        outs.close()

    def skip_video(self):
        global finished_videos_path
        global videos_path
        global currentItem
        global skipped_videos_path
        global files
        if currentItem>=0:
            sub_name = files[currentItem]
            os.rename(os.path.join(videos_path,sub_name),
                      os.path.join(skipped_videos_path,sub_name))
            self.detect_videos()
        else:
            # self.pushS("Nothing to do (push refresh or move file back"
            #            " from " + finished_videos_path + " to "
            #            + videos_path + ").")
            self.ids.statusLabel.text = (
                "Nothing to do (push refresh or move file back from "
                + finished_videos_path + " to " + videos_path + ")."
            )

    def recall_skipped_videos(self):
        pass
        # subs = os.listdir(skipped_videos_path)
        # unskipped_count = 0
        # for sub_name in subs:
        #     sub_path = os.path.join(skipped_videos_path,sub_name)
        #     if os.path.isfile(sub_path):
        #         if sub_path.lower().endswith(".wmv"):
        #             unskipped_count += 1
        # self.detect_videos()
        # self.pushS("Brought back "+str(unskipped_count)+" video(s)")

class IntroCompatiblizerApp(App):
    def build(self):
        mainform = MainForm()
        # mainform.this_app = self
        if os.path.isfile("/usr/local/bin/MP4Box"):
            mainform.gpac_enable = True
        elif os.path.isfile("/usr/bin/MP4Box"):
            mainform.gpac_enable = True
        return mainform

if __name__ == '__main__':
    IntroCompatiblizerApp().run()
