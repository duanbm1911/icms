$(document).ready(function() {
  $('#list-bypass-url-table').DataTable({
    'pageLength': 50
  });
  $(document.body).on('click', '[data-toggle="modal"]', function() {
      var id = $(this).attr('id');
      var href = "/cm/proxy/objects/delete-bypass-url/" + id
      $('#delete-bypass-url-form').attr('action', href)
    });
});
