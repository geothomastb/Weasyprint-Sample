from flask import Flask, render_template
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/')
def hello_html():
    return render_template('hello.html')


@app.route('/pdf',methods=['GET'])
def hello_pdf():
    html = render_template('hello.html')
    return render_pdf(HTML(string=html))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)