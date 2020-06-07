from flask import jsonify

def process_comb1(form_comb):

    true_false_vec = ['true_false']*12
    
    form_comb_errors = {}
    true_false_vec[0] =     form_comb.fg_vector.validate(form_comb) 
    true_false_vec[1] =     form_comb.fg_p1.validate(form_comb)
    true_false_vec[2] =     form_comb.fg_t1.validate(form_comb)
    true_false_vec[3] =     form_comb.fg_selector.validate(form_comb)
    

    true_false_vec[4] =     form_comb.oxgas_vector.validate(form_comb)
    true_false_vec[5] =     form_comb.oxgas_p1.validate(form_comb)
    true_false_vec[6] =     form_comb.oxgas_t1.validate(form_comb)
    true_false_vec[7] =     form_comb.oxgas_selector.validate(form_comb)

    true_false_vec[8]  =    form_comb.calc_fgFlowOrHeat.validate(form_comb)
    true_false_vec[9]  =    form_comb.calc_selector1.validate(form_comb)
    true_false_vec[10] =    form_comb.calc_oxgasFlowOrLamb.validate(form_comb)
    true_false_vec[11] =    form_comb.calc_selector2.validate(form_comb)


    if true_false_vec[0] == False:
        form_comb_errors.update({str(form_comb.fg_vector.name) : form_comb.fg_vector.errors[-1]})  
    if true_false_vec[1] == False:
        form_comb_errors.update({str(form_comb.fg_p1.name) : form_comb.fg_p1.errors[-1]})
    if true_false_vec[2] == False:
        form_comb_errors.update({str(form_comb.fg_t1.name) : form_comb.fg_t1.errors[-1]})
    if true_false_vec[3] == False:
        form_comb_errors.update({str(form_comb.fg_selector.name) : form_comb.fg_selector.errors[-1]})

    if true_false_vec[4] == False:
        form_comb_errors.update({str(form_comb.oxgas_vector.name) : form_comb.oxgas_vector.errors[-1]}) 
    if true_false_vec[5] == False:
        form_comb_errors.update({str(form_comb.oxgas_p1.name) : form_comb.oxgas_p1.errors[-1]}) 
    if true_false_vec[6] == False:
        form_comb_errors.update({str(form_comb.oxgas_t1.name) : form_comb.oxgas_t1.errors[-1]}) 
    if true_false_vec[7] == False:
        form_comb_errors.update({str(form_comb.oxgas_selector.name) : form_comb.oxgas_selector.errors[-1]})
    

    if true_false_vec[8] == False:
        form_comb_errors.update({str(form_comb.calc_fgFlowOrHeat.name) : form_comb.calc_fgFlowOrHeat.errors[-1]}) 
    if true_false_vec[9] == False:
        form_comb_errors.update({str(form_comb.calc_selector1.name) : form_comb.calc_selector1.errors[-1]}) 
    if true_false_vec[10] == False:
        form_comb_errors.update({str(form_comb.calc_oxgasFlowOrLamb.name) : form_comb.calc_oxgasFlowOrLamb.errors[-1]}) 
    if true_false_vec[11] == False:
        form_comb_errors.update({str(form_comb.calc_selector2.name) : form_comb.calc_selector2.errors[-1]}) 
    
    if False in true_false_vec: return [False, jsonify({'flag':1,'errors':form_comb_errors})]
    else: return [True]   

