$(document).ready(function() {
    $('#list-ip-subnet-table').DataTable();
    $('[data-toggle="modal"]').click(function() {
        var id = $(this).attr('id');
        var href = "/ipplan/delete-ip-subnet/" + id
        $('#delete-ip-subnet-from').attr('action', href)
      });
});
