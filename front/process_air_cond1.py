from flask import jsonify

def process_air_cond1(form_air_cond):
    form_air_cond_errors = {}

    air_cond_H2O = form_air_cond.air_cond_H2O.validate(form_air_cond)
    air_cond_selector = form_air_cond.air_cond_selector.validate(form_air_cond)
    air_cond_p1 = form_air_cond.air_cond_p1.validate(form_air_cond)
    air_cond_t1 = form_air_cond.air_cond_t1.validate(form_air_cond)

    if air_cond_H2O == False:
        form_air_cond_errors.update({str(form_air_cond.air_cond_H2O.name) : form_air_cond.air_cond_H2O.errors[-1] })
    if air_cond_selector == False:
        form_air_cond_errors.update({str(form_air_cond.air_cond_selector.name) : form_air_cond.air_cond_selector.errors[-1] })    
    if air_cond_p1 == False:
        form_air_cond_errors.update({str(form_air_cond.air_cond_p1.name) : form_air_cond.air_cond_p1.errors[-1] })
    if air_cond_t1 == False:
        form_air_cond_errors.update({str(form_air_cond.air_cond_t1.name) : form_air_cond.air_cond_t1.errors[-1] })

    
    if air_cond_H2O == False or air_cond_selector == False or air_cond_p1 == False or air_cond_t1 == False:
        return  [False,jsonify( {'flag':1, 'errors':form_air_cond_errors})]
  
    if air_cond_H2O == True and air_cond_selector == True and air_cond_p1 == True and air_cond_t1 == True:
        air_cond_val1 = form_air_cond.air_cond_val1.validate(form_air_cond)
         
        if air_cond_val1 == False:
            form_air_cond_errors.update({str(form_air_cond.air_cond_val1.name) : form_air_cond.air_cond_val1.errors[-1] })
            return  [False,jsonify( {'flag':1, 'errors':form_air_cond_errors})]
        else: return [True]

