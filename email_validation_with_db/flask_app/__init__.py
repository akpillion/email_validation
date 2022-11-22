from flask import Flask
from flask import flash

app = Flask(__name__)

app.secret_key = "Secrets Secrets"