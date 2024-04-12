$(document).ready(function() {
    $('#list-device-rack-layout-table').DataTable({
        'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device/device-rack-layout/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
