# Jake Zaia
# SoftDev pd 9
# Work 04
# 2017-09-20

from flask import Flask, render_template
from utils import occupation as occ

data = occ.takeFile()

app = Flask(__name__)


@app.route('/')
def main():
    return 'Welcome to main!\n <a href="http://127.0.0.1:5000/occupations"> Go to occupations </a>'

@app.route('/occupations')
def occupations():
    return render_template("occupations.html", data = data, rand = occ.getRandWeighted(data))

    
if __name__ == '__main__':
    app.debug = True
    app.run()
