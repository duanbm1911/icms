$(document).ready(function() {
    $('#list-pending-task-table').DataTable({
      'pageLength': 50
    });
    $('#list-process-task-table').DataTable({
      'pageLength': 50
    });
    $('#list-success-task-table').DataTable({
      'pageLength': 50
    });
    $('#list-failed-task-table').DataTable({
      'pageLength': 50
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/cm/checkpoint/delete-task/" + id
        $('#delete-task-from').attr('action', href)
      });
});
