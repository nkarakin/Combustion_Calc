$(document).ready(function () {
  $("#comb_submit").click(function () {
    var data = {
      comb: {
        fg_vector: $("#fg_vector").val(),
        fg_p1: $("#fg_p1").val(),
        fg_t1: $("#fg_t1").val(),
        fg_selector: $("#fg_selector").val(),
      
        oxgas_vector: $("#oxgas_vector").val(),  
        oxgas_p1: $("#oxgas_p1").val(),
        oxgas_t1: $("#oxgas_t1").val(),
        oxgas_selector: $("#oxgas_selector").val(),
      
        calc_fgFlowOrHeat: $("#calc_fgFlowOrHeat").val(),
        calc_selector1:$("#calc_selector1").val(),
        calc_oxgasFlowOrLamb:$("#calc_oxgasFlowOrLamb").val(),
        calc_selector2:$("#calc_selector2").val(),
      }
    };
    $.ajax({
      type: "POST",
      url: "/process_comb",
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      data: JSON.stringify(data),
    }).done(function (data) {
      if (data.flag == 1) {
        //console.log(data)
        // remove table from previous calculation
        var output = document.getElementById("form_comb_res");
        output.innerHTML = "";
      ///////////////////////////////////////////////////////////------------------------------Fuelgas
      if (data.errors.fg_vector) {
        var output = document.getElementById("fg_vector_Alert");
        output.innerHTML = data.errors.fg_vector;
      } else {
        var output = document.getElementById("fg_vector_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.fg_p1) {
        var output = document.getElementById("fg_p1_Alert");
        output.innerHTML = data.errors.fg_p1;
      } else {
        var output = document.getElementById("fg_p1_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.fg_t1) {
        var output = document.getElementById("fg_t1_Alert");
        output.innerHTML = data.errors.fg_t1;
      } else {
        var output = document.getElementById("fg_t1_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.fg_selector) {
        var output = document.getElementById("fg_selector_Alert");
        output.innerHTML = data.errors.fg_selector;
      } else {
        var output = document.getElementById("fg_selector_Alert");
        output.innerHTML = "OK";
      }
      ///////////////////////////////////////////////////////////------------------------------Oxgas
      if (data.errors.oxgas_vector) {
        var output = document.getElementById("oxgas_vector_Alert");
        output.innerHTML = data.errors.oxgas_vector;
      } else {
        var output = document.getElementById("oxgas_vector_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.oxgas_p1) {
        var output = document.getElementById("oxgas_p1_Alert");
        output.innerHTML = data.errors.oxgas_p1;
      } else {
        var output = document.getElementById("oxgas_p1_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.oxgas_t1) {
        var output = document.getElementById("oxgas_t1_Alert");
        output.innerHTML = data.errors.oxgas_t1;
      } else {
        var output = document.getElementById("oxgas_t1_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.oxgas_selector) {
        var output = document.getElementById("oxgas_selector_Alert");
        output.innerHTML = data.errors.oxgas_selector;
      } else {
        var output = document.getElementById("oxgas_selector_Alert");
        output.innerHTML = "OK";
      }
      ///////////////////////////////////////////////////////////------------------------------Calc
      if (data.errors.calc_fgFlowOrHeat) {
        var output = document.getElementById("calc_fgFlowOrHeat_Alert");
        output.innerHTML = data.errors.calc_fgFlowOrHeat;
      } else {
        var output = document.getElementById("calc_fgFlowOrHeat_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.calc_selector1) {
        var output = document.getElementById("calc_selector1_Alert");
        output.innerHTML = data.errors.calc_selector1;
      } else {
        var output = document.getElementById("calc_selector1_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.calc_oxgasFlowOrLamb) {
        var output = document.getElementById("calc_oxgasFlowOrLamb_Alert");
        output.innerHTML = data.errors.calc_oxgasFlowOrLamb;
      } else {
        var output = document.getElementById("calc_oxgasFlowOrLamb_Alert");
        output.innerHTML = "OK";
      }
      if (data.errors.calc_selector2) {
        var output = document.getElementById("calc_selector2_Alert");
        output.innerHTML = data.errors.calc_selector2;
      } else {
        var output = document.getElementById("calc_selector2_Alert");
        output.innerHTML = "OK";
      }

      }else if (data.flag ==2) {
        // Set Error Alerts to "OK"
        var output1 = document.getElementById("fg_vector_Alert");
        output1.innerHTML = "Ok";
        var output2 = document.getElementById("fg_p1_Alert");
        output2.innerHTML = "Ok";
        var output3 = document.getElementById("fg_t1_Alert");
        output3.innerHTML = "Ok";
        var output4 = document.getElementById("fg_selector_Alert");
        output4.innerHTML = "Ok";

        var output5 = document.getElementById("oxgas_vector_Alert");
        output5.innerHTML = "Ok";
        var output6 = document.getElementById("oxgas_p1_Alert");
        output6.innerHTML = "Ok";
        var output7 = document.getElementById("oxgas_t1_Alert");
        output7.innerHTML = "Ok";
        var output8 = document.getElementById("oxgas_selector_Alert");
        output8.innerHTML = "Ok";

        var output9 = document.getElementById("calc_fgFlowOrHeat_Alert");
        output9.innerHTML = "Ok";
        var output10 = document.getElementById("calc_selector1_Alert");
        output10.innerHTML = "Ok";
        var output11 = document.getElementById("calc_oxgasFlowOrLamb_Alert");
        output11.innerHTML = "Ok";
        var output12 = document.getElementById("calc_selector2_Alert");
        output12.innerHTML = "Ok";
      $('#form_comb_res').html(data.result);
      }
    });
    event.preventDefault();
  });
});
