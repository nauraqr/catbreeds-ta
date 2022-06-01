from PyQt5 import QtWidgets, QtCore

from gui_train import TrainGui
from trainingmodel import TrainerModel
from trainingoptions import TrainingOptions

class TrainingApp(TrainGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi(self)

        self.threadpool = QtCore.QThreadPool()

        self.trainer_thread = None

        self.path_dir = None
        self.select_dir.clicked.connect(self.select_path_dir)
        self.start_train.clicked.connect(self.run_training)
    
    def show_error_dialog(self):
        self.dialog_box.setWindowTitle("Notice")
        self.dialog_box.setText("No dataset found!")
        self.dialog_box.exec()
        
    def select_path_dir(self):
        dirname = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        self.path_dir = dirname
        self.label_dir.setText("Dataset directory: "+self.path_dir)
        
    def run_training(self):
        opts = TrainingOptions()
        opts.path_dir = self.path_dir
        if(opts.path_dir is None):
            self.show_error_dialog()
        else:
            self.trainer_thread = TrainerModel(opts)
            self.trainer_thread.signals.finish.connect(self.thread_finished)
            self.threadpool.start(self.trainer_thread)
            self.start_train.setText("Cancel training")
        
    def thread_finished(self):
        self.trainer_thread = None
        self.start_train.setText("Trained")

def main():
    app = QtWidgets.QApplication([])
    trainer = TrainingApp()
    trainer.show()
    app.exec_()

if __name__ == "__main__":
    main()