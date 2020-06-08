from flask import Flask, render_template, request
import smtplib
import json
from PIL import Image as img
app = Flask(__name__)

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
    sp_nric = request.form.get('sp_nric')
    sp_pw = request.form.get('sp_pw')
    sp_dec = request.form.get('p_declare')
    
    # check database
    fread = open('/info.txt', 'r')
    
    for line in fread: 
      count += 1
      if sp_nric == line[7]:
        x = True
        break
      if not line: 
        x = False
        break
      else: 
        continue
    
    if sp_dec == "Disagree":
      x = False
    
    fread.close()

    # check if valid
    if x == True:
      # record html variables into python variables
      pname = request.form.get('pname')
      pprice = request.form.get('pprice')
      plink = request.form.get('plink')
      pimage = request.form.get('pimage')

      # write variables into json
      # a Python object (dict)
      p_newdict = {
        "pname": pname,
        "pprice": pprice,
        "plink": plink,
        "pimage": pimage,
      }

      # convert into JSON
      p_newjson = json.dumps(p_newdict)

      # print JSON string into INFO.txt
      fout = open("/info.txt", 'a')
      fout.write(p_newjson)
      fout.close()
      fin = open("/info.txt", 'r')
      fin.close()

      #valid
      return render_template("/productcompleted.html")

    else x == False:
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
    nric = request.form.get('nric')

    bname = request.form.get('bname')
    bpw = request.form.get('bpw')
    b_dec = request.form.get('s_declare')

    if b_dec == "Disagree":
      # invalid
      return render_template("/registerfailed.html")

    else:
      # write variables into json
      # a Python object (dict)
      s_newdict = {
        "name": name,
        "contactnum": contactnum,
        "contactemail": contactemail,
        "nric": nric,
      
        "bname": bname,
        "bpw": bpw,
      }

      # convert into JSON
      s_newjson = json.dumps(s_newdict)

      # update database
      fout = open("info.txt", "a")
      fout.write(s_newjson + "\n")
      fout.close()
      return render_template("/registeroutput.html")
    return


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
