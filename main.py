from flask import Flask, render_template, request
import smtplib
import numpy
from werkzeug import secure_filename
from PIL import Image as img
app = Flask(__name__)
app.config['products']

info = []
products = []
names = [eda, shian pei, jessica]

# Home Page
@app.route('/index')
def index():
  return render_template('/index.html')

# Upload Product Form
@app.route('/sellerproduct', methods=["GET","POST"])
def sellerproduct():
  if request.method == 'GET': # GET
    return render_template("/sellerproduct.html")

  else: # POST
    # record html variables into python variables
    sp_bname = request.form.get('sp_bname')
    sp_pw = request.form.get('sp_pw')
    sp_dec = request.form.get('p_declare')
    
    # check database
    for i in range(len(info):
      if sp_bname == info[i][7]:
        if sp_pw ==info[i][9]:
          x = True
          break
        else:
          return
      elif i == len(info):
        x = False
        break
      else:
        return
              
    if sp_dec == "Disagree":
      x = False

    # check if valid
    if x == True:
      # record html variables into python variables
      pname = request.form.get('pname')
      pprice = request.form.get('pprice')
      plink = request.form.get('plink')
      pimage = request.files['pimage']
      numpimage = asarray(pimage)

      # a Python object (dict)
      p_newdict = {
        "pname": pname,
        "pprice": pprice,
        "plink": plink,
        "pimage": pimage,
      }
                   
      # https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays
      products.append(p_newdict)

      #valid
      return render_template("/productcompleted.html")

    else:
      #invalid
      return render_template("/productrejected.html")

                   
                   
# Seller Registration Form
@app.route('/sellerregister', methods=["GET","POST"])
def sellerregister():
  if request.method == 'GET': # GET
    return render_template("/sellerregister.html")

  else: # POST
    # record html variables into python variables
    name = request.form.get('name')
    contactnum = request.form.get('contactnum')
    contactemail = request.form.get('contactemail')

    bname = request.form.get('bname')
    bpw = request.form.get('bpw')
    b_dec = request.form.get('s_declare')

    if b_dec == "Disagree":
      # invalid
      return render_template("/registerfailed.html")

    else:
      # dict
      s_newdict = {
        "name": name,
        "contactnum": contactnum,
        "contactemail": contactemail,
        "bname": bname,
        "bpw": bpw,
      }

      # update database
      products.append(s_newdict)
      #valid
      return render_template("/registeroutput.html")
    return

@app.route('/staff')
def staff():
  if request.method == "GET":
    return render_template('/staff.html') 
  else:
    pwd = request.form.get('pwd')
    for i in range(len(names)):
      if pwd = names[i]:
        return render_template('/staffinfo.html', pwd=pwd, products=products, info=info)
      else:
        continue
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
