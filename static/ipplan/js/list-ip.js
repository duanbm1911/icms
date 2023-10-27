$(document).ready(function() {
    $('#list-ip-table').DataTable();
    $('[data-toggle="modal"]').click(function() {
        var id = $(this).attr('id');
        var href = "/ipplan/delete-ip/" + id
        $('#delete-ip-from').attr('action', href)
      });
});
