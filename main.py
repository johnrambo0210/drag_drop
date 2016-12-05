import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import subprocess


class MyListWidget(QListWidget):
  def __init__(self, parent):
    super(MyListWidget, self).__init__(parent)
    self.setAcceptDrops(True)
    self.setDragDropMode(QAbstractItemView.InternalMove)

  def dragEnterEvent(self, event):
    if event.mimeData().hasUrls():
      event.acceptProposedAction()
    else:
      super(MyListWidget, self).dragEnterEvent(event)

  def dragMoveEvent(self, event):
    super(MyListWidget, self).dragMoveEvent(event)

  def dropEvent(self, event):
    if event.mimeData().hasUrls():
      for url in event.mimeData().urls():
        self.addItem(url.path())
      event.acceptProposedAction()
      file_path = str(url.path())[1:]
      print file_path
      if " " in file_path:
          new_path = []
          line = file_path.split("/")
          for x in line:
              if " " in x:
                  new_path.append('"' + x + '"')
              else :
                  new_path.append(x)

          file_path = "\\".join(new_path)
          #file_path = "\\".join(line[:-1]) + '\\"' + line[-1] + '"'
      print "Path", file_path
      os.system("start " + file_path)

    else:
      super(MyListWidget,self).dropEvent(event)

class MyWindow(QWidget):

  def __init__(self):
    super(MyWindow,self).__init__()
    self.setGeometry(100,100,300,400)
    self.setWindowTitle("Filenames")

    self.list = MyListWidget(self)
    layout = QVBoxLayout(self)
    layout.addWidget(self.list)
    self.items = []

    self.setLayout(layout)

  def build_list(self):
      for index in xrange(self.list.count()):
         items.append(self.list(index))
      print self.items

if __name__ == '__main__':

  app = QApplication(sys.argv)
  app.setStyle("plastique")

  window = MyWindow()
  window.show()

  sys.exit(app.exec_())




"""
os.system("start " + str(file_name))
"""
