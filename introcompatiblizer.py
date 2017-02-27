from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
#from kivy.clock import Clock

import traceback
import time

import os
from os import path
profile_path = None
if 'USERPROFILE' in os.environ:  # if os_name=="windows":
    profile_path = os.environ['USERPROFILE']
else:
    profile_path = os.environ['HOME']



videos_path =  os.path.join(profile_path, "Videos")
finished_videos_path = os.path.join(videos_path,"without-intro")
skipped_videos_path = os.path.join(videos_path,"finished")
intros_path = os.path.join(videos_path,"Intro")
introVideoFileString = None
required_dotext = ".wmv"
folder_path = intros_path
if os.path.isdir(folder_path):
    for sub_name in os.listdir(folder_path):
        sub_path = os.path.join(folder_path, sub_name)
        if sub_name[:1]!="." and os.path.isfile(sub_path):
            basename=os.path.splitext(sub_name)[0]
            if "intro" in sub_name.lower() and sub_name[-4:].lower()==required_dotext:
                introVideoFileString = sub_path

dirsep="\\"
processedFileIDString = " (with Intro)"
files = list()
currentItem = -1
ffmpegFullName = "D:\\Projects-kivy\\IntroCompatiblizer\\ffmpeg.exe"

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
        newFiles = os.listdir(videos_path)
        files[:] = []
        fileCount = 0
        for thisFile in newFiles:
            thisFullName = path.join(videos_path,thisFile)
            if path.isfile(thisFullName):
                if thisFullName.lower().endswith(".wmv"):
                    identifierIndex = thisFile.find(processedFileIDString)
                    #only do if not already done:
                    if identifierIndex<0:
                        files.append(thisFile)
                        #self.ids.videoListView.item_strings.append(thisFullName)
                        fileCount += 1
        if fileCount < 1:
            self.ids.statusLabel.text = "No Videos Found"
            self.ids.addIntroButton.text = ""
            self.ids.skipVideoButton.text = ""
            currentItem = -1
        else:
            currentItem = 0
            self.ids.statusLabel.text = str(fileCount) + " Video(s) Found. Opened:\n" + files[currentItem]
            self.ids.addIntroButton.text = "Add Intro"
            self.ids.skipVideoButton.text = "Skip This File"


    def addIntro(self):
        global finished_videos_path
        global videos_path
        global dirsep
        global currentItem
        global introVideoFileString
        global files
        global ffmpegFullName
        thisFile = files[currentItem]
        srcFileFullName = path.join(videos_path,thisFile)
        srcMovedFileFullName = path.join(finished_videos_path,thisFile)
        newIndex = 1
        #make sure file does not already exist (avoid overwriting!):
        while (path.isfile(srcMovedFileFullName)):
            newIndex+=1
            #starts at 2 intentionally:
            srcMovedFileFullName = path.join(finished_videos_path,self.get_filenamenoext(thisFile)+" ("+str(newIndex)+")"+self.get_dotext(thisFile))
        destFileFullName = path.join(videos_path,self.get_filenamenoext(thisFile)+processedFileIDString+self.get_dotext(thisFile))
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
                        #batchLine = ffmpegFullName+" -i \"concat:"+introVideoFileString+"|"+srcMovedFileFullName+"\" -c copy \""+destFileFullName+"\""
                        #batchLine = ffmpegFullName+" -i \""+listFileName+"\" -c copy \""+destFileFullName+"\""
                        #batchLine = "copy /b \"" + introVideoFileString + "\" + \"" + srcMovedFileFullName + "\" \"" + destFileFullName + "\""
                        batchLine = ffmpegFullName + " -f concat -safe 0 -auto_convert 1 -i \"" + listFileName + "\" -c copy \"" + destFileFullName + "\""
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
                self.ids.videoListView.item_strings.append("Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+").")
        except:
            #traceback.print_exc()
            #print(traceback.format_exc(), file=sys.stderr, flush=True)
            self.ids.videoListView.item_strings.append(traceback.format_exc())

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
        global dirsep
        global currentItem
        global skipped_videos_path
        global files
        if currentItem>=0:
            thisFile = files[currentItem]
            os.rename(path.join(videos_path,thisFile), path.join(skipped_videos_path,thisFile))
            self.detectVideos()
        else:
            self.ids.videoListView.item_strings.append("Nothing to do (push refresh or move file back from "+finished_videos_path+" to "+videos_path+").")

    def getSkippedVideosBack(self):
        pass
        #newFiles = os.listdir(skipped_videos_path)
        #unskipped_count = 0
        #for thisFile in newFiles:
        #    thisFullName = path.join(skipped_videos_path,thisFile)
        #    if path.isfile(thisFullName):
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
