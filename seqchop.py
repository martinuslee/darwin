import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Bio import SeqIO
import random
import os

form_class = uic.loadUiType("/Users/jongheon/Desktop/10reads.ui")[0]

class MyWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 600, 300)
        self.setWindowTitle("Seqchop v0.0.1")

        self.pushButton = QPushButton("File Open")
        self.pushButton2 = QPushButton("File Open")
        self.runButton = QPushButton("Start")
        
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton2.clicked.connect(self.pushButtonClicked2)
        self.runButton.clicked.connect(self.runReadWrite)
        self.label = QLabel()
        self.label2 = QLabel()

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
        self.label.setText(fname[0])
        self.label_state.setText("Ready..!")
        
    def pushButtonClicked2(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label2.setText(fname[0])
        self.label_state.setText("Ready..!")  

    def runReadWrite(self):

        self.label_state.setText("File Reading...")
        #File Read
        #print(self.label.text(), self.label2.text())
        fastq1 = self.label.text()
        fastq2 = self.label2.text()
        
        records , records_2= list(SeqIO.parse(fastq1,"fastq")), list(SeqIO.parse(fastq2,"fastq"))
        index = list(range(1,len(records)+1))

        sampleIdx = sorted(random.sample(index, 10))
        
        print(sampleIdx)
        
        sampleRecords, sampleRecords_2 = [], []
        print(os.path.dirname(fastq1) + "r10" + os.path.basename(fastq1))

        for i in sampleIdx:
            sampleRecords.append(records[i])
            sampleRecords_2.append(records_2[i])
        # File Write
        
        self.label_state.setText("File Writting...")
        SeqIO.write(sampleRecords, os.path.dirname(fastq1) + "/r10" + os.path.basename(fastq1), "fastq")
        SeqIO.write(sampleRecords_2, os.path.dirname(fastq2) + "/r10" + os.path.basename(fastq2), "fastq")
        self.label_state.setText("Done..! Path : " + os.path.dirname(fastq1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()