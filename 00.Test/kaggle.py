import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ex.html')