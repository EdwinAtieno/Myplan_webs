from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def api():
    return {"userid":1,"title":"flask application", "completed": False}


if __name__ == '__main__':
    app.run(debug=True)
