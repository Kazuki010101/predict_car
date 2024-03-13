import os
from flask import (
     Flask, 
     request, 
     render_template)


UPLOAD_FOLDER='/Users/okahashikazuki/Desktop/ORIGINAL/static/'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        img_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
        upload_file.save(img_path)
        result, score = 4, 6
        return render_template('result.html', score=int(score*100),result=result, img_path=img_path)
    else:
        print("ファイルを選択してください")
        return None
if __name__ == "__main__":
    app.run(debug=True)