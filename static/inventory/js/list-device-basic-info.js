$(document).ready(function() {
    $('#list-device-basic-info-table').DataTable();
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device/device-basic-info/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
