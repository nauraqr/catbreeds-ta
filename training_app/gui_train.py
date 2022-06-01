from PyQt5 import QtCore, QtGui, QtWidgets

class TrainGui(QtWidgets.QMainWindow):
    def initUi(self, TrainWindow):
        TrainWindow.setObjectName("TrainWindow")
        TrainWindow.resize(476, 300)
        self.centralwidget = QtWidgets.QWidget(TrainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 461, 100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.select_dir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_dir.setObjectName("select_dir")
        self.gridLayout.addWidget(self.select_dir, 2, 0, 1, 1)
        
        self.start_train = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_train.setObjectName("start_train")
        self.gridLayout.addWidget(self.start_train, 2, 1, 1, 1)
        
        self.label_dir = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_dir.setStyleSheet("")
        self.label_dir.setObjectName("label_dir")
        self.label_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dir.setFont(QtGui.QFont('Arial', 9))
        self.gridLayout.addWidget(self.label_dir, 1, 0, 1, 2)

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(16, 10, 451, 20))
        self.label_title.setObjectName("label_title")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setFont(QtGui.QFont('Arial', 13))
        
        self.dialog_box = QtWidgets.QMessageBox()
        
        TrainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TrainWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainWindow)    
        
    def retranslateUi(self, TrainWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainWindow.setWindowTitle(_translate("TrainWindow", "Cat Breeds Training"))
        self.select_dir.setToolTip(_translate("TrainWindow", "<html><head/><body><p>Load dataset</p></body></html>"))
        self.select_dir.setText(_translate("TrainWindow", "Load Dataset"))
        self.start_train.setToolTip(_translate("TrainWindow", "<html><head/><body><p>Train image</p></body></html>"))
        self.start_train.setText(_translate("TrainWindow", "Start Training"))
        self.label_title.setText(_translate("TrainWindow", "Cat Breeds Training"))
        self.label_dir.setToolTip(_translate("TrainWindow", "<html><head/><body><p>Folder Directory</p></body></html>"))