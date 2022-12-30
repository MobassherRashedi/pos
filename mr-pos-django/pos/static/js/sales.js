$(document).ready(function(){
  $('#id_sales-customer').change(function() {
  let pk =  $(this).find(":selected").val()
  if (!pk) {
    $('#id_sales-phone').val('')
    $('#id_sales-address').val('') // write return for exception handle
  } 
  request_url = 'http://127.0.0.1:8000/settings/customer/details/' + pk + '/';
  $.ajax({ 
    url: request_url,
    headers: {"ajax-call": "true"},// this need to allow in server side configuration as in violets cors policy
    success: function(data){
    myObj = JSON.parse(data);
    var my_address = myObj[0].fields.address;
    var my_phone = myObj[0].fields.phone_1;
    $('#id_sales-phone').val(my_phone)
    $('#id_sales-address').val(my_address)
    },
    errors: function(e) {
    alert(e);
  }
  }) 
})
});

$(document).ready(function(){
  $('#id_sales-product').change(function() {
  let pk =  $(this).find(":selected").val()
  request_url = 'http://127.0.0.1:8000/products/details/' + pk + '/';
  $.ajax({ 
    url: request_url,
    headers: {"ajax-call": "true"},// this need to allow in server side configuration as in violets cors policy
    success: function(data){
    myObj = JSON.parse(data);
    var sales_rate = myObj[0].fields.sales_rate;
    var alert_qty_as_stock = myObj[0].fields.alert_qty;
    $('#id_sales-sales_rate').val(sales_rate)
    $('#id_sales-stock').val(alert_qty_as_stock)
    },
    errors: function(e) {
    alert(e);
  }
  })
})
});

$(document).ready(function(){
  $('#id_sales-barcode').on("keypress", function(e) {
    if (e.keyCode == 13) {
        let barcode =  $(this).val()
        $(this).val(barcode)
        request_url = 'http://127.0.0.1:8000/products/details/' + barcode + '/';
        $.ajax({ 
          url: request_url,
          headers: {"ajax-call": "true"},// Access-Control-Allow-Headers: YOUR_HEADER_NAME >> this need to allow in server side configuration as in violets cors policy
          success: function(data){
                    myObj = JSON.parse(data);
                    var product_pk = myObj[0].pk
                    var product_text = myObj[0].fields.name
                    var $select = $('#id_sales-product');
                    $select.val(product_pk).find("option[value=" + product_pk +"]").attr('selected', true); 
                    setTimeout(function(){ $select.change()}, 100);
                  },
          errors: function(e) {
                  alert(e);
                }
        })
        return false; // prevent the button click from happening
      }
  })
});
// --------------- Add Product --------------- //

$(document).ready(function(){
  var table = $('#example').DataTable({
    paging: false,
    ordering: false,
    info: false,
    searching: false,
    // columns: [
    //   { data: 'id' },
    //   { data: 'product__name' },
    //   { data: 'product__catagory__name' },
    //   { data: 'quantity' },
    //   { data: 'product__sales_rate' },
    //   { data: 'total_amount' },
    //   { data: 'Edit' },
    //   { data: 'Delete' }
    // ]
});

  var val = $("#id_sales-stock").val()
  $("#div_id_sales-qty").attr(
    "max", val)

  $('#id_sales-add_product_to_cart').click(function(e) {
  request_url = 'http://127.0.0.1:8000/sales/cart/create/ajax/';
  let id_sales_product_val = $('#id_sales-product').find(":selected").val()
  let id_sales_customer_val = $('#id_sales-customer').find(":selected").val()
  let id_sales_qty_val = $('#id_sales-qty').val()
  let id_sales_stock = $('#id_sales-stock').val()
  let id_sales_sales_rate_val = $('#id_sales-sales_rate').val()
  let total_val =(parseInt(id_sales_qty_val) * parseFloat(id_sales_sales_rate_val).toFixed(2)).toString()
  if (parseInt(id_sales_qty_val)<=parseInt(id_sales_stock)){
    $.ajax({
      type:'POST',
      url: request_url,
      data:{
        customer_id:id_sales_customer_val,
        product_id:id_sales_product_val,
        quantity:id_sales_qty_val,
        total:total_val,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
      success: function(response){
        if (response.sucessfull=='true') {
              // table.clear();
              // table.rows.add(response.SaleCarts).draw();
              window.location.href = response.redirect;
        }
        else {
         alert("something wrong....!")
        }
      },
      errors: function(e) {
      alert(e);
    }
    })
  }
 else{
  if (id_sales_qty_val && id_sales_stock) {
    
    alert("Product qty can't be bigger then stock!!!")
  }
  else{
     //pass
  }
 }
})
});

$(document).ready(function(){
$(".add_customer_btn").click(function (e) {
  e.preventDefault();
  $.ajax({
    url: 'http://127.0.0.1:8000/settings/customer/create/ajax/',
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#modal-book").modal("show");
    },
    success: function (data) {
      $("#modal-book .modal-content").html(data.html_form);
    }
  });
})
});


$(document).ready(function(){
$("#modal-book").on("submit", ".js-customer-create-form", function () {
  var form = $(this);
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid) {
        $('#id_sales-customer').append(new Option(data.customer_name, data.customer_id));
        $('#id_sales-customer').val(data.customer_id).change();
        $("#modal-book").modal("hide");  // <-- Close the modal
      }
      else {
        $("#modal-book .modal-content").html(data.html_form);
      }
    }
  });
  return false;
});
});


  $(function () {
    /* Functions */
  
    var loadForm = function (e) {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
        }
      });
    };
  

    var saveForm = function (e) {
      e.preventDefault();
      var form = $(this);
      var x = form.serialize();
      console.log(x);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid = 'true') {
            $("#example tbody").html(data.html_list);
            $("#modal-book").modal("hide");
          }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
    // Update cart
    $("#example").on("click", ".js-update-salescart-single", loadForm);
    $("#modal-book").on("submit", ".js-salescart-update-form", saveForm)

    // Delete cart
    $("#example").on("click", ".js-delete-salescart-single", loadForm);
    $("#modal-book").on("submit", ".js_delete_from_cart_form", saveForm)
  });