



 
$(document).ready(function() {
    var table = $('#stock_table').DataTable( {
        dom: 'Bfrtip',
        "pageLength": 3,
        "ordering": true,
        "orderClasses": true,
        columns: [
            { data: 'name' },
            { data: 'product_code' },
            { data: 'catagory', 
            render: function (data, type, row) {
                switch(data) {
                case 1:
                    return 'demo 1';
                    break; 
                case 2:
                    return 'cloth';
                    break;                
                case 3:
                    return 'electronics';
                    break;
                default:
                    return '-';
                }
            }},
            { data: 'sub_catagory',render: function (data, type, row) {
                switch(data) {
                case 1:
                    return 'demo 1';
                    break; 
                case 2:
                    return 'demo 1';
                    break;                
                case 3:
                    return 'cloth';
                    break;
                case 4:
                    return 'electronics';
                    break;                    
                case 5:
                    return 'electronics';
                    break;                   
                default:
                    return '-';
                }
            }},
            { data: 'product_unit' ,render: function (data, type, row) {
                switch(data) {
                case 1:
                    return 'demo unit 1';
                    break; 
                case 2:
                    return 'demo unit 2';
                    break;                
                case 3:
                    return 'demo unit 3';
                    break;                   
                default:
                    return '-';
                }
            }},
            { data: 'alert_qty' },
            { data: 'purchase_rate' },
            { data: 'sales_rate' },

        ],
        buttons: [
            {
                extend: 'copyHtml5',
                exportOptions: {
                    columns: [ 0,1,2,3,4,5 ]
                }
            },
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [ 0,1,2,3,4,5 ]
  
                }
            },
            {
                extend: 'csvHtml5',
                exportOptions: {
                    columns: [ 0,1,2,3,4,5 ]
  
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                  columns: [ 0,1,2,3,4,5 ]
  
                }
            },
            {
              extend: 'print',
              exportOptions: {
                columns: [ 0,1,2,3,4,5 ]
  
              }
          },
            'colvis'
        ]
    } );

    $('#btn_submit_stock').click(function(e) {
        e.preventDefault()
        var selectedOption = $('#Type').val();
        $.ajax({
          url: 'http://127.0.0.1:8000/stocks/product/search/',
          type: 'GET',
          cache: false,
          data: { option: selectedOption},
          success: function(response) {
              table.clear();
              table.rows.add(response.products).draw();
            //   console.log(response.products);
          //   $("#stock_table tbody").html(response.html_data);
          }
        });
      });

  } );



