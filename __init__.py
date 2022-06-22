from flask import Flask, render_template, redirect, request, url_for, session
from yourapp.main import *
import os

app = Flask(__name__, template_folder='templates')

app.register_blueprint(views)

if __name__ == '__main__':
  # port = int(os.environ.get('PORT', 5000))
  # app.run(host='0.0.0.0', port=port)
  app.run(debug=True)