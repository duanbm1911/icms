$(document).ready(function() {
    $('#list-ip-table').DataTable();
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var ip_id = $(this).attr('ip-id');
        var subnet_id = $(this).attr('subnet-id')
        var href = "/ipplan/list-ip/" + subnet_id + "/delete-ip/" + ip_id
        $('#delete-ip-from').attr('action', href)
      });
});
