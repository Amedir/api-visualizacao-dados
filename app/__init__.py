import os
from flask import Flask, render_template, redirect, request, url_for, session
from yourapp.main import *

app = Flask(__name__, template_folder='templates')

app.register_blueprint(views)

if __name__ == '__main__':
  app.run(debug=True)