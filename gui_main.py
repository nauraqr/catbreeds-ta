from PyQt5 import QtCore, QtGui, QtWidgets

class MainGui(QtWidgets.QMainWindow):
    def initUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 461, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.select_dir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_dir.setObjectName("select_dir")
        self.gridLayout.addWidget(self.select_dir, 3, 0, 1, 1)
        
        self.start_pred = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_pred.setObjectName("start_pred")
        self.gridLayout.addWidget(self.start_pred, 3, 1, 1, 1)
        
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(16, 10, 451, 20))
        self.label_title.setObjectName("label_title")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setFont(QtGui.QFont('Arial', 13))
        
        self.label_img = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_img.setStyleSheet("")
        self.label_img.setObjectName("label")
        self.gridLayout.addWidget(self.label_img, 2, 0, 1, 2)
        
        self.dialog_box = QtWidgets.QMessageBox()
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cat Breeds Classifier"))
        self.select_dir.setToolTip(_translate("MainWindow", "<html><head/><body><p>Load image</p></body></html>"))
        self.select_dir.setText(_translate("MainWindow", "Load"))
        self.start_pred.setToolTip(_translate("MainWindow", "<html><head/><body><p>Classify image</p></body></html>"))
        self.start_pred.setText(_translate("MainWindow", "Classify"))
        self.label_title.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cat Breeds Classification</p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "Cat Breeds Classifier"))
        self.label_img.setToolTip(_translate("MainWindow", "<html><head/><body><p>Image area</p></body></html>"))
    
