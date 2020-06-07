
 let fg_vector_Descr = document.getElementById('fg_vector_Descr');
 let fg_selector = document.getElementById('fg_selector');

 fg_selector.onchange = function(){
     userschoice = fg_selector.selectedIndex
     if(userschoice == 0){
     fg_vector_Descr.innerHTML = 'Fuel Gas Composition';}
     
     else if (userschoice == 1){
     fg_vector_Descr.innerHTML = 'Fuel Gas Composition[mass%]';}
     
     else if (userschoice == 2){
     fg_vector_Descr.innerHTML = 'Fuel Gas Composition[mole%]';}
    }
