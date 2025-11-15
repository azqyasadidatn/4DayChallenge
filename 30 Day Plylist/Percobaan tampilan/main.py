from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/template')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
