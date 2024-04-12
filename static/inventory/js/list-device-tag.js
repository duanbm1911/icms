$(document).ready(function() {
    $('#list-device-tag-table').DataTable({
      'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device-tag/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
