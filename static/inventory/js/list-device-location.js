$(document).ready(function() {
    $('#list-device-location-table').DataTable({
      'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device-location/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
