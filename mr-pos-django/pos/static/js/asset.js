// function double created because of js scope prevent to call this function from ducomented ready fn  ****** need to fix it*****
function get_data() {
    $.ajax({
      type: "GET",
      datatype : 'json',
      url: 'http://127.0.0.1:8000/asset/get/data/', 
      success: function (response) {
        $('#asset-table').DataTable().clear();
        $('#asset-table').DataTable().destroy();
          $('#asset-table').DataTable({
              data:response,
              "columns": [
                  { "data": "id"},
                  { "data": "date"},
                  { "data": "name"},
                  { "data": "amount"},
                  { "data": "note"},
              ],
          });
  
      },
      error: function (response) {
          alert(response["error"]);
      }
  })
};


$(document).ready(function(e){
    $('#asset-form-submit').on("click",function(e) {
        var form = $(".js-asset-creat-form");
    $.ajax({
          url: 'http://127.0.0.1:8000/asset/post/data/',
        data: form.serialize(),
          type: 'POST',
          dataType: 'json',
          async: false,
          success: function (data) {
                // $("#").ajax.reload( null, false );
                get_data();
                // $('#asset-table').DataTable().ajax.reload();
          }
        });
    e.preventDefault();
    })
  });
  

  $(document).ready(function() {
    $.ajax({
      type: "GET",
      datatype : 'json',
      url: 'http://127.0.0.1:8000/asset/get/data/', 
      success: function (response) {
          $('#asset-table').DataTable({
              data:response,
              "columns": [
                  { "data": "id"},
                  { "data": "date"},
                  { "data": "name"},
                  { "data": "amount"},
                  { "data": "note"},
              ],
          });
  
      },
      error: function (response) {
          alert(response["error"]);
      }
  })
  });
  

//   //// ************ Editor table start **************////

//   var editor; // use a global for the submit and return data rendering in the examples
 
// $(document).ready(function() {
//     editor = new $.fn.dataTable.Editor( {
//         "ajax": 'http://127.0.0.1:8000/asset/get/data/',
//         "table": "#example",
//         "fields": [ {
//                 "label": "First name:",
//                 "name": "first_name"
//             }, {
//                 "label": "Last name:",
//                 "name": "last_name"
//             }, {
//                 "label": "Position:",
//                 "name": "position"
//             }, {
//                 "label": "Office:",
//                 "name": "office"
//             }, {
//                 "label": "Extension:",
//                 "name": "extn"
//             }, {
//                 "label": "Start date:",
//                 "name": "start_date",
//                 "type": "datetime"
//             }, {
//                 "label": "Salary:",
//                 "name": "salary"
//             }
//         ]
//     } );
 
//     // New record
//     $('a.editor-create').on('click', function (e) {
//         e.preventDefault();
 
//         editor.create( {
//             title: 'Create new record',
//             buttons: 'Add'
//         } );
//     } );
 
//     // Edit record
//     $('#example').on('click', 'td.editor-edit', function (e) {
//         e.preventDefault();
 
//         editor.edit( $(this).closest('tr'), {
//             title: 'Edit record',
//             buttons: 'Update'
//         } );
//     } );
 
//     // Delete a record
//     $('#example').on('click', 'td.editor-delete', function (e) {
//         e.preventDefault();
 
//         editor.remove( $(this).closest('tr'), {
//             title: 'Delete record',
//             message: 'Are you sure you wish to remove this record?',
//             buttons: 'Delete'
//         } );
//     } );
 
//     $('#example').DataTable( {
//         ajax: 'http://127.0.0.1:8000/asset/get/data/',
//         columns: [
//             { data: null, render: function ( data, type, row ) {
//                 // Combine the first and last names into a single table field
//                 return data.first_name+' '+data.last_name;
//             } },
//             { data: "position" },
//             { data: "office" },
//             { data: "extn" },
//             { data: "start_date" },
//             { data: "salary", render: $.fn.dataTable.render.number( ',', '.', 0, '$' ) },
//             {
//                 data: null,
//                 className: "dt-center editor-edit",
//                 defaultContent: '<i class="fa fa-pencil"/>',
//                 orderable: false
//             },
//             {
//                 data: null,
//                 className: "dt-center editor-delete",
//                 defaultContent: '<i class="fa fa-trash"/>',
//                 orderable: false
//             }
//         ]
//     } );
// } );
//   //// ************ Editor table end **************////
