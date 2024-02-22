$(document).ready(function() {
    $('#list-device-type-table').DataTable({
      'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device-type/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
