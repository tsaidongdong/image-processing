import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget

import Ui_hw2

if __name__=='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_hw2.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())