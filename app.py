import sys
from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QWidget, 
    QHBoxLayout, QVBoxLayout, QTextEdit,
    QPushButton
)
from googletrans import Translator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.main_layout = QVBoxLayout()
        self.editors_layout = QHBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.origin = QTextEdit()
        self.destination = QTextEdit()
        self.translate_btn = QPushButton("Translate")
        self.import_file_btn = QPushButton("Import File")

        self.destination.setReadOnly(True)
        self.translate_btn.clicked.connect(self.translate)
        self.import_file_btn.clicked.connect(self.import_file)

        self.editors_layout.addWidget(self.origin)
        self.editors_layout.addWidget(self.destination)
        self.buttons_layout.addWidget(self.translate_btn)
        self.buttons_layout.addWidget(self.import_file_btn)
        self.main_layout.addLayout(self.editors_layout)
        self.main_layout.addLayout(self.buttons_layout)

        window = QWidget()
        window.setLayout(self.main_layout)

        self.setWindowTitle("Translator")
        self.setCentralWidget(window)
    
    def translate(self):
        translator = Translator()
        input_text = self.origin.toPlainText()
        if input_text:
            trans = translator.translate(input_text, dest="ar")
            self.destination.setPlainText(trans.text)
    
    def import_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', '/', '*.txt')
        words = self.__read_file(file_path[0])
        for word in words:
            self.origin.append(word+"\n")
    
    def __read_file(self, file_path):
        with open(file_path) as f:
            lines = [line.replace('\n', '') for line in f.readlines()]
            return list(filter(lambda line: line != '', lines))
        return []


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
