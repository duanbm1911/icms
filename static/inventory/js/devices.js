$(document).ready(function() {
    $('#list-device-table').DataTable();
    $('[data-toggle="modal"]').click(function() {
        var id = $(this).attr('id');
        var href = "/inventory/delete-device/" + id
        $('#delete-device-from').attr('action', href)
      });
});