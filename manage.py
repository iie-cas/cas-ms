#coding: utf8
from app import app, create_db
from flask_script import Manager


manage = Manager(app)


if __name__ == '__main__':
    create_db()
    app.run()
