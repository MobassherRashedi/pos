$(document).ready(function() {
    var table = $('#my-table').DataTable({
      ajax: {
        url: '/my-data-url',
        dataSrc: ''
      },
      columns: [
        { data: 'name' },
        { data: 'grade' }
      ]
    });
  
    $('#my-form').on('submit', function(e) {
      e.preventDefault();
      var formData = $(this).serialize();
      $.ajax({
        type: 'POST',
        url: '/my-form-url',
        data: formData,
        success: function(response) {
          table.ajax.reload();
        }
      });
    });
  });
  