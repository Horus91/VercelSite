from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    # the files should be in a directory called templates
    return render_template('/website/home.html')


@app.route('/about/')
def about():
    return render_template('/website/about.html')


if __name__ == '__main__':
    app.run(debug=True)
