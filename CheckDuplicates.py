
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel
import sys
#import pandas as pd
#from pandasModel import pandasModel



class Ui_Mainwindow(object):

    def duplicate_check(self):

        x = self.textEdit.toPlainText()  #anchorAt(Mainwindow)  #text()
        self.label_2.setText("Duplicates :")

        y= x.splitlines()
        lst = list(y)

# using regular logic

        data_list = []
        final_list = []
        for item in lst:

            if item not in final_list:

                final_list.append(item)
            else:
                data_list.append(item)

            str0 = ""

            for elem in data_list:
                str0 = str0 + elem  + "\n                             \n"
                str2 = str0.rstrip().lstrip()
                self.textEdit_2.setText(str(str2))





            #data_list.reverse()
            #rev_data2 = data_list[0]
            #self.textEdit_2.setText(str(data_list))


            #else:
             #   data_list.append(item)
              #  data_list2 = data_list.append(item)
               # print(item)
                #self.textEdit_2.setText("item")
        #self.textEdit_2.setText(data_list2)
                #data = []
                #data_final = data.append(item)

            #return final_list
        #data = final_list


### using dataframes
        #df = pd.DataFrame(lst)
        #dp = df.duplicated()
        #y = df[dp]
        #self.textEdit_2.setText(str(y))


    def clear(self):
        self.textEdit.clear()
        self.textEdit_2.clear()


#
    def Tenants(self):
        x = self.textEdit.toPlainText()  # anchorAt(Mainwindow)  #text()
        self.label_2.setText("Duplicates :")


        y = x.splitlines()
        lst = list(y)
        # using regular logic
        data_list = []
        final_list = []
        for item in lst:

            if item not in final_list:

                final_list.append(item)
            else:
                data_list.append(item)

            str1 = ""
            strd2 = ""

            for elem in data_list:

                elem2 = elem.rstrip().lstrip().split()
                finalelem = elem2[6]
                strd = finalelem + "\n"
                strd2 = strd2 + strd
                self.textEdit_2.setText(str(strd2))



                #strd = " " + finalelem
                #strd2 = strd [:]

                #str1 = str1 + strd2 + "\n                             \n"

    def NoDuplicates(self):

        x = self.textEdit.toPlainText()  # anchorAt(Mainwindow)  #text()

        y = x.splitlines()
        lst = list(y)

        # using regular logic

        data_list = []
        final_list = []
        for item in lst:

            if item not in final_list:

                final_list.append(item)


            else:
                data_list.append(item)

            str0 = ""

            for elem in final_list:
                str0 = str0 + elem   + "\n                             \n"
                str2 = str0.rstrip().lstrip()
                self.textEdit_2.setText(str(str2))
        self.label_2.setText("NoDuplicates :")





    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(884, 832)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Mainwindow.setFont(font)
        Mainwindow.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("CD")
        Mainwindow.setWindowIcon(icon)
        Mainwindow.setAnimated(True)
        Mainwindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        Mainwindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setObjectName("centralwidget")

   #     self.Labelname = QLabel(Mainwindow)
    #    self.Labelname.setText('Name')
     #   self.Labelname.move(80, 20)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(400, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("checkduplicates")

        self.pushButton.clicked.connect(self.duplicate_check)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 141, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic Semilight")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 510, 141, 131))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic Semilight")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

       # self.textbox = QLineEdit(Mainwindow)

        #self.textbox.move(200, 200)
###
#        self.process = QtCore.QProcess()
#        self.process.readyReadStandardOutput.connect(self.stdoutReady)
#        self.process.readyReadStandardError.connect(self.stderrReady)

###
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 10, 661, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.textEdit.setFont(font)
        #self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)





        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 410, 661, 341))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit_2.setObjectName("textEdit_2")
        Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuexit = QtWidgets.QMenu(self.menubar)
        self.menuexit.setObjectName("menuexit")
        Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mainwindow)
        self.statusbar.setObjectName("statusbar")
        Mainwindow.setStatusBar(self.statusbar)
        self.menuexit.addSeparator()
        self.menuexit.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuexit.menuAction())
##########
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setEnabled(True)
        self.pushButton1.setGeometry(QtCore.QRect(160, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton1.setFlat(False)
        self.pushButton1.setObjectName("clear")
        self.pushButton1.clicked.connect(self.clear)

#########
#get tenants button


        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setEnabled(True)
        self.pushButton2.setGeometry(QtCore.QRect(550, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setFlat(False)
        self.pushButton2.setObjectName("checkduplicates")

        self.pushButton2.clicked.connect(self.Tenants)


###############No duplicates button

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setEnabled(True)
        self.pushButton3.setGeometry(QtCore.QRect(700, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton3.setFlat(False)
        self.pushButton3.setObjectName("checkduplicates")

        self.pushButton3.clicked.connect(self.NoDuplicates)

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)



        #self.pandasTv = QtWidgets.QTableView(self)



    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "CheckDuplicates"))
        self.pushButton.setText(_translate("Mainwindow", "Duplicate Commands"))
        self.pushButton1.setText(_translate("Mainwindow", "Clear"))
        self.pushButton2.setText(_translate("Mainwindow", "Duplicate Tenants"))
        self.pushButton3.setText(_translate("Mainwindow", "NoDuplicates"))
        self.label.setText(_translate("Mainwindow", "Enter data :"))
        self.label_2.setText(_translate("Mainwindow", "Duplicates :"))
        self.menuFile.setTitle(_translate("Mainwindow", "File"))
        self.menuexit.setTitle(_translate("Mainwindow", "exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_Mainwindow()

    ui.setupUi(Mainwindow)

    Mainwindow.show()
    sys.exit(app.exec_())
