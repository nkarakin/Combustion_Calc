$(document).ready(function() {

    $("body").on("click", "#btn", function() {
  
      $("#myModal").modal("show");
  
      $(".contVert_test").addClass("after_modal_appended");
  
      //appending modal background inside the blue div
      $('.modal-backdrop').appendTo(".contVert_test");
  
      //remove the padding right and modal-open class from the body tag which bootstrap adds when a modal is shown
  
      $('body').removeClass("modal-open")
      $('body').css("padding-right", "");
    });
  
  });