import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.models import Sequential
from keras.layers.pooling import GlobalAveragePooling2D
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject
from trainingoptions import TrainingOptions

class WorkerSignals(QObject):
    update = pyqtSignal(object)
    finish = pyqtSignal()

class TrainerModel(QRunnable):
    def __init__(self, opts: TrainingOptions):
        QRunnable.__init__(self)
        
        self.opts = opts
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            model = self.build_model()

            training_datagen = self.build_datagen(validation=False)
            training_dataflow = self.build_dataflow(training_datagen, validation=False)

            validation_datagen = self.build_datagen(validation=True)
            validation_dataflow = self.build_dataflow(validation_datagen, validation=True)
            
            base_path = 'train_model'
            trained_model_path = base_path + 'train_model/'
            model_names = trained_model_path + '.{epoch:02d}-{val_acc:.2f}.h5'
            
            earlystopping = EarlyStopping(monitor ="val_loss", 
                                          mode = "auto", patience = 15, 
                                          restore_best_weights = True)
            
            checkpoint = ModelCheckpoint(model_names, monitor = 'val_loss',
                                         mode = 'auto', verbose = 1,
                                         save_best_only = True)
            
            history = model.fit(training_dataflow,
                                steps_per_epoch = len(training_dataflow),
                                validation_data = validation_dataflow,
                                validation_steps = len(validation_dataflow),
                                epochs = 100, verbose = 1, callbacks=[checkpoint, earlystopping])
            
            model.save('model/model.h5')
        finally:
            self.signals.finish.emit()

    def build_model(self):
        shape = (299, 299)
        channel = (3, )
        input_size = shape + channel

        base_model = Xception(include_top=False, 
                              weights='imagenet', 
                              input_tensor=None,
                              input_shape=input_size, 
                              pooling=max, classes=3,
                              classifier_activation='softmax')

        model = Sequential()
        model.add(base_model)
        model.add(GlobalAveragePooling2D())
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(3, activation = 'softmax'))
        
        base_model.trainable = False
        
        model.compile(optimizer = Adam(),
                     loss="categorical_crossentropy",
                     metrics=["acc"])

        return model

    def build_datagen(self, validation=False):
        if validation:
            gen = ImageDataGenerator(rescale = 1. / 255,
                                  horizontal_flip = True)
        else:
            gen = ImageDataGenerator(rescale = 1./255, 
                                 rotation_range = 30, 
                                 width_shift_range = 0.2,
                                 height_shift_range = 0.2,
                                 shear_range = 0.2,
                                 zoom_range = 0.2,
                                 horizontal_flip = True)

        return gen

    def build_dataflow(self, datagen, validation=False):
        if validation:
            return datagen.flow_from_directory(self.opts.path_dir+'/val/',
                                          target_size = (299,299),
                                          batch_size = 32,
                                          class_mode = 'categorical',
                                          shuffle = False)
        else:
            return datagen.flow_from_directory(self.opts.path_dir+'/train/',
                                          target_size = (299,299),
                                          batch_size = 32,
                                          class_mode = 'categorical',
                                          shuffle = False)
