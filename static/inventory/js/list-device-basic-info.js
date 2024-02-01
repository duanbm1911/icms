$(document).ready(function() {
    $('#list-device-basic-info-table').DataTable();
    $('[data-toggle="modal"]').click(function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device/device-basic-info/delete/" + id
        console.log(href)
        $('#delete-device-from').attr('action', href)
      });
});
