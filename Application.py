# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
import Resources
import sys
from PyQt5.QtCore import Qt, QTimer, QThread
from BlurWindow.blurWindow import blur
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from Google_Form_Solver import Google_Form_Solver
from threading import Thread
import Resources
import qdarkstyle
from PIL import Image
import pyautogui
import os
import webbrowser as wb

class Dark_Mode_Checker(QThread):
        def __init__(self, ui, parent= None):
                super().__init__(parent)
                self.ui = ui
                self.run()
                self.dark = False
        def run(self):
                self.timer = QTimer()
                self.timer.timeout.connect(self.showTime)
                self.start_Timer()
        def start_Timer(self):
                self.timer.start(7000)
        def showTime(self):
                check = Check_BG().Black_for_T_White_for_F()
                if check:
                        if not self.dark:
                                print("If Runned Because it was light already")
                                self.dark = True
                                self.ui.label_3.setStyleSheet("color: white")
                                self.ui.pushButton_9.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: white;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: black;
                                        padding: 15px;
                                        }""")
                                self.ui.pushButton_4.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: white;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: black;
                                        padding: 15px;
                                        }""")
                                self.ui.pushButton_6.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: white;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: black;
                                        padding: 15px;
                                        }""")
                                self.ui.pushButton_3.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: white;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: black;
                                        padding: 15px;
                                        }""")
                                self.ui.label_4.setStyleSheet("color:white")
                else:
                        if self.dark:
                                print("Else Runned Because it was dark already")
                                self.dark = False
                                self.ui.label_3.setStyleSheet("color: black")
                                self.ui.pushButton_9.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: black;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: white;
                                        padding: 15px;
                                        }""")
                                self.ui.pushButton_4.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: black;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: white;
                                        padding: 15px;
                                        }""")
                                self.ui.pushButton_6.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: black;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: white;
                                        padding: 15px;
                                        }""")
                                self.ui.pushButton_3.setStyleSheet("""QPushButton{
                                        border-radius: 15px;
                                        color: black;
                                        padding: 15px;
                                        }
                                        #QPushButton:hover{
                                        border-radius: 15px;
                                        background-color: darkblue;
                                        color: white;
                                        padding: 15px;
                                        }""")
                                self.ui.label_4.setStyleSheet("color:black")
        def endTimer(self):
                self.timer.stop()
class Check_BG:
    def __init__(self):
        pyautogui.screenshot().save(r'./ss.png')
        self.im = Image.open(r"./ss.png") # Can be many different formats.
        self.pix = self.im.load()
        self.total = 0
        self.black = 0
        self.white = 0
        for height in range(0, self.im.size[0]):
            for width in range(0, self.im.size[1]):
                self.total+=1
                r = self.pix[height,width][0]
                g = self.pix[height,width][1]
                b = self.pix[height,width][2]
                if r < 127 and g < 127  and b < 127:
                    self.black+=1
                else:
                    self.white+=1
                # print(f"Height: {height}\tWidth: {width} \tRGB:{self.pix[height,width]} \tWhite: {self.white} \tBlack:{self.black}")
        os.remove(r"./ss.png")
    def Black_for_T_White_for_F(self):
        if round((self.black/self.total)*100,1) > 50:
            return True
        else:
            return False
class Ui_MainWindow(object):    
        def __init__(self):
                self.stack_color = "white"
                self.app = QtWidgets.QApplication(sys.argv)
                MainWindow = QtWidgets.QMainWindow()
                self.setupUi(MainWindow)
                self.convert_Mainwindow_blur(MainWindow)
                self.connect_with_button()
                MainWindow.show()
                dm = Dark_Mode_Checker(self)
                sys.exit(self.app.exec_())
        def convert_Mainwindow_blur(self, MainWindow):
                MainWindow.setAttribute(Qt.WA_TranslucentBackground)
                MainWindow.setWindowFlag(Qt.FramelessWindowHint)
                hWnd = MainWindow.winId()
                blur(hWnd)        
        def close(self):
                sys.exit()
        def goto_solver(self):
                self.stackedWidget.setCurrentWidget(self.GoogleFormSolverPage)
        def goto_how_it_works(self):
                self.stackedWidget.setCurrentWidget(self.HowItWorksPage)
        def goto_setting(self):
                self.stackedWidget.setCurrentWidget(self.Setting)
        def connect_with_button(self):
                self.pushButton_9.clicked.connect(self.goto_solver)
                self.pushButton_4.clicked.connect(self.goto_how_it_works)
                self.pushButton_3.clicked.connect(self.goto_setting)
                self.pushButton_6.clicked.connect(self.close)
                self.pushButton_5.clicked.connect(self.start_process)
                self.pushButton_8.clicked.connect(self.go_dark_mode)
                self.pushButton_7.clicked.connect(self.go_light_mode)
                self.pushButton.clicked.connect(self.go_to_gmail)
        def show_and_hide_message(self):
                self.animatemessageview__height = QPropertyAnimation(self.Message_Label, b'maximumHeight')
                self.animatemessageview__height.setDuration(1000)
                self.animatemessageview__height.setStartValue(0)
                self.animatemessageview__height.setEndValue(100)
                self.animatemessageview__height.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.hidemessageanime_height = QPropertyAnimation(self.Message_Label, b'maximumHeight')
                self.hidemessageanime_height.setDuration(1000)
                self.hidemessageanime_height.setStartValue(100)
                self.hidemessageanime_height.setEndValue(0)
                self.hidemessageanime_height.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.Sequenceformessage = QSequentialAnimationGroup()
                self.Sequenceformessage.addAnimation(self.animatemessageview__height)
                self.Sequenceformessage.addAnimation(self.hidemessageanime_height)
                self.Sequenceformessage.start()
        def start_process(self):
                Google_doc_link = self.lineEdit.text()
                Repeat_time = self.lineEdit_2.text()
                if Google_doc_link == "":
                        self.Message_Label.setText("Please Provide Google Form Document Link!!!".upper())
                        self.show_and_hide_message()
                elif Repeat_time == "":
                        self.Message_Label.setText("Please Provide Repeat Value!!!".upper())
                        self.show_and_hide_message()
                else:
                        try:
                                Repeat_time =  int(Repeat_time)
                                def parallelFunc2(Google_doc_link,Repeat_time,label_14, Browser_display, comboBox):
                                        Form_Solver = Google_Form_Solver(Google_doc_link,Repeat_time, label_14, Browser_display, comboBox)
                                if self.checkBox.isChecked():
                                        if self.comboBox.currentText() == "Positive Response":
                                                th2 = Thread(target=parallelFunc2, args=[Google_doc_link,Repeat_time, self.label_14, True, True])
                                                th2.start()
                                        elif self.comboBox.currentText() == "Negative Response":
                                                th2 = Thread(target=parallelFunc2, args=[Google_doc_link,Repeat_time, self.label_14, True, False])
                                                th2.start()
                                else:
                                        if self.comboBox.currentText() == "Positive Response":
                                                th2 = Thread(target=parallelFunc2, args=[Google_doc_link,Repeat_time, self.label_14, False, True])
                                                th2.start()
                                        elif self.comboBox.currentText() == "Negative Response":
                                                th2 = Thread(target=parallelFunc2, args=[Google_doc_link,Repeat_time,self.label_14, False, False])
                                                th2.start()
                        except:
                                self.Message_Label.setText("Please input integer value in Repeat Input Field!!!".upper())
                                self.show_and_hide_message()
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(639, 435)
                MainWindow.setStyleSheet("QMainWindow{\n"
        "border-radius: 15px;\n"
        "background-color: lightgreen;\n"
        "padding: 15px;\n"
        "}")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.widget_2 = QtWidgets.QWidget(self.centralwidget)
                self.widget_2.setMaximumSize(QtCore.QSize(195, 16777215))
                self.widget_2.setStyleSheet("QPushButton{\n"
        "border-radius: 15px;\n"
        "color: black;\n"
        "padding: 15px;\n"
        "}\n"
        "#QPushButton:hover{\n"
        "border-radius: 15px;\n"
        "background-color: darkblue;\n"
        "color: white;\n"
        "padding: 15px;\n"
        "}\n"
        "")
                self.widget_2.setObjectName("widget_2")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
                self.verticalLayout.setObjectName("verticalLayout")
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem)
                self.label_3 = QtWidgets.QLabel(self.widget_2)
                font = QtGui.QFont()
                font.setFamily("Segoe UI Black")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.verticalLayout.addWidget(self.label_3)
                spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem1)
                self.widget_8 = QtWidgets.QWidget(self.widget_2)
                self.widget_8.setStyleSheet("QPushButton:hover{\n"
        "border-radius: 15px;\n"
        "background-color: darkblue;\n"
        "color: white;\n"
        "padding: 15px;\n"
        "}\n"
        "")
                self.widget_8.setObjectName("widget_8")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.label_9 = QtWidgets.QLabel(self.widget_8)
                self.label_9.setText("")
                self.label_9.setTextFormat(QtCore.Qt.PlainText)
                self.label_9.setPixmap(QtGui.QPixmap(":/Icons/Icons/check-square.svg"))
                self.label_9.setScaledContents(False)
                self.label_9.setWordWrap(False)
                self.label_9.setObjectName("label_9")
                self.horizontalLayout_6.addWidget(self.label_9, 0, QtCore.Qt.AlignLeft)
                self.pushButton_9 = QtWidgets.QPushButton(self.widget_8)
                self.pushButton_9.setObjectName("pushButton_9")
                self.horizontalLayout_6.addWidget(self.pushButton_9)
                self.verticalLayout.addWidget(self.widget_8)
                self.widget_5 = QtWidgets.QWidget(self.widget_2)
                self.widget_5.setStyleSheet("QPushButton:hover{\n"
        "border-radius: 15px;\n"
        "background-color: darkblue;\n"
        "color: white;\n"
        "padding: 15px;\n"
        "}\n"
        "")
                self.widget_5.setObjectName("widget_5")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_6 = QtWidgets.QLabel(self.widget_5)
                self.label_6.setText("")
                self.label_6.setTextFormat(QtCore.Qt.PlainText)
                self.label_6.setPixmap(QtGui.QPixmap(":/Icons/Icons/sliders.svg"))
                self.label_6.setScaledContents(False)
                self.label_6.setWordWrap(False)
                self.label_6.setObjectName("label_6")
                self.horizontalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignLeft)
                self.pushButton_4 = QtWidgets.QPushButton(self.widget_5)
                self.pushButton_4.setObjectName("pushButton_4")
                self.horizontalLayout_3.addWidget(self.pushButton_4)
                self.verticalLayout.addWidget(self.widget_5)
                self.widget_6 = QtWidgets.QWidget(self.widget_2)
                self.widget_6.setStyleSheet("QPushButton:hover{\n"
        "border-radius: 15px;\n"
        "background-color: darkblue;\n"
        "color: white;\n"
        "padding: 15px;\n"
        "}\n"
        "")
                self.widget_6.setObjectName("widget_6")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.label_7 = QtWidgets.QLabel(self.widget_6)
                self.label_7.setText("")
                self.label_7.setTextFormat(QtCore.Qt.PlainText)
                self.label_7.setPixmap(QtGui.QPixmap(":/Icons/Icons/settings.svg"))
                self.label_7.setScaledContents(False)
                self.label_7.setWordWrap(False)
                self.label_7.setObjectName("label_7")
                self.horizontalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft)
                self.pushButton_3 = QtWidgets.QPushButton(self.widget_6)
                self.pushButton_3.setObjectName("pushButton_3")
                self.horizontalLayout_4.addWidget(self.pushButton_3)
                self.verticalLayout.addWidget(self.widget_6)
                self.widget_7 = QtWidgets.QWidget(self.widget_2)
                self.widget_7.setStyleSheet("QPushButton:hover{\n"
        "border-radius: 15px;\n"
        "background-color: darkblue;\n"
        "color: white;\n"
        "padding: 15px;\n"
        "}\n"
        "")
                self.widget_7.setObjectName("widget_7")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.label_12 = QtWidgets.QLabel(self.widget_7)
                self.label_12.setText("")
                self.label_12.setTextFormat(QtCore.Qt.PlainText)
                self.label_12.setPixmap(QtGui.QPixmap(":/Icons/Icons/log-out.svg"))
                self.label_12.setScaledContents(False)
                self.label_12.setWordWrap(False)
                self.label_12.setObjectName("label_12")
                self.horizontalLayout_5.addWidget(self.label_12, 0, QtCore.Qt.AlignLeft)
                self.pushButton_6 = QtWidgets.QPushButton(self.widget_7)
                self.pushButton_6.setObjectName("pushButton_6")
                self.horizontalLayout_5.addWidget(self.pushButton_6)
                self.verticalLayout.addWidget(self.widget_7)
                spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem2)
                self.widget_3 = QtWidgets.QWidget(self.widget_2)
                self.widget_3.setObjectName("widget_3")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.label_4 = QtWidgets.QLabel(self.widget_3)
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.verticalLayout_4.addWidget(self.label_4)
                self.verticalLayout.addWidget(self.widget_3)
                self.horizontalLayout.addWidget(self.widget_2)
                self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
                self.stackedWidget.setStyleSheet("QStackedWidget{\n"
        "background-color: white;\n"
        "border-radius: 15px;\n"
        "}")
                self.stackedWidget.setObjectName("stackedWidget")
                self.GoogleFormSolverPage = QtWidgets.QWidget()
                self.GoogleFormSolverPage.setObjectName("GoogleFormSolverPage")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.GoogleFormSolverPage)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.Containar = QtWidgets.QWidget(self.GoogleFormSolverPage)
                self.Containar.setObjectName("Containar")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Containar)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.Heading = QtWidgets.QLabel(self.Containar)
                font = QtGui.QFont()
                font.setFamily("Segoe UI Black")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.Heading.setFont(font)
                self.Heading.setAlignment(QtCore.Qt.AlignCenter)
                self.Heading.setObjectName("Heading")
                self.verticalLayout_2.addWidget(self.Heading)
                self.Message_Label = QtWidgets.QLabel(self.Containar)
                self.Message_Label.setMaximumSize(QtCore.QSize(16777215, 0))
                self.Message_Label.setStyleSheet("#Message_Label{\n"
        "background-color: lightgreen;\n"
        "border-radius:15px;\n"
        "border: 2px solid green;\n"
        "padding: 10px;\n"
        "}")
                self.Message_Label.setObjectName("Message_Label")
                self.verticalLayout_2.addWidget(self.Message_Label)
                spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem3)
                self.widget = QtWidgets.QWidget(self.Containar)
                self.widget.setStyleSheet("QPushButton:hover{\n"
        "border-radius: 15px;\n"
        "background-color: grey;\n"
        "color: white;\n"
        "padding: 15px;\n"
        "}\n"
        "QPushButton{\n"
        "border-radius: 15px;\n"
        "background-color: lightblue;\n"
        "color: black;\n"
        "padding: 15px;\n"
        "}\n"
        "QLineEdit{\n"
        "border-radius:15px;\n"
        "padding:15px;\n"
        "border: 2px solid grey;\n"
        "}\n"
        "QLineEdit:focus{\n"
        "border-radius:15px;\n"
        "padding:15px;\n"
        "border: 2px solid black;\n"
        "}\n"
        "")
                self.widget.setObjectName("widget")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.label = QtWidgets.QLabel(self.widget)
                self.label.setObjectName("label")
                self.verticalLayout_3.addWidget(self.label)
                self.lineEdit = QtWidgets.QLineEdit(self.widget)
                self.lineEdit.setObjectName("lineEdit")
                self.verticalLayout_3.addWidget(self.lineEdit)
                self.label_2 = QtWidgets.QLabel(self.widget)
                self.label_2.setObjectName("label_2")
                self.verticalLayout_3.addWidget(self.label_2)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.verticalLayout_3.addWidget(self.lineEdit_2)
                self.label_15 = QtWidgets.QLabel(self.widget)
                self.label_15.setObjectName("label_15")
                self.verticalLayout_3.addWidget(self.label_15)
                self.comboBox = QtWidgets.QComboBox(self.widget)
                self.comboBox.setStyleSheet("border-radius: 15px;\n"
        "padding: 5px;\n"
        "border: 2px solid grey;")
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.verticalLayout_3.addWidget(self.comboBox)
                self.checkBox = QtWidgets.QCheckBox(self.widget)
                self.checkBox.setObjectName("checkBox")
                self.verticalLayout_3.addWidget(self.checkBox)
                self.pushButton_5 = QtWidgets.QPushButton(self.widget)
                self.pushButton_5.setObjectName("pushButton_5")
                self.verticalLayout_3.addWidget(self.pushButton_5)
                self.label_13 = QtWidgets.QLabel(self.widget)
                self.label_13.setObjectName("label_13")
                self.verticalLayout_3.addWidget(self.label_13)
                self.label_14 = QtWidgets.QLabel(self.widget)
                self.label_14.setObjectName("label_14")
                self.verticalLayout_3.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_2.addWidget(self.widget)
                spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem4)
                self.verticalLayout_5.addWidget(self.Containar)
                self.stackedWidget.addWidget(self.GoogleFormSolverPage)
                self.HowItWorksPage = QtWidgets.QWidget()
                self.HowItWorksPage.setObjectName("HowItWorksPage")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.HowItWorksPage)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_6.addItem(spacerItem5)
                self.label_5 = QtWidgets.QLabel(self.HowItWorksPage)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(26)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.verticalLayout_6.addWidget(self.label_5)
                self.textBrowser = QtWidgets.QTextBrowser(self.HowItWorksPage)
                self.textBrowser.setObjectName("textBrowser")
                self.verticalLayout_6.addWidget(self.textBrowser)
                spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_6.addItem(spacerItem6)
                self.stackedWidget.addWidget(self.HowItWorksPage)
                self.Setting = QtWidgets.QWidget()
                self.Setting.setObjectName("Setting")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Setting)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.label_8 = QtWidgets.QLabel(self.Setting)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(26)
                font.setBold(True)
                font.setWeight(75)
                self.label_8.setFont(font)
                self.label_8.setAlignment(QtCore.Qt.AlignCenter)
                self.label_8.setObjectName("label_8")
                self.verticalLayout_7.addWidget(self.label_8)
                spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_7.addItem(spacerItem7)
                self.widget_4 = QtWidgets.QWidget(self.Setting)
                self.widget_4.setStyleSheet("QPushButton{\n"
        "background-color:grey;\n"
        "border-radius: 15px;\n"
        "padding: 15px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: lightgreen;\n"
        "border-radius: 15px;\n"
        "padding: 15px;\n"
        "}")
                self.widget_4.setObjectName("widget_4")
                self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
                self.gridLayout.setObjectName("gridLayout")
                self.label_10 = QtWidgets.QLabel(self.widget_4)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setObjectName("label_10")
                self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
                self.label_11 = QtWidgets.QLabel(self.widget_4)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.label_11.setFont(font)
                self.label_11.setObjectName("label_11")
                self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
                self.pushButton = QtWidgets.QPushButton(self.widget_4)
                self.pushButton.setObjectName("pushButton")
                self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
                self.pushButton_7 = QtWidgets.QPushButton(self.widget_4)
                self.pushButton_7.setStyleSheet("QPushButton:hover{\n"
        "background-color: red;\n"
        "border-radius: 15px;\n"
        "padding: 15px;\n"
        "}")
                self.pushButton_7.setObjectName("pushButton_7")
                self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
                self.pushButton_8 = QtWidgets.QPushButton(self.widget_4)
                self.pushButton_8.setObjectName("pushButton_8")
                self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
                self.verticalLayout_7.addWidget(self.widget_4)
                spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_7.addItem(spacerItem8)
                self.stackedWidget.addWidget(self.Setting)
                self.horizontalLayout.addWidget(self.stackedWidget)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_3.setText(_translate("MainWindow", "Menu"))
                self.pushButton_9.setText(_translate("MainWindow", "Google Form Solver"))
                self.pushButton_4.setText(_translate("MainWindow", "How it works?"))
                self.pushButton_3.setText(_translate("MainWindow", "Setting"))
                self.pushButton_6.setText(_translate("MainWindow", "Exit"))
                self.label_4.setText(_translate("MainWindow", "(C) Created By Team Mutavir 2023"))
                self.Heading.setText(_translate("MainWindow", "Google Form Solver V 1.0"))
                self.Message_Label.setText(_translate("MainWindow", "Message_Label"))
                self.label.setText(_translate("MainWindow", "Google Form Link:"))
                self.label_2.setText(_translate("MainWindow", "Repeat Time: (Must be a number)"))
                self.label_15.setText(_translate("MainWindow", "Response Type:"))
                self.comboBox.setItemText(0, _translate("MainWindow", "Positive Response"))
                self.comboBox.setItemText(1, _translate("MainWindow", "Negative Response"))
                self.checkBox.setText(_translate("MainWindow", "Show Browser"))
                self.pushButton_5.setText(_translate("MainWindow", "Activate"))
                self.label_13.setText(_translate("MainWindow", "Progress:"))
                self.label_14.setText(_translate("MainWindow", "None"))
                self.label_5.setText(_translate("MainWindow", "How it works?"))
                self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Following are some of the steps, you have to follow:</span></p>\n"
        "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Put your link in the </span><span style=\" font-size:9pt; font-weight:600;\">Google Form Link</span><span style=\" font-size:9pt;\"> input field.</span></p>\n"
        "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2.Then put the value how many time you want the software to solve the form for you in the </span><span style=\" font-size:9pt; font-weight:600;\">Repeat </span><span style=\" font-size:9pt;\">input field.</span></p>\n"
        "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3.Then click </span><span style=\" font-size:9pt; font-weight:600;\">Submit </span><span style=\" font-size:9pt;\">and that\'s all it takes.</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow", "Setting"))
                self.label_10.setText(_translate("MainWindow", "Dark Mode"))
                self.label_11.setText(_translate("MainWindow", "For Feedback Contact us on"))
                self.pushButton.setText(_translate("MainWindow", "Gmail"))
                self.pushButton_7.setText(_translate("MainWindow", "Off"))
                self.pushButton_8.setText(_translate("MainWindow", "On"))
        def go_dark_mode(self):
                self.stack_color = "black"
                self.stackedWidget.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()+"QStackedWidget{border-radius: 15px;\n}")
        def go_light_mode(self):
                self.stack_color = "white"
                self.stackedWidget.setStyleSheet("QStackedWidget{\n"
        "background-color: white;\n"
        "border-radius: 15px;\n"
        "}")
        def go_to_gmail(self):
                wb.open("https://mail.google.com/mail/?view=cm&fs=1&to=umer.fiesta2762@gmail.com&su=Feedback%20for%20Google%20Form%20Solver&body=Let%20Us%20know%20what%20you%20need.") 

# Generate Thread to generate GUI
# =======================================
def run_gui():
        ui = Ui_MainWindow()
th = Thread(target=run_gui)
th.start()