

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
      e.preventDefault()
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            // $("#bank_table").html(data.table);
            $("#modal-book").modal("hide");
            window.location.href = data.redirect;
          }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  

    var deleteForm = function (e) {
      e.preventDefault()
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            // $("#bank_table").html(data.table);
            $("#modal-book").modal("hide");
            window.location.href = data.redirect;
          }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
    /* Binding */
  
    // Update bank
    $(".bank_table").on("click", ".edit_btn", loadForm);
    $("#modal-book").on("submit", ".js-bank-update-form", saveForm);


    // delete bank
    $(".bank_table").on("click", ".js_delete_btn", loadForm);
    $("#modal-book").on("submit", ".js_delete_form", deleteForm);
    // $(document).on("submit", ".js-bank-update-form", saveForm);
  });

//   $(document).ready(function () {
//     $('#bankTable').DataTable({
//         buttons: [
//             'copy', 'csv', 'excel', 'pdf', 'print'
//         ],
//         lengthMenu: [
//             [2,10, 25, 50, -1],
//             [2,10, 25, 50, 'All'],
//         ],
//     });
// });


$(document).ready(function() {
  $('#bankTable').DataTable( {
      dom: 'Bfrtip',
      "pageLength": 2,
      "ordering": true,
      "orderClasses": true,
      buttons: [
          {
              extend: 'copyHtml5',
              exportOptions: {
                  columns: [ 0,1,2,3,4 ]
              }
          },
          {
              extend: 'excelHtml5',
              exportOptions: {
                  columns: [ 0,1,2,3,4 ]

              }
          },
          {
              extend: 'csvHtml5',
              exportOptions: {
                  columns: [ 0,1,2,3,4 ]

              }
          },
          {
              extend: 'pdfHtml5',
              exportOptions: {
                columns: [ 0,1,2,3,4 ]

              }
          },
          {
            extend: 'print',
            exportOptions: {
              columns: [ 0,1,2,3,4 ]

            }
        },


          'colvis'
      ]
  } );
} );
