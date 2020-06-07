from wtforms.validators import StopValidation
import re, json
from CoolProp.CoolProp import HAPropsSI

# ------------------------------------Special Validators

class Val_acc_Sel(object):
    '''
    Validates depending on selector choices 
    
    Parameters in dict_sel:
    key = 'sel_name' : value = string with the name of the selector the validation depends on. 
    key = 'cant_val' : value = tuple with options which make the validation impossible
    key = 'val'      : value = tuple with options which lead to validation

    Parameters in dict_val:
    key = some key matching one of the items in tuple with key 'val' in dict_sel : value = list with validators
    and so on... Number of keys = number of items in tuple with key 'val' in dict_sel

    '''
    def __init__(self,dict_sel, dict_val):
        self.dict_sel = dict_sel
        self.dict_val = dict_val


    def __call__(self, form, field):
        sel_name = self.dict_sel.get('sel_name')
        cant_val = self.dict_sel.get('cant_val')
        val = self.dict_sel.get('val')

        if form[sel_name].data in cant_val:
            raise StopValidation('Error: No Option selected')
        
        elif form[sel_name].data in val:
            validators = self.dict_val.get(form[sel_name].data)
            for validator in validators:
                validator.__call__(form,field)

class Pass(object):
    def __init__(self):
        pass
    def __call__(self,form,field):
        pass
# ------------------------------------Number Fields

class NumberRangeExcl(object):
    """
    Validates that a number is of a minimum and/or maximum value, exclusive.
    Flask-Built-in validator (NumberRange) does it inclusive!
    
    This validator (just as NumberRange) works with any comparable number type,
    such as floats and decimals or just integers.

    :param min:
        The minimum required value of the number. If not provided, minimum
        value will not be checked.
    :param max:
        The maximum value of the number. If not provided, maximum value
        will not be checked."""

    def __init__(self,min=None,max=None):
        self.min = min
        self.max = max

    def __call__(self,form,field):
        if self.min is not None and self.max is None:
            if field.data == self.min or field.data < self.min:
                raise StopValidation(message='Error: Value < %.2f or Value = %.2f' % (self.min, self.min) )
        elif self.min is None and self.max is not None:
            if field.data == self.max or field.data > self.max:
                raise StopValidation(message='Error: Value > %.2f or Value = %.2f' % (self.max, self.max) )
        elif self.min is not None and self.max is not None:
            if field.data == self.min or field.data == self.max or field.data < self.min or field.data > self.max:
                raise StopValidation(message='Error: Value is outside the range from %.2f to %.2f (exclusive).' % (self.min,self.max))

class FloatInpReq(object):
    '''
    I use it in combination with the MyFloatField. MyFloatField works
    as Built-in FloatField:
    int, float, decimal are converted to float, everything else is converted to None.
    
    There is only one difference:
    FloatField raises a Validation Error if it sees something which is not 
    float or int and it writes the error into field's error-list.
    MyFloatField raises no Validation Error and doesn't write anything into
    field's error list.
    '''

    def __init__(self):
        pass
    def __call__(self,form, field):
        if type(field.data) != float:
            raise StopValidation('Error: Value is not float or integer') 

# ------------------------------------Selector Fields
class SelField(object):
    def __init__(self, sel_name, notvalid):
        self.sel_name = sel_name
        self.notvalid = notvalid
    
    def __call__(self,form,field):
        if form[self.sel_name].data in self.notvalid:
            raise StopValidation('Error: Selection is not valid')

# ------------------------------------Vector Fields
def regex_vec(length):
    '''pattern: list with numbers of length 'length' '''
    def _regex_vec(form,field):
        length2 = str(length-1)
        my_regex = r'^(?:(?=\s*0)(\s*0\.[0-9]*\s*[,]|\s*0\s*[,])|\s*[1-9]+[0-9]*\.?[0-9]*\s*[,]){'+length2+r'}(?:(?=\s*0)(\s*0\.[0-9]*\s*$|\s*0\s*$)|\s*[1-9]+[0-9]*\.?[0-9]*\s*)$' 
        pattern = re.compile(my_regex)
        if len( [m for m in re.finditer(pattern, field.data) ] ) == 1: pass
        else: raise  StopValidation('Error: Not required pattern (%d comma separated positive floats or integers)' % length)
    return _regex_vec

def sum_isNOT_x(req_sum):
    '''req_sum = required sum of all numbers in a list'''
    def _sum_isNOT_x(form,field):
        if req_sum != None:
            dummy1 = field.data.replace(" ","")
            if sum(json.loads('['+dummy1+']')) != req_sum:
                raise StopValidation(message='Error: Sum of all components is not %d' % req_sum)
        else:
            pass
    return _sum_isNOT_x

def sum_compsX_isNot_zero(*args):
    '''args = tuple with indexes (start = 1). sum of the according values in the list has to be zero
    !!! args becomes tuple here, and not in the call !!!'''
    def _sum_compsX_isNot_zero(form, field):
        dummy1 = field.data.replace(" ","")
        vec = json.loads('['+dummy1+']')
        dummy2 = []
        for a in args: 
            dummy2.append(vec[a-1])       
        if sum(dummy2) != 0:
            dummy3 = ''
            for i in range(len(args)):
                string = str('{},'.format(args[i]))
                dummy3+=string
            dummy4 = dummy3.rstrip(',')
            raise StopValidation('Error: The sum of components '+dummy4+' is not 0')     
    return _sum_compsX_isNot_zero

def compsX_is_zero(*args):
    '''args = tuple with indexes (start = 1).!!! args becomes tuple here, and not in the call !!!'''
    def _compsX_is_zero(form, field):
        dummy1 = field.data.replace(" ","")
        vec = json.loads('['+dummy1+']')
        for a in args:
            if vec[a-1] == 0:
                raise StopValidation('Error: Component %d is 0' %a )
    return _compsX_is_zero

def compsX_isNOT_zero(*args):
    '''args = tuple with indexes (start = 1).!!! args becomes tuple here, and not in the call !!!'''
    def _compsX_isNOT_zero(form, field):
        dummy1 = field.data.replace(" ","")
        vec = json.loads('['+dummy1+']')
        for a in args:
            if vec[a-1] != 0:
                raise StopValidation('Error: Component %d is not 0' %a )
    return _compsX_isNOT_zero

# ------------------------------------val1 (H2O condensation)
def huair_rel_humid(air_cond_H2O,air_cond_p1,air_cond_t1):
    def _humid_air_rel_humid(form,field):
        phi = form[air_cond_H2O].data
        p = form[air_cond_p1].data
        t = form[air_cond_t1].data
        try: HAPropsSI('W','T',t,'P',p,'R',phi)
        except Exception as e: raise StopValidation(str(e))
    return _humid_air_rel_humid

def huair_mass_pct(air_cond_H2O,air_cond_p1,air_cond_t1):
    def _huair_mass_pct(form,field):
        mass_pct = form[air_cond_H2O].data
        p = form[air_cond_p1].data
        t = form[air_cond_t1].data
        try: HAPropsSI('R','T',t,'P',p,'W', mass_pct / (100-mass_pct))
        except Exception as e: raise StopValidation(str(e))
    return _huair_mass_pct

def huair_mass_load(air_cond_H2O,air_cond_p1,air_cond_t1):
    def _huair_mass_load(form,field):
        mass_load = form[air_cond_H2O].data
        p = form[air_cond_p1].data
        t = form[air_cond_t1].data
        try: HAPropsSI('R','T',t,'P',p,'W', mass_load)
        except Exception as e: raise StopValidation(str(e))
    return _huair_mass_load

def huair_mole_pct(air_cond_H2O,air_cond_p1,air_cond_t1):
    def _huair_mole_pct(form,field):
        mole_pct = form[air_cond_H2O].data
        p = form[air_cond_p1].data
        t = form[air_cond_t1].data
        try: HAPropsSI('R','T',t,'P',p,'Y', mole_pct / 100)
        except Exception as e: raise StopValidation(str(e))
    return _huair_mole_pct

def huair_mole_load(air_cond_H2O,air_cond_p1,air_cond_t1):
    def _huair_mole_load(form,field):
        mole_load = form[air_cond_H2O].data
        p = form[air_cond_p1].data
        t = form[air_cond_t1].data
        try: HAPropsSI('R','T',t,'P',p,'Y', mole_load / (1 + mole_load))
        except Exception as e: raise StopValidation(str(e))
    return _huair_mole_load


def test():
    def _test(form,field):
        return 'yah'
    return _test





'''
def cond_H2O(air_phi,air_p1,air_t1):
    def _test(form,field):
        phi = form[air_phi].data
        p = form[air_p1].data
        t = form[air_t1].data
        try:
            H2O_load = HAPropsSI('W','T',t,'P',p,'R',phi)
        except Exception as e:
            raise StopValidation(str(e))
    return _test


def cond_H2O2(vec,air_p1,air_t1):
    def _test(form,field):
        
        #dummy1 = form[vec_oxgas].data.replace(" ","")
        #vec = json.loads('['+dummy1+']')
        
        p = form[air_p1].data
        t = form[air_t1].data
        try:
            H2O_phi = HAPropsSI('R','T',t,'P',p,'W',vec[1]/100)
            return H2O_phi
        except Exception as e:
            raise StopValidation(str(e))
    return _test

def air_H2O_cond():
    def _air_H2O_cond(form,field):
        raise StopValidation('TEST TEST')
    return _air_H2O_cond
    '''




