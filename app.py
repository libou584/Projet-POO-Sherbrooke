from flask import Flask, render_template, request
from urllib.parse import quote as url_quote

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
