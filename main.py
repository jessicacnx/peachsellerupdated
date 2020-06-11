from flask import Flask, render_template, request
import smtplib
import numpy
from werkzeug import secure_filename
from PIL import Image as img
app = Flask(__name__)



info = []
products = []
names = ["eda", "shian pei", "jessica"]



# Home Page
@app.route('/index')
def index():
  return render_template('/index.html')



# staff
@app.route('/staff', methods=["GET","POST"])
def staff():
  if request.method == "GET": # get
    return render_template('/staff.html') 
  else: # post
    pwd = request.form.get('pwd')
    for i in range(len(names):
      if pwd = names[i]:
        return render_template('/staffinfo.html', pwd=pwd, products=products, info=info)
    return render_template('/staff.html')

                     
# ** Future Plan: **
# prevent spam (repeated email, spam bots, valid documents)
# create safe database
# create email for company

''' 
Note for Coder: 

1. make sure database records
2. make sure database checks
4. make everyth work
5. make it look nice
stupid img banner

'''

app.run(host='0.0.0.0', port=8080)
