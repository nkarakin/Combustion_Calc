
 let air_cond_H2O_Descr = document.getElementById('air_cond_H2O_Descr'); 
 let air_cond_selector = document.getElementById('air_cond_selector');

 air_cond_selector.onchange = function(){
    
     userschoice = air_cond_selector.selectedIndex
     if(userschoice == 0){
     air_cond_H2O_Descr.innerHTML = 'H2O-Content in Humid Air';}     
     else if (userschoice == 1){
     air_cond_H2O_Descr.innerHTML = 'Relative Humidity';}     
     else if (userschoice == 2){
     air_cond_H2O_Descr.innerHTML = 'Mass H2O [%]';} 
     else if (userschoice == 3){
     air_cond_H2O_Descr.innerHTML = 'Mass H2O / Mass Dry Air';} 
     else if (userschoice == 4){
     air_cond_H2O_Descr.innerHTML = 'Mole H2O [%]';} 
     else if (userschoice == 5){
     air_cond_H2O_Descr.innerHTML = 'Mole H2O / Mole Dry Air';} 
    }