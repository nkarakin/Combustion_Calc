$(document).ready(function () {
    $("#air_cond_submit").click(function () {
      var data = {
        air_cond: {
          air_cond_H2O: $("#air_cond_H2O").val(),
          air_cond_selector: $("#air_cond_selector").val(),
          air_cond_p1: $("#air_cond_p1").val(),
          air_cond_t1: $("#air_cond_t1").val(),
        },
      };
      $.ajax({
        type: "POST",
        url: "/process_air_cond",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify(data),
      }).done(function (data) {
        if (data.flag == 1){
          //console.log(data)
          // remove table from previous calculation
          var output = document.getElementById("form_air_cond_res");
          output.innerHTML = "";

        if (data.errors.air_cond_H2O) {
          var output = document.getElementById("air_cond_H2O_Alert");
          output.innerHTML = data.errors.air_cond_H2O;
        } else {
          var output = document.getElementById("air_cond_H2O_Alert");
          output.innerHTML = "OK";
        }
        if (data.errors.air_cond_selector) {
          var output = document.getElementById("air_cond_selector_Alert");
          output.innerHTML = data.errors.air_cond_selector;
        } else {
          var output = document.getElementById("air_cond_selector_Alert");
          output.innerHTML = "OK";
        }
        if (data.errors.air_cond_p1) {
          var output = document.getElementById("air_cond_p1_Alert");
          output.innerHTML = data.errors.air_cond_p1;
        } else {
          var output = document.getElementById("air_cond_p1_Alert");
          output.innerHTML = "OK";
        }  
        if (data.errors.air_cond_t1) {
          var output = document.getElementById("air_cond_t1_Alert");
          output.innerHTML = data.errors.air_cond_t1;
        } else {
          var output = document.getElementById("air_cond_t1_Alert");
          output.innerHTML = "OK";
        }  
        // Validation: Can CoolProp process the data?
        if (data.errors.air_cond_val1) {
          var output = document.getElementById("air_cond_val1_Alert");
          output.innerHTML = data.errors.air_cond_val1;
        } else { 
          var output = document.getElementById("air_cond_val1_Alert");
          output.innerHTML = "H2O-Condensation-check";
        }

        } else if (data.flag == 2) {
        // Set Error Alerts to "Ok" 
        var output1 = document.getElementById("air_cond_H2O_Alert");
        output1.innerHTML = "Ok";
        var output2 = document.getElementById("air_cond_selector_Alert");
        output2.innerHTML = "Ok";
        var output3 = document.getElementById("air_cond_p1_Alert");
        output3.innerHTML = "Ok";
        var output4 = document.getElementById("air_cond_t1_Alert");
        output4.innerHTML = "Ok";
        var output5 = document.getElementById("air_cond_val1_Alert");
        output5.innerHTML = "H2O-Condensation-check";


        // Showing result of calculation
        $('#form_air_cond_res').html(data.result);
        }
    });
      event.preventDefault();
    });
  });
  