$(document).ready(function () {
    $("#test_submit").click(function () {
      var data = {
      test: {
        test_field1: $("#test_field1").val(),
        test_field2: $("#test_field2").val(),
    },
      };
      $.ajax({
        type: "POST",
        url: "/process_test",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify(data),
        
      }).done(function (data){   
        if (data.flag == 1){
          if (data.js_errors.test_field1){
          var output = document.getElementById("test_field1_Alert")
          output.innerHTML = data.js_errors.test_field1
        } else {
          var output = document.getElementById("test_field1_Alert")
          output.innerHTML = "OK"
        }
        if (data.js_errors.test_field2){
          var output = document.getElementById("test_field2_Alert")
          output.innerHTML = data.js_errors.test_field2
        } else {
          var output = document.getElementById("test_field2_Alert")
          output.innerHTML = "OK"
        }

        } else if (data.flag==2) {
          $('#test_result').html(data.html_res);
        }
        
        //else {alert ("it is html")}
         //var output = document.getElementById("test_result")
         //output.innerHTML = data.result
         //$('#test_result').append(data)
       //}).fail(function(data) {
        //  alert("it is html")
          //var output = document.getElementById("test_result")
          //output = data
          //$('#test_result').html(data)
    });
    event.preventDefault();
    });
  });