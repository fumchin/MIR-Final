from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys
import ui
from Audio import Audio
# from test import MplCanvas
# class MplCanvas(FigureCanvasQTAgg):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)

class MainFrame(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        self.setupUi(self)
        self.audio = None
        self.button_music_import.triggered.connect(self.open_file_dialog_and_read_audio)
        
    

    def open_file_dialog_and_read_audio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose your file", r"C:\Users\fumchin\Music","All Files (*);;MP3 Files (*.mp3);;WAV Files (*.wav)", options=options)
        if fileName:
            print(fileName)
        self.audio = Audio(fileName)
        # print(self.audio.y)

def main():
    app = QApplication(sys.argv)
    form = MainFrame()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()