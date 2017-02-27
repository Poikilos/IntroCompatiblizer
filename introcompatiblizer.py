deps_enable = True
python_basename="python"  # could also be python3
try:
    from kivy.uix.boxlayout import BoxLayout
    from kivy.app import App
    from kivy.lang import Builder
    #from kivy.clock import Clock
except:
    deps_enable = False
    
    print("Kivy is missing from your system. Try the following commands in terminal:")
    print("")
    print("If you are on Windows:")
    print("Go to http://expertmultimedia.com/usingpython")
    print(" then click 'Install Kivy for Python 3'")
    print("")
    print("If you are on a debian-based distro:")
    #print("sudo add-apt-repository ppa:kivy-team/kivy")
    #print("sudo apt-get update")
    print("sudo apt-get remove python-kivy python3-kivy")
    #print("sudo apt-get install python-setuptools python-pygame python-opengl python-gst0.10 python-enchant gstreamer0.10-plugins-good python-dev build-essential libgl1-mesa-dev-lts-quantal libgles2-mesa-dev-lts-quantal python-pip")
    
    #The next commented print command is a modified one-line python3 version of instruction at https://kivy.org/docs/installation/installation.html under "Development Version"
#    print("sudo apt-get install python3-setuptools python3-pygame python3-opengl python3-gst-1.0 python3-enchant gstreamer0.10-plugins-good python3-dev build-essential libgl1-mesa-dev libgles2-mesa-dev python3-pip")
#  but python3-pygame doesn't exist so follow http://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3 :
#sudo apt-get install mercurial
#hg clone https://bitbucket.org/pygame/pygame
#cd pygame
#sudo apt-get install python3-dev python3-setuptools python3-numpy libsdl-dev libsdl-image1.2-dev \
#  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
#  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
#python3 config.py
#python3 setup.py build
#sudo python3 setup.py install

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
    # pypiwin32 kivy.deps.sdl2 kivy.deps.glew")
    
    try:
        raw_input("Press enter to exit...")
    except:
        input("Press enter to exit...")

if not deps_enable:
    exit(1)

import traceback
import time

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

processedFileIDString = " (with Intro)"
os_name = "posix"
converter_exe_path = None
if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")):
    converter_exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")
    os_name = "windows"
elif os.path.isfile("/usr/bin/ffmpeg"):
    converter_exe_path = "ffmpeg"  # no full path is needed if in bin
    os_name = "linux"
elif os.path.isfile("ffmpeg.exe"):
    converter_exe_path="ffmpeg.exe"
    os_name = "windows"
elif os.path.isfile("ffmpeg"):
    converter_exe_path="ffmpeg"
    os_name = "linux"
else:
    #deps_enable=False
    #try:
    #    raw_input("Please place ffmpeg in the current directory in order to use this program.")
    #except:
    #    input("Please place ffmpeg in the current directory in order to use this program.")
    pass

if os_name=="windows":
    converter_package = "ffmpeg"
else:
    if os.path.isfile("/usr/bin/MP4Box"):
        converter_exe_path = "MP4Box"  # no full path is needed if in bin
    else:
        deps_enable = False
        try:
            raw_input("Please install MP4Box via gpac package in order to use this program.")
        except:
            input("Please install MP4Box via gpac package in order to use this program.")
        
if not deps_enable:
    exit(1)

introVideoFileString = None
required_dotext = ".mp4"
if os_name=="windows":
    required_dotext = ".wmv"
folder_path = intros_path
intro_count = 0
if os.path.isdir(folder_path):
    for sub_name in os.listdir(folder_path):
        sub_path = os.path.join(folder_path, sub_name)
        if sub_name[:1]!="." and os.path.isfile(sub_path):
            basename=os.path.splitext(sub_name)[0]
            if "intro" in sub_name.lower() and sub_name[-4:].lower()==required_dotext:
                introVideoFileString = sub_path
                intro_count += 1
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
            on_press: root.detectVideos()
        Label:
            id: statusLabel
            size_hint: (1, 0.1)
            text: ''
        Button:
            id: addIntroButton
            size_hint: (1, 0.1)
            text: ''
            on_press: root.addIntro()
        Button:
            id: skipVideoButton
            size_hint: (1, 0.1)
            text: ''
            on_press: root.skipVideo()
        Button:
            id: getSkippedVideosBackButton
            size_hint: (1, 0.1)
            text: ''
            opacity: 0.0
            on_press: root.getSkippedVideosBack()

        ListView:
            id: videoListView
''')

class MainForm(BoxLayout):
    #this_app = None
    def get_dotext(self, filename):
        lastDotIndex = filename.rfind(".")
        wholeStringCount = len(filename)
        if (lastDotIndex>=0):
            #fromEndCount = lastDotIndex - wholeStringCount
            #make it positive:
            #fromEndCount *= 1
            #get end only (part before ':' is what to remove):
            filenameonly = filename[lastDotIndex:]
        else:
            filenameonly = filename
        return filenameonly

    def get_filenamenoext(self, filename):
        #from Paulo Scardine. "How to get rid of extenstions from file basename using python" [sic]. Stack Overflow. Apr 6 2013. Dec 14, 2014
        lastDotIndex = filename.rfind(".")
        if (lastDotIndex>=0):
            filenameonly = filename[:lastDotIndex]
        else:
            filenameonly = filename
        return filenameonly

    def detectVideos(self):
        global files
        global videos_path
        global currentItem
        global required_dotext
        if os.path.isdir(intros_path):
            if introVideoFileString is not None and os.path.isfile(introVideoFileString):
                newFiles = os.listdir(videos_path)
                #while len(files) > 0 : files.pop()
                del files[:]
                #del files[:] is same as files[:] = [] --neither change the reference
                #files[:] = []
                fileCount = 0
                for thisFile in newFiles:
                    thisFullName = os.path.join(videos_path,thisFile)
                    if os.path.isfile(thisFullName):
                        if thisFullName.lower().endswith(required_dotext):
                            identifierIndex = thisFile.find(processedFileIDString)
                            #only do if not already done:
                            if identifierIndex<0:
                                files.append(thisFile)
                                #self.ids.videoListView.item_strings.append(thisFullName)
                                fileCount += 1
                if fileCount < 1:
                    self.ids.statusLabel.text = "No Videos Found in "+videos_path
                    self.ids.addIntroButton.text = ""
                    self.ids.skipVideoButton.text = ""
                    currentItem = -1
                else:
                    currentItem = 0
                    self.ids.statusLabel.text = str(fileCount) + " Video(s) Found. Opened:\n" + files[currentItem]
                    self.ids.addIntroButton.text = "Add Intro"
                    self.ids.skipVideoButton.text = "Skip This File"
            else:
                self.ids.statusLabel.text = "Error: "+intros_path+" must contain "+required_dotext+" file"
        else:
            self.ids.statusLabel.text = "Error: "+intros_path+" is missing--place *"+required_dotext+" there."

    def addIntro(self):
        global finished_videos_path
        global videos_path
        global currentItem
        global introVideoFileString
        global files
        global converter_exe_path
        if currentItem >=0 and currentItem < len(files):
            thisFile = files[currentItem]
            srcFileFullName = os.path.join(videos_path,thisFile)
            srcMovedFileFullName = os.path.join(finished_videos_path,thisFile)
            newIndex = 1
            #make sure file does not already exist (avoid overwriting!):
            while (os.path.isfile(srcMovedFileFullName)):
                newIndex+=1
                #starts at 2 intentionally:
                srcMovedFileFullName = os.path.join(finished_videos_path,self.get_filenamenoext(thisFile)+" ("+str(newIndex)+")"+self.get_dotext(thisFile))
            destFileFullName = os.path.join(videos_path,self.get_filenamenoext(thisFile)+processedFileIDString+self.get_dotext(thisFile))
            try:
                if (currentItem>=0):
                    bad_character_index = videos_path.find("'")
                    if bad_character_index < 0:
                        bad_character_index = finished_videos_path.find("'")
                        if bad_character_index < 0:
                            srcMovedFileFullName = srcMovedFileFullName.replace("'","")
                            destFileFullName = destFileFullName.replace("'","")
                            if srcFileFullName != srcMovedFileFullName:
                                os.rename(srcFileFullName, srcMovedFileFullName)
                            #GOAL: combine introVideoFileString with srcMovedFileFullName
                            # and save result as destFileFullName
                            # ffmpeg -i concat:"introVideoFileString|srcMovedFileFullName" "destFileFullName"
                            listFileName = "lastList.txt"
                            listFile = open(listFileName, 'w')
                            listFile.write("ffconcat version 1.0\n")
                            listFile.write("file '" + introVideoFileString+"'\n")
                            #listFile.write("stream\n")
                            listFile.write("file '" + srcMovedFileFullName+"'\n")
                            #listFile.write("stream\n")
                            listFile.close()
                            #batchLine = converter_exe_path+" -i \"concat:"+introVideoFileString+"|"+srcMovedFileFullName+"\" -c copy \""+destFileFullName+"\""
                            #batchLine = converter_exe_path+" -i \""+listFileName+"\" -c copy \""+destFileFullName+"\""
                            #batchLine = "copy /b \"" + introVideoFileString + "\" + \"" + srcMovedFileFullName + "\" \"" + destFileFullName + "\""
                            #see also MP4Box -add 1.mp4 -cat 2.mp4 -cat 3.mp4 NameofNewCombinedFile.mp4
                            #see also mencoder firstmovie.mp4 secondmovie.mp4 -ovc copy -oac copy -of lavf format=mp4 mergedclip.mp4
                           
                            if converter_package=="ffmpeg":
                                batchLine = converter_exe_path + " -f concat -safe 0 -auto_convert 1 -i \"" + listFileName + "\" -c copy \"" + destFileFullName + "\""
                            else:
                                batchLine = converter_exe_path + " -add \"" + introVideoFileString + "\" -cat \"" + srcMovedFileFullName + "\" \""+destFileFullName+"\""
                            self.ids.videoListView.item_strings.append("(Creating...) "+destFileFullName)
                            self.set_button_usability(False)
                            os.system(batchLine)
                            self.set_button_usability(True)
                            item_count = len(self.ids.videoListView.item_strings)
                            self.ids.videoListView.item_strings[item_count-1]="Done "+destFileFullName
                            #self.ids.videoListView.item_strings.append("Creating "+destFileFullName+"...OK")
                        else:
                            self.ids.videoListView.item_strings.append("Cannot have single quote in finished videos path.")
                            self.ids.videoListView.item_strings.append("(Nothing was done)")

                    else:
                        self.ids.videoListView.item_strings.append("Cannot have single quote in videos path.")
                        self.ids.videoListView.item_strings.append("(Nothing was done)")
                    self.detectVideos()
                else:
                    #self.ids.videoListView.item_strings.append("Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+").")
                    self.ids.statusLabel.text="Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+")."
            except:
                #traceback.print_exc()
                #print(traceback.format_exc(), file=sys.stderr, flush=True)
                self.ids.videoListView.item_strings.append(traceback.format_exc())
        else:
            self.ids.statusLabel.text="Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+")."

    def set_button_usability(self, usable_enable):
        this_opacity = 1.0
        if not usable_enable:
            this_opacity=  .5
        self.ids.detectVideosButton.opacity = this_opacity
        self.ids.detectVideosButton.disabled = not usable_enable
        #self.ids.detectVideosButton.canvas.ask_update()
        self.ids.addIntroButton.opacity = this_opacity
        self.ids.addIntroButton.disabled = not usable_enable
        #self.ids.addIntroButton.canvas.ask_update()
        self.ids.skipVideoButton.opacity = this_opacity
        self.ids.skipVideoButton.disabled = not usable_enable
        #self.this_app.update()
        #none of this stuff below refreshes the widgets :(
        #self.ids.skipVideoButton.canvas.ask_update()
        #self.ids.getSkippedVideosBackButton.opacity = this_opacity
        #self.ids.getSkippedVideosBackButton.disabled = not usable_enable
        #self.ask_update() #no attribute exception
        #self.ids.videoListView.ask_update() #no attribute exception
        #self.ids.videoListView.canvas.ask_update()
        #self.canvas.ask_update()
        #this_layout = self.ids.mainBoxLayout
        #self.remove_widget(self.ids.mainBoxLayout)
        #self.add_widget(this_layout)
        #self.ids.mainBoxLayout.do_layout()
        #self.ids.skipVideoButton.update_canvas()
        #self.update_canvas()
        #time.sleep(.2)  # allow window to refresh (?)

    def skipVideo(self):
        global finished_videos_path
        global videos_path
        global currentItem
        global skipped_videos_path
        global files
        if currentItem>=0:
            thisFile = files[currentItem]
            os.rename(os.path.join(videos_path,thisFile), os.path.join(skipped_videos_path,thisFile))
            self.detectVideos()
        else:
            #self.ids.videoListView.item_strings.append("Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+").")
            self.ids.statusLabel.text="Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+")."

    def getSkippedVideosBack(self):
        pass
        #newFiles = os.listdir(skipped_videos_path)
        #unskipped_count = 0
        #for thisFile in newFiles:
        #    thisFullName = os.path.join(skipped_videos_path,thisFile)
        #    if os.path.isfile(thisFullName):
        #        if thisFullName.lower().endswith(".wmv"):
        #            unskipped_count += 1
        #self.detectVideos()
        #self.ids.videoListView.item_strings.append("Brought back "+str(unskipped_count)+" video(s)")

class IntroCompatiblizerApp(App):
    def build(self):
        mainform = MainForm()
        #mainform.this_app = self
        return mainform

if __name__ == '__main__':
    IntroCompatiblizerApp().run()
