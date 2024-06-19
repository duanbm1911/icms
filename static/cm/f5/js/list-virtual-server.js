$(document).ready(function() {
  $('#list-virtual-server-table').DataTable({
    'pageLength': 50
  });
  $(document.body).on('click', '[data-toggle="modal"]', function() {
      var id = $(this).attr('id');
      var href = "/cm/f5/objects/delete-virtual-server/" + id
      $('#delete-virtual-server-form').attr('action', href)
    });
});
