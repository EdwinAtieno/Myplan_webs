from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/members')
def hello_world():
    return {"members":["member1", "member2", "member3"]}


if __name__ == '__main__':
    app.run(debug=True)
