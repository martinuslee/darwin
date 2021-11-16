import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from Bio import SeqIO
import random
import os

class ThreadClass(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        try:
            self.parent.label_state.setText("File Reading...")

            # File Read
            fastq1 = self.parent.label.text()
            fastq2 = self.parent.label2.text()

            record_dict, record2_dict= SeqIO.index(fastq1, "fastq"), SeqIO.index(fastq2, "fastq")

            sampleRecords, sampleRecords_2 = [], []
            keys = random.sample(list(record_dict), 10)
            keys = sorted(keys)
            for k in keys:
                sampleRecords.append(record_dict[k])
                sampleRecords_2.append(record2_dict[k])

            print(os.path.dirname(fastq1) + "/r10" + os.path.basename(fastq1))
            # File Write

            self.parent.label_state.setText("File Writting...")
            SeqIO.write(sampleRecords, os.path.dirname(fastq1) +
                        "/r10" + os.path.basename(fastq1), "fastq")
            SeqIO.write(sampleRecords_2, os.path.dirname(fastq2) +
                        "/r10" + os.path.basename(fastq2), "fastq")
            self.parent.label_state.setText(
                "Done..! \n Check : " + os.path.dirname(fastq1))
        except FileNotFoundError:
            self.parent.label_state.setText("Check your FASTQ File...")

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 600, 300)
        self.setWindowTitle("Seqchop v0.0.1")

        self.pushButton = QPushButton("Select First FASTQ Read File")
        self.pushButton2 = QPushButton("Select Second FASTQ Read File")
        self.runButton = QPushButton("Start")

        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton2.clicked.connect(self.pushButtonClicked2)
        self.runButton.clicked.connect(self.runReadWrite)
        self.label = QLabel("Fastq read 1 : ")
        self.label2 = QLabel("Fastq read 2 : ")

        self.label_state = QLabel("Ready..!")

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.label_state)
        layout.addWidget(self.runButton)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText("Fastq read 1 : " + fname[0])
        self.label_state.setText("Ready..!")

    def pushButtonClicked2(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label2.setText("Fastq read 2 : " + fname[0])
        self.label_state.setText("Ready..!")

    def runReadWrite(self):
        x = ThreadClass(self)
        x.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
