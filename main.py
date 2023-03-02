import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        f = request.files.get('file')
        if f.filename:
            name = 'user_image'
            i = 1
            while os.path.exists(os.path.join('static', 'img', name + '.png')):
                name += str(i)
                i += 1
            f.save(os.path.join('static', 'img', name + '.png'))
    slides = os.listdir(os.path.join('static', 'img'))
    return render_template('index.html', slides=slides)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
