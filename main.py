import numpy as np
from tensorflow.keras.models import load_model
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from gui_main import MainGui

import os
import time

filePath = []

class MainApp(MainGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi(self)
        self.select_dir.clicked.connect(self.select_image)
        self.start_pred.clicked.connect(self.predict_image)
        
    def show_error_dialog(self):
        self.dialog_box.setWindowTitle("Notice")
        self.dialog_box.setText("No image found!")
        self.dialog_box.exec()

    def select_image(self):
        global filePath
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load image", "", "Image Files (*.png *.jpg *jpeg)")
        if fileName:
            filePath.append(fileName)
            pixmap = QtGui.QPixmap(fileName)
            pic = pixmap.scaled(299, 299, QtCore.Qt.KeepAspectRatio)
            self.label_img.setPixmap(QtGui.QPixmap(pic))
            self.label_img.setAlignment(QtCore.Qt.AlignCenter)
    
    def predict_image(self):
        if(len(filePath) == 0):
            self.show_error_dialog()
        else:
            start_time = time.time()
            cat_cascade = cv2.CascadeClassifier('catface.xml')
            MODEL_PATH = 'model/cat_model.h5'
            model = load_model(MODEL_PATH,compile=False)
        
            path = os.path.join(filePath[-1])
            cat_img = cv2.imread(path)
            gray = cv2.cvtColor(cat_img, cv2.COLOR_BGR2GRAY)
            cats = cat_cascade.detectMultiScale(gray, scaleFactor = 1.01, minNeighbors = 5)
            
            if(len(cats) == 0):
                self.dialog_box.setWindowTitle("Notice")
                self.dialog_box.setText("No cat founds")
                self.dialog_box.exec()
            else:
                for (i, (x, y, w, h)) in enumerate(cats):  
                    roi_rgb = cat_img[y:y+h, x:x+w]
                    new_array = cv2.resize(roi_rgb, (299,299))
                    pic_matrix = np.array(new_array)/255
                    pic_matrix = pic_matrix.reshape(1, 299, 299, 3)
                    model_predict = model.predict(pic_matrix)
                    cat_predict = np.argmax(model_predict)
                    #proba_predict = "%.2f" % (np.max(model_predict)*100) +"%"
                    labels = ['Bengal', 'Calico', 'Persian', 'Siamese', 'Sphynx']
                    
                    cv2.rectangle(cat_img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(cat_img,"#{} ".format(i + 1) + labels[int(cat_predict)], 
                                (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.55, (0, 0, 255), 1)
                
                respond_time = "%.2f" % (time.time() - start_time)
                format_time = 'Respond Time: {0}s'.format(respond_time)
                cv2.putText(cat_img, format_time,(0, 20), cv2.FONT_HERSHEY_DUPLEX, 0.55, (0, 0, 255), 1)
                cv2.imshow("Image Result", cat_img)
                cv2.imwrite("result/cat_result.jpg", cat_img)
    
def main():
    app = QtWidgets.QApplication([])
    cat_test = MainApp()
    cat_test.show()
    app.exec_()

if __name__ == "__main__":
    main()
