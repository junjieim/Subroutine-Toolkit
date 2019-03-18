from ui_MainWindow import Ui_MainWindow
import sys
import subprocess
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtWidgets, QtGui


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.working_dir = sys.path[0]
        self.inp_name = ''
        self.for_name = ''

        self.input_working_dir.setText(self.working_dir)

    def slot_runScrit(self):
        # delete the old data
        tmplist = []
        files = [f for f in os.listdir(self.working_dir) if not os.path.isdir(f)]
        for file in files:
            if ((not file == self.input_inp.text())
                    and file.split('.')[0] == self.input_inp.text().split('.')[0]):
                tmplist.append(file)
                # os.remove(file)
        print(tmplist)

        # run abaqus script
        cmd_line = "abaqus job={job} user={forName} int".format(job=self.input_inp.text().split('.')[0],
                                                                    forName=self.input_for.text())
        # subprocess.call(cmd_line)
        print(cmd_line)

    def slot_setWorkingDir(self):
        self.working_dir = QFileDialog.getExistingDirectory(self,
                                                            "Select the working direction:",
                                                            sys.path[0])
        self.input_working_dir.setText(self.working_dir)
        pass

    def slot_setInpName(self):
        self.inp_name = self.getFileName(".inp")
        self.input_inp.setText(os.path.basename(self.inp_name))

    def slot_setForName(self):
        self.for_name = self.getFileName(".for")
        self.input_for.setText(os.path.basename((self.for_name)))

    def slot_dataDealing(self):
        pass

    def slot_update(self):
        pass

    def getFileName(self, str):
        title = "Select the {str} file:".format(str=str)
        filetype = "{str1} File (*{str2})".format(str1=str, str2=str)
        filename, ret = QFileDialog.getOpenFileName(self,
                                                         title,
                                                         self.input_working_dir.text(),
                                                         filetype)
        return filename


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
