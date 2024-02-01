$(document).ready(function() {
    $('#list-device-basic-info-table').DataTable({
      dom: 'Bfrtip',
      buttons: [
          'copy', 'csv', 'excel', 'pdf', 'print'
      ]
  });
    $('[data-toggle="modal"]').click(function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device/device-basic-info/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
