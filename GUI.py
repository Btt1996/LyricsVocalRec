
from lyricsByModules import song , res,artist ,lyrics
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys
from gtts import gTTS
import os
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # set the title
        self.setWindowTitle("Label")
  
        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)
  
        # creating a label widget
        # by default label will display at top left corner
        self.label_1 = QLabel(song, self)
  
        # moving position
        self.label_1.move(100, 100)
  
        # setting font and size
        self.label_1.setFont(QFont('Arial', 15))
  
        # creating a label widget
        # by default label will display at top left corner
        self.label_2 = QLabel(res, self)
  
        # moving position
        self.label_2.move(100, 120)
  
        # setting font and size
        self.label_2.setFont(QFont('Times', 10))
  
  
        # show all the widgets
        self.show()
  

App = QApplication(sys.argv)
with open("lyrics of "+song+" by "+artist+".txt", "w") as outfile:
     print("attendez pour avoir "+artist+" de "+song)  
     outfile.write(res) 

window = Window()
myobj = gTTS(text="ok your Lyrics for "+song+" by "+artist+"have been saved succesfully", lang="en", slow=False)
myobj.save("ok.mp3")
os.system("mpg321 ok.mp3")

sys.exit(App.exec())
