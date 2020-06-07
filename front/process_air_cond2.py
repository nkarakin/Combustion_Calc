from back import Stream
from back import Block
from back import HAStreamCreator
from back import formater

from CoolProp.CoolProp import HAPropsSI
import pandas as pd
import numpy as np
from flask import jsonify
from flask import render_template


def process_air_cond2(form_air_cond):
    dry_air = Stream()
    dry_air.set_compos(mass_pct_list =Block().get_drai_mass_pct_list())

    cont_H2O = form_air_cond.air_cond_H2O.data
    press    = form_air_cond.air_cond_p1.data
    temp     = form_air_cond.air_cond_t1.data  
           
    dict = \
    {'op2': HAStreamCreator().from_rel_humid ,
    'op3': HAStreamCreator().from_mass_pct  ,
    'op4': HAStreamCreator().from_mass_load ,
    'op5': HAStreamCreator().from_mole_pct  ,
    'op6': HAStreamCreator().from_mole_load }
    fun = dict[form_air_cond.air_cond_selector.data]
           
    humid_air = fun(dry_air,cont_H2O,press,temp)
    huair_mass_pct_list = humid_air.get_compos('mass_pct_list')
    huair_mole_pct_list = humid_air.get_compos('mole_pct_list')

    index_H2O = Block().get_block().index('Water') 

    #original value from the form
    dict2 = \
    { form_air_cond.air_cond_selector.data : form_air_cond.air_cond_H2O.data}

    #calculated value: fall-back-value, if original value is None
    dict3 = \
    {'op2'  : HAPropsSI,
     'op3'  : huair_mass_pct_list[index_H2O],
     'op4'  : huair_mass_pct_list[index_H2O] / (100-huair_mass_pct_list[index_H2O]),
     'op5'  : huair_mole_pct_list[index_H2O],
     'op6'  : huair_mole_pct_list[index_H2O] / (100-huair_mole_pct_list[index_H2O])}

    form_air_cond_result = \
    {'op2': dict2.get('op2') or round(dict3['op2']('R','T',temp,'P',press,'W', huair_mass_pct_list[index_H2O] / (100-huair_mass_pct_list[index_H2O])),5),
     'op3' : dict2.get('op3') or round(dict3['op3'],5),
     'op4' : dict2.get('op4') or round(dict3['op4'],5),
     'op5' : dict2.get('op5') or round(dict3['op5'],5),
     'op6' : dict2.get('op6') or round(dict3['op6'],2)}
            
    #create data frame for composition vectors
    col_names = ['mass%','mole%']
    col1_name = col_names[0].replace('%','') + '_pct_list'
    col2_name = col_names[1].replace('%','') + '_pct_list'
    ind = Block().get_block()
    ind.append('sum')
        
    col1 = humid_air.get_compos(col1_name)
    col2 = humid_air.get_compos(col2_name)
    col1.append(sum(col1))
    col2.append(sum(col2))

    df1 = pd.DataFrame(np.array([[formater(x,8,2) for x in col1], [formater(x,8,2) for x in col2]]).T, index=ind,columns=col_names)
            
    #create data frame for H2O-Content vector
    conv = {'op2':'Part.P H2O/Sat.P H2O @ T',\
                'op3':'kg H2O/kg humid air',    'op4':'kg H2O/kg dry air',\
                'op5':'mole H2O/mole humid air','op6':'mole H2O/mole dry air'}
    optns = []
    names = []
    dim = []
    values = []
    for num,element in enumerate(form_air_cond.air_cond_selector.choices[1:],start = 0):  
        names.append(element[1])
        optns.append(element[0])
        dim.append(conv.get(optns[num]))
        values.append(form_air_cond_result.get(optns[num]))   
    values = [formater(x,8,2) for x in values]     

    df2 = pd.DataFrame(np.array([dim,values]).T,index=names)
    
   
    return jsonify( { 'flag': 2,'result': render_template('form_air_cond_res.html',data1=df1.to_html(),data2=df2.to_html(header=False))} )