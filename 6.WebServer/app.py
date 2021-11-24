from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from Bio import SeqIO
from io import StringIO 

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"*": {"origins": "*"}})
#/api/* 에 해당하는 url 들은 CORS 가 적용되어 어디서든 호출이 가능

#http://163.152.219.180:3838/uploadfile

@app.route("/api/uploadfile", methods=['POST'])
def uploadFile():
    file1 = request.files['read1'] #werkzeug.datastructures.FileStorage
    file2 = request.files['read2']
    # f = request.form
    # print(f)
    print(type(file1))
    print(secure_filename(file1.filename))
    print(secure_filename(file2.filename))
    print(file1.read()) # werkzeug.datastructures.FileStorage . read() => b''
    
    records = list(SeqIO.parse(StringIO(file1),'fastq'))
    print(records)
    return 'ok'

if __name__ == '__main__':
    app.run(host='163.152.219.180', port=3838, debug=True)


