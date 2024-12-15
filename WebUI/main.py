from flask import Flask, request, render_template
import uuid
import subprocess
import os

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_text():
    text = request.form['text']
    print(text)
    uid = str(uuid.uuid4())
    print(uid)
    with open(f'{uid}.txt', 'a') as f:
        f.write(text + '\n')
    result = subprocess.run(f'script -q -c "python ./Elyzer/elyzer.py -f {uid}.txt" /dev/null | aha', 
                            shell=True, capture_output=True, text=True)
    os.remove(f'{uid}.txt')
    return result.stdout.replace('olive', 'orange')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')