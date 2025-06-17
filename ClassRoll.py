import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



def window():
    app = QApplication(sys.argv) #This starts said app

    window = QWidget() #Makes a blank window

    label = QLabel(window) #Creates a label. Labels are for showing text or images

    label.setText("Student:") #This sets what the label says

    window.setGeometry(100,100,200,300) #Sets the sizes of the window

    label.move(50,20) #Moves the label inside the window

    window.setWindowTitle("Class Roll") #Changes title bar to say Class Roll

    window.show() #Makes the window appear

    sys.exit(app.exec_()) #Starts the event loop (listens for clicks, close buttons, etc.)

if __name__ == '__main__': #This runs window() only if you run this file directly.

    window()