from flask import render_template, flash, jsonify
from back import rand_gen_vec, formater, Block
import pandas as pd
import numpy as np
def process_comb2(form_comb):
        

        # Table with compositions of streams
        a1flow = rand_gen_vec(12,0,10000); a1flow.append(sum(a1flow)) ; a1flow = [formater(x,8,2) for x in a1flow]
        a2flow = rand_gen_vec(12,0,10000); a2flow.append(sum(a2flow)) ; a2flow = [formater(x,8,2) for x in a2flow]
        a3flow = rand_gen_vec(12,0,10000); a3flow.append(sum(a3flow)) ; a3flow = [formater(x,8,2) for x in a3flow]

        b1flow = rand_gen_vec(12,0,10000); b1flow.append(sum(b1flow)) ; b1flow = [formater(x,8,2) for x in b1flow]
        b2flow = rand_gen_vec(12,0,10000); b2flow.append(sum(b2flow)) ; b2flow = [formater(x,8,2) for x in b2flow]
        b3flow = rand_gen_vec(12,0,10000); b3flow.append(sum(b3flow)) ; b3flow = [formater(x,8,2) for x in b3flow]
        
        columns_A = [('Fuel','kg/s'),('Fuel','mole/s'),('Ox.Gas','kg/s'),('Ox.Gas','mole/s'),('Flue','kg/s'),('Flue','mole/s')]
        mu_columns_A = pd.MultiIndex.from_tuples(columns_A)

        arr_A = np.array([a1flow,a2flow,a3flow,b1flow,b2flow,b3flow]).T
        index_A = Block().get_block()
        index_A.append('sum')
        df_A = pd.DataFrame(arr_A,index = index_A, columns = mu_columns_A)

        # Table with element balance
        c1flow = rand_gen_vec(6,0,10000); c1flow.append(sum(c1flow)) ; c1flow = [formater(x,8,2) for x in c1flow]
        c2flow = rand_gen_vec(6,0,10000); c2flow.append(sum(c2flow)) ; c2flow = [formater(x,8,2) for x in c2flow]
        c3flow = rand_gen_vec(6,0,10000); c3flow.append(sum(c3flow)) ; c3flow = [formater(x,8,2) for x in c3flow]
        c4flow = rand_gen_vec(6,0,10000); c4flow.append(sum(c4flow)) ; c4flow = [formater(x,8,2) for x in c4flow]
        
        columns_B = [('Fuel','mole/s'),('Ox.Gas','mole/s'),('Flue','mole/s'), ('Balance','mole/s')]
        mu_columns_B = pd.MultiIndex.from_tuples(columns_B)

        arr_B = np.array([c1flow,c2flow,c3flow,c4flow]).T
        index_B = Block().get_elem()
        index_B.append('sum')
        df_B = pd.DataFrame(arr_B,index = index_B, columns = mu_columns_B)

        # Table with other Variables
        d1variables = rand_gen_vec(3,0,100) ; d1variables = [formater(x,8,2) for x in d1variables]
        d1_units = ['unit','unit','unit']
        arr_C = np.array([d1_units,d1variables]).T
        df_C = pd.DataFrame(arr_C,index=['var1','var2','var3'])


        a = render_template('form_comb_res.html', data1 = df_A.to_html(), data2 = df_B.to_html(), data3=df_C.to_html(header=False))
        return jsonify( { 'flag': 2,'result': a} )