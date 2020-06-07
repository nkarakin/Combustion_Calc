
 let calc_fgFlowOrHeat_Descr = document.getElementById('calc_fgFlowOrHeat_Descr'); 
 let calc_selector1 = document.getElementById('calc_selector1');

 calc_selector1.onchange = function(){
    
     userschoice = calc_selector1.selectedIndex
     if(userschoice == 0){
     calc_fgFlowOrHeat_Descr.innerHTML = '----------';}     
     else if (userschoice == 1){
     calc_fgFlowOrHeat_Descr.innerHTML = 'Fuel Gas Flow[kg/s]';}     
     else if (userschoice == 2){
     calc_fgFlowOrHeat_Descr.innerHTML = 'Fuel Gas Flow[mole/s]';} 
     else if (userschoice == 3){
     calc_fgFlowOrHeat_Descr.innerHTML = 'Fired Heat[W]';} }


let calc_oxgasFlowOrLamb_Descr = document.getElementById('calc_oxgasFlowOrLamb_Descr'); 
let calc_selector2 = document.getElementById('calc_selector2');
    
calc_selector2.onchange = function(){
    userschoice = calc_selector2.selectedIndex
    if(userschoice == 0){
    calc_oxgasFlowOrLamb_Descr.innerHTML = '----------';}     
    else if (userschoice == 1){
    calc_oxgasFlowOrLamb_Descr.innerHTML = 'Oxidation Gas Flow[kg/s]';}     
    else if (userschoice == 2){
    calc_oxgasFlowOrLamb_Descr.innerHTML = 'Oxidation Gas Flow[mole/s]';} 
    else if (userschoice == 3){
    calc_oxgasFlowOrLamb_Descr.innerHTML = 'Lambda - Oxygen Excess[-]';} }

