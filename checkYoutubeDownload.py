from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
from PyQt5.QtWidgets import *
import pafy


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('assets/ui/youtubedownload.ui', self)
        self.show()
        # self.initUI()
        self.handleButtons()

    def initUI(self):
        # contain all the ui changes in loading
        pass

    def handleButtons(self):
        self.downloadButton.clicked.connect(self.downloadAudio)
        self.checkButton.clicked.connect(self.getVideoData)
        self.saveButton.clicked.connect(self.chooseSaveLocation)

    def getVideoData(self):
        video_url = self.downLink.text()
        if video_url == '':
            QMessageBox.warning(self, "Invalid URL", "Please enter a valid YouTube URL")
        else:
            video = pafy.new(video_url)
            print(video.title)

    def chooseSaveLocation(self):
        save_location = QFileDialog.getSaveFileName(self, caption="Save as", directory=".", filter='All Files(*.*)')
        self.saveLoc.setText(save_location[0])


    def downloadAudio(self):
        video_url = self.downLink.text()
        save_location = self.saveLoc.text()

        if video_url == '' or save_location == '':
            QMessageBox.warning(self, "Check Again", "Invalid URL or Save Location")
        else:
            video = pafy.new(video_url)
            bestaudio = video.getbestaudio()
            print(bestaudio)
            bestaudio.download(filepath=save_location + '.mp3')
            out_text = video.title + ' has finished downloading!'
            QMessageBox.information(self, "Download Completed!", out_text)
            self.downLink.setText('')
            self.saveLoc.setText('')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
