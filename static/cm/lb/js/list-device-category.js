$(document).ready(function() {
  $('#list-device-category-table').DataTable({
    'pageLength': 50
  });
  $(document.body).on('click', '[data-toggle="modal"]', function() {
      var id = $(this).attr('id');
      var href = "/cm/lb/objects/delete-device-category/" + id
      $('#delete-device-category-form').attr('action', href)
    });
});
