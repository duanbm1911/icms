$(document).ready(function() {
    $('#list-policy-table').DataTable({
      'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/cm/checkpoint/objects/delete-policy/" + id
        $('#delete-policy-from').attr('action', href)
      });
});
