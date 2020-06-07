import requests
from flask import Flask, render_template, flash, request, json, jsonify
from forms import Form_comb, Form_air_cond, Form_test
import werkzeug.datastructures as wd
from CoolProp.CoolProp import HAPropsSI
from back.stream import Stream
from back.block import Block
from back.HAStreamCreator import HAStreamCreator
from front import process_air_cond1, process_air_cond2
from front import process_comb1, process_comb2
import pandas as pd
import numpy as np


app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY'] = 'secret'

@app.route("/index",methods = ['GET','POST'])
def index():
    form_comb = Form_comb()
    form_air_cond = Form_air_cond()
    form_test = Form_test()
    return render_template('index.html', form_comb = form_comb, form_air_cond = form_air_cond, form_test = form_test)

@app.route('/process_comb', methods = ['POST'])
def process_comb():
    form_comb = Form_comb(wd.ImmutableMultiDict(request.json['comb']))
    res_val = process_comb1(form_comb)
    if res_val[0] == False:  return res_val[1]
    elif res_val[0] == True: return process_comb2(form_comb)
  
@app.route('/process_air_cond', methods = ['POST'])
def process_air_cond():
    form_air_cond =  Form_air_cond(wd.ImmutableMultiDict(request.json['air_cond']))
    res_val = process_air_cond1(form_air_cond)
    if res_val[0] == False:  return res_val[1]
    elif res_val[0] == True: return process_air_cond2(form_air_cond) 

@app.route('/process_test', methods = ['POST'])
def process_test():
    form_test = Form_test(wd.ImmutableMultiDict(request.json['test']))
    form_test_errors = {}
    
    test_field1 = form_test.test_field1.validate(form_test)
    test_field2 = form_test.test_field2.validate(form_test)

    if test_field1 == False:
        form_test_errors.update({str(form_test.test_field1.name) : form_test.test_field1.errors[-1]})
    if test_field2 == False:
        form_test_errors.update({str(form_test.test_field2.name) : form_test.test_field2.errors[-1]})

    if test_field1 == True and test_field2 == True:
        print(form_test.test_field1.validators[1].__call__(form_test,form_test.test_field1))
        
        result = form_test.test_field1.data + form_test.test_field2.data
        flash(str(result))
        list1 = [1,2,3,4]
        list2 = [1,2,3,4]
        col = ['col1','col2','col3','col4']
        ind = ['ind1','ind2']
        df = pd.DataFrame(np.array([list1,list2]),columns=col,index=ind)

        return jsonify({'flag': 2, 'json_errors': {}, 'html_res': render_template('form_test_res.html',data=df.to_html())})

    return jsonify({'flag': 1, 'js_errors': form_test_errors, 'html_res': {} })
     

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
