let oxgas_selector = document.getElementById('oxgas_selector');
let oxgas_vector_Descr = document.getElementById('oxgas_vector_Descr');
oxgas_selector.onchange = function() {
    userchoice = oxgas_selector.selectedIndex   
    if(userchoice == 0) {
        oxgas_vector_Descr.innerHTML = 'Oxidation Gas Composition';}  
    else if (userchoice == 1 ){
        oxgas_vector_Descr.innerHTML = 'Oxidation Gas Composition[mass%]';} 
    else if (userchoice == 2) {
        oxgas_vector_Descr.innerHTML = 'Oxidation Gas Composition[mole%]';} 
}



