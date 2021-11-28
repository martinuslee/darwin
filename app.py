import os 
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
from Bio import SeqIO
from io import StringIO

app = Flask(__name__, static_folder='3.SAMPLE/', template_folder='6.WebServer/templates')
app.config['CORS_HEADERS'] = 'Content-Type'
# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})
# /api/* 에 해당하는 url 들은 CORS 가 적용되어 어디서든 호출이 가능

# http://163.152.219.180:3838/uploadfile


@app.route('/')
def hello_world():
    return 'DARWIN SERVER RUN PORT 3838'


@app.route("/api/uploadfile", methods=['POST'])
def uploadFile():
    file1 = request.files['read1']  # werkzeug.datastructures.FileStorage
    file2 = request.files['read2']
    species_name = request.form['species']
    thread_opt = request.form['threadOpt']
    
    print('- SPECIES NAME : ' + species_name)
    print('- READ 1 : ' + secure_filename(file1.filename))
    print('- READ 2 : ' + secure_filename(file2.filename))
    #print(file1.read())  # werkzeug.datastructures.FileStorage . read() => b''


    try:
        os.makedirs(f'3.SAMPLE/{species_name}/')
    
    except OSError:
        if not os.path.isdir(f'3.SAMPLE/{species_name}/'):
            raise Exception('error...!')

    file1.save(f'3.SAMPLE/{species_name}/' + secure_filename(file1.filename))
    file2.save(f'3.SAMPLE/{species_name}/' + secure_filename(file2.filename))
    print('-- file saved done..! --')
    print(f'- SAVE DIR : 3.SAMPLE/{species_name}/{secure_filename(file1.filename)}')
    # records = SeqIO.index(f'../3.SAMPLE/{species_name}/{secure_filename(file1.filename)}', 'fastq')
    # data = fileget(f'../3.SAMPLE/{species_name}/{secure_filename(file1.filename)}')
    print(f'python3 darwin.py -t {thread_opt} --name {species_name} --per r10r50')
    result = os.popen(f'time python3 darwin.py -t {thread_opt} --name {species_name} --per r10r50').read()
    print(result)

    result_csv = open(f'3.SAMPLE/{species_name}/result.csv')
    data = result_csv.readlines()
    
    return render_template('result.html', data = data)

def fileget(param):
    f = open(param, 'r')
    records = list(SeqIO.parse(f, 'fastq'))
    return records

@app.route("/api/<filename>", methods=["GET"])
def uploadFileName(filename):
    return 'ok %s'%(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3838, debug=True)


