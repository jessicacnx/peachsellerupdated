from flask import Flask, render_template, request
import smtplib
import numpy
from werkzeug import secure_filename
from PIL import Image as img
app = Flask(__name__)

info = ["test"]
products = ["testp"]
names = ["eda", "shian pei", "jessica"]

# Home Page
@app.route('/')
def index():
  return render_template('index.html')



# staff
@app.route('/staff', methods=["GET","POST"])
def staff():
  if request.form.method == "GET": # get
    return render_template('staff.html') 
  else: # post
    name = request.form.get('pwd')
   
    if name == "eda" or name == "shian pei" or name == "jessica":
      return render_template('info.html', name=name, info=info, products=products)
    else:
      return render_template('index.html')
    

                     
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
