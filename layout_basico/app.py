from flask import Flask, render_template, request, redirect,url_for, send_from_directory

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True)