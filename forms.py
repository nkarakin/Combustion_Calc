from flask_wtf import FlaskForm
#---wtf-fields
from wtforms import SelectField, SubmitField, HiddenField, TextField
#---my fields
from my_fields import MyFloatField
#---wtf-validators
from wtforms.validators import InputRequired, NumberRange, Optional
#---my validators
from my_validators import Val_acc_Sel, Pass
from my_validators import SelField
from my_validators import FloatInpReq, NumberRangeExcl
from my_validators import regex_vec, sum_isNOT_x, compsX_is_zero, compsX_isNOT_zero, sum_compsX_isNot_zero
from my_validators import huair_rel_humid, huair_mass_pct, huair_mass_load, huair_mole_pct, huair_mole_load
from my_validators import test
#---Block
from back import Block
length = len(Block().get_block())

class Form_comb(FlaskForm):
    #---------------------fuel gas vector
    
    fg_vector = TextField(validators = [InputRequired('Error: Input req'),regex_vec(length = length), sum_isNOT_x(req_sum=100)])  
    
    #---------------------fuel gas selector
    
    choices_fg = [('op1','----------'),\
    ('op2','Fuel Gas Composition[mass%]'), ('op3','Fuel Gas Composition[mole%]'),]
    fg_selector = SelectField(choices=choices_fg, validators = [SelField(sel_name='fg_selector', notvalid=('op1',))])
    
    #---------------------fuel gas conditions
    
    fg_p1 = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(), NumberRangeExcl(min=0)])
    fg_t1 = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(), NumberRangeExcl(min=-273.15)])
    
    #---------------------oxidation gas vector
    
    tuple = Block().indexs('CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane')
    val_oxgas_vector = [InputRequired(message='Error: Input req.'),regex_vec(length = length), \
        sum_isNOT_x(req_sum=100), compsX_is_zero(Block().index('Oxygen')), sum_compsX_isNot_zero(*tuple)]
    oxgas_vector = TextField(validators = val_oxgas_vector)

    #---------------------oxidation gas selector
    
    choices_oxgas = [('op1','----------'),('op2','Oxidation Gas[mass%]'),('op3','Oxidation Gas[mole%]')]
    oxgas_selector = SelectField(choices = choices_oxgas, \
        validators = [SelField(sel_name = 'oxgas_selector', notvalid = ('op1',))])
    
    #---------------------oxidation gas conditions
    oxgas_p1 = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(),NumberRangeExcl(min=0)])
    oxgas_t1 = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(), NumberRangeExcl(min=-273.15)])

    #---------------------calculation fgFlowOrHeat

    calc_fgFlowOrHeat = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(),NumberRangeExcl(min=0)])
    
    #---------------------calculation fgFlowOrHeat - selector

    choices_calc1 = [('op1','----------'),\
    ('op2','Fuel Gas Flow[kg/s]'),('op3','Fuel Gas Flow[mole/s]'),\
    ('op4','Fired Heat[W]')]
    calc_selector1 = SelectField(choices=choices_calc1, validators = [SelField( sel_name = 'calc_selector1', notvalid=('op1',))])
    
    #---------------------calculation oxgasFlowOrLamb

    dict_sel_oxgasFlowOrLamb = {
        'sel_name': 'calc_selector2',
        'cant_val': ('op1',),
        'val': ('op2','op3','op4') } 
    dict_val_oxgasFlowOrLamb = {    
        'op2': [NumberRangeExcl(min=0)], 
        'op3': [NumberRangeExcl(min=0)],
        'op4': [NumberRange(min=0,max=1)]} 
    calc_oxgasFlowOrLamb = MyFloatField(validators=[InputRequired('Error: Input req'), FloatInpReq(), \
        Val_acc_Sel(dict_sel=dict_sel_oxgasFlowOrLamb, dict_val = dict_val_oxgasFlowOrLamb)])
    
    #----------------------calculation oxgasFlowOrLamb - selector

    choices_calc2 = [('op1','----------'),\
    ('op2','Oxidation Gas Flow[kg/s]'),('op3','Oxidation Gas Flow[mole/s]'),\
    ('op4','Lambda - Oxygen Excess[-]')]
    calc_selector2 = SelectField(choices=choices_calc2,validators =[SelField( sel_name = 'calc_selector2', notvalid=('op1',))])

    #-----------------------submit button for combustion form
    
    comb_submit = SubmitField('Calc. Combustion')

class Form_air_cond(FlaskForm):

    #-----------------------air condensation H2O-content

    dict_sel_H2O = {
        'sel_name': 'air_cond_selector',
        'cant_val': ('op1',),
        'val': ('op2','op3','op4', 'op5', 'op6') } 
    dict_val_H2O = {    
        'op2': [InputRequired('Error: Input req'),FloatInpReq(), NumberRange(min=0,max=1)], 
        'op3': [InputRequired('Error: Input req'),FloatInpReq(), NumberRange(min=0,max=100)],
        'op4': [InputRequired('Error: Input req'),FloatInpReq(), NumberRange(min=0,max=1)],
        'op5': [InputRequired('Error: Input req'),FloatInpReq(), NumberRange(min=0,max=100)],
        'op6': [InputRequired('Error: Input req'),FloatInpReq(), NumberRange(min=0,max=1)]} 
    air_cond_H2O = MyFloatField(validators=[Val_acc_Sel(dict_sel=dict_sel_H2O, dict_val=dict_val_H2O)])

    #----------------------air condensation selector

    choices_air_cond = [('op1','----------'), \
    ('op2','Rel.Humidity[0,1]'), \
    ('op3','Mass Percent[0,100] '), \
    ('op4','Humid.Ratio(Mass)[0,1]'), \
    ('op5','Mole Percent[0,100]'), \
    ('op6','Humid.Ratio(Mole)[0,1]')]    
    air_cond_selector = SelectField(choices=choices_air_cond,\
        validators=[SelField(sel_name='air_cond_selector', notvalid = ('op1',))])
  
    #----------------------air condensation conditions

    air_cond_p1 = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(),NumberRangeExcl(min=0)])
    air_cond_t1 = MyFloatField(validators=[InputRequired('Error: Input req'),FloatInpReq(), NumberRangeExcl(min=-273.15)])
  
    #----------------------air condensation submit button

    air_cond_submit = SubmitField('Calc.Humid Air')
      
    #----------------------air condensation hidden field for validation

    dict_sel_val1 = {
        'sel_name': 'air_cond_selector',
        'cant_val': ('op1',),
        'val': ('op2','op3','op4','op5','op6') } 
    dict_val_val1 = {    
        'op2': [huair_rel_humid('air_cond_H2O','air_cond_p1','air_cond_t1')], 
        'op3': [huair_mass_pct('air_cond_H2O','air_cond_p1','air_cond_t1')],
        'op4': [huair_mass_load('air_cond_H2O','air_cond_p1','air_cond_t1')],
        'op5': [huair_mole_pct('air_cond_H2O','air_cond_p1','air_cond_t1')],
        'op6': [huair_mole_load('air_cond_H2O','air_cond_p1','air_cond_t1')]}  
    air_cond_val1 = HiddenField(validators=[Val_acc_Sel(dict_sel=dict_sel_val1, dict_val=dict_val_val1)])


class Form_test(FlaskForm):
    test_field1 = MyFloatField(validators=[NumberRange(min=0),test()])
    test_field2 = MyFloatField(validators=[NumberRange(min=0)])
    test_submit = SubmitField('submit test')

    '''
        dict_sel_vec = {
        'sel_name': 'air_selector',
        'cant_val': ('op1',),
        'val': ('op2','op3','op4','op5') } 
    
    dict_val_vec = {    
        'op2': [compsX_isNOT_zero(Block().index('Water'))], 
        'op3': [compsX_isNOT_zero(Block().index('Water'))],
        'op4': [Pass()],
        'op5': [Pass()]}    
        
    tuple = Block().indexs('CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane')
    val_air_vector = [InputRequired(message='Error: Input req.'),regex_vec(length = length), \
                    sum_isNOT_x(req_sum=100), compsX_is_zero(Block().index('Oxygen')), \
                    Val_acc_Sel(dict_sel=dict_sel_vec, dict_val=dict_val_vec), \
                    sum_compsX_isNot_zero(*tuple)]
    air_vector = TextField(validators = val_air_vector)

    #---------------------phi
    dict_sel_phi = {
        'sel_name': 'air_selector',
        'cant_val': ('op1',),
        'val': ('op2','op3','op4','op5') } 
    dict_val_phi = {    
        'op2': [InputRequired('Error: Input req'),FloatInpReq(),NumberRange(min=0,max=1)], 
        'op3': [InputRequired('Error: Input req'),FloatInpReq(),NumberRange(min=0,max=1)],
        'op4': [Optional()],
        'op5': [Optional()]} 
    air_phi = MyFloatField(validators = [Val_acc_Sel(dict_sel=dict_sel_phi, dict_val =dict_val_phi)]) 
    '''

 
 