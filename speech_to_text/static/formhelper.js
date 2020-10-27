$(document).ready(function(){

    let input = $("#inpputaudio");
    let button = $("#submitButton");
    let form = new FormData();
    input.on('input',evt => {
       let submitButton = $("#submitButton");
       let title = $("#title");
           submitButton.css("background-color", "#335672");
           submitButton.css("color" ,"white");
           submitButton.prop('disabled', false);
           console.log(input[0].files[0].name);
           title.html(input[0].files[0].name); 
           form.append('document', input[0].files[0]);
    });
    button.click(function(){
      //console.log(file);
      $("#loading").show();
       $.ajax({
             url: "/ajax-posting/",
              type: "POST",
              data : form,
              contentType : false,
              processData: false,
              cache: false,
              success: function(info) {
            console.log(info);
            $("#loading").hide();
                $('#output').html(info.msg);

            }
          });
    });
  });