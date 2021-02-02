from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route('/user/<username>')
def hello_world(username):
    return render_template('/test.html', username=username)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
