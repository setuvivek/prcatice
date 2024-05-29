$(document).ready(function() {
    //set initial state.

    $('.product_id').change(function() {
        debugger
       var value = $(this).val()
       var data = JSON.stringify({data:value})
       console.log(data)
       $.ajax({
                type: "POST",
                dataType: 'json',
                url: '/productgetqty',
                contentType: "application/json; charset=utf-8",
                data:data,
                success: function(result){
                    $("#result").html(result);
                  },
                  error: function(xhr,status,result){
                    $("#result").html(result);
                  }
          });
    });
});
