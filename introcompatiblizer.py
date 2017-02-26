from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder

import os
from os import path
videosFolderString = "C:\\Users\\seanm\\Videos"
videosDoneFolderString = "C:\\Users\\seanm\\Videos\\without-intro"
videosSkippedFolderString = "C:\\Users\\seanm\\Videos\\finished"
introVideoFileString = "C:\\Users\\seanm\\Videos\\Intro\\Intro - SeanMauer Video Intro 2014-06-10c (wmv-2Mbps).wmv"
dirsep="\\"
processedFileIDString = " (with Intro)"
files = list()
currentItem = -1
ffmpegFullName = "D:\\Projects-kivy\\IntroCompatiblizer\\ffmpeg.exe"

Builder.load_string('''
<MainForm>:
    cols: 1

    BoxLayout:
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
        ListView:
            id: videoListView
''')

class MainForm(BoxLayout):
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
        global videosFolderString
        global currentItem
        newFiles = os.listdir(videosFolderString)
        files.clear()
        fileCount = 0
        for thisFile in newFiles:
            thisFullName = path.join(videosFolderString,thisFile)
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
        global videosDoneFolderString
        global videosFolderString
        global dirsep
        global currentItem
        global introVideoFileString
        global files
        global ffmpegFullName
        thisFile = files[currentItem]
        srcFileFullName = path.join(videosFolderString,thisFile)
        srcMovedFileFullName = path.join(videosDoneFolderString,thisFile)
        newIndex = 1
        #make sure file does not already exist (avoid overwriting!):
        while (path.isfile(srcMovedFileFullName)):
            newIndex+=1
            #starts at 2 intentionally:
            srcMovedFileFullName = path.join(videosDoneFolderString,self.get_filenamenoext(thisFile)+" ("+str(newIndex)+")"+self.get_dotext(thisFile))
        destFileFullName = path.join(videosFolderString,self.get_filenamenoext(thisFile)+processedFileIDString+self.get_dotext(thisFile))
        if (currentItem>=0):
            bad_character_index = videosFolderString.find("'")
            if bad_character_index < 0:
                bad_character_index = videosDoneFolderString.find("'")
                if bad_character_index < 0:
                    srcMovedFileFullName = srcMovedFileFullName.replace("'","")
                    destFileFullName = destFileFullName.replace("'","")
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
                    self.ids.videoListView.item_strings.append("Creating "+destFileFullName)
                    os.system(batchLine)
                    self.ids.videoListView.item_strings.append("Done")
                else:
                    self.ids.videoListView.item_strings.append("Cannot have single quote in finished videos path.")
                    self.ids.videoListView.item_strings.append("(Nothing was done)")

            else:
                self.ids.videoListView.item_strings.append("Cannot have single quote in videos path.")
                self.ids.videoListView.item_strings.append("(Nothing was done)")
            self.detectVideos()
        else:
            self.ids.videoListView.item_strings.append("Nothing to do (push refresh or move file back from "+videosDoneFolderString+" to "+videosFolderString+").")

    def skipVideo(self):
        global videosDoneFolderString
        global videosFolderString
        global dirsep
        global currentItem
        global videosSkippedFolderString
        global files
        if currentItem>=0:
            thisFile = files[currentItem]
            os.rename(path.join(videosFolderString,thisFile), path.join(videosSkippedFolderString,thisFile))
            self.detectVideos()
        else:
            self.ids.videoListView.item_strings.append("Nothing to do (push refresh or move file back from "+videosDoneFolderString+" to "+videosFolderString+").")

class IntroCompatiblizerApp(App):
    def build(self):
        return MainForm()

if __name__ == '__main__':
    IntroCompatiblizerApp().run()
