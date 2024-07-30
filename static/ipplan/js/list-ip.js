$(document).ready(function() {
    $('#list-ip-table').DataTable({
      'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var ip_id = $(this).attr('ip-id');
        var subnet_id = $(this).attr('subnet-id')
        var href = "/ipplan/list-ip/" + subnet_id + "/delete-ip/" + ip_id
        $('#delete-ip-from').attr('action', href)
      });
    $('#btn-discovery').on('click', function() {
      $('#btn-discovery').prop('disabled', true)
      subnet = $('#id-subnet').data('subnet')
      $.ajax({
        type: "POST",
        url: '/api/ipplan/scan-ip',
        data: {
          'subnet': subnet
        },
        dataType: 'json',
        success: function(response){
          if (response.status == 'success') {
            Swal.fire({
              text: response.message,
              icon: "success"
            }).then(function () {
              $('#btn-discovery').prop('disabled', false)
            })
          }
          else{
            Swal.fire({
              text: response.error,
              icon: "error"
            }).then(function () {
              $('#btn-discovery').prop('disabled', false)
            })
          }
        }
      })
    })
});
