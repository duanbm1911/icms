$(document).ready(function() {
    $('#list-device-basic-info-table thead tr')
    .clone(true)
    .addClass('filters')
    .appendTo('#list-device-basic-info-table thead');
    $('#list-device-basic-info-table').DataTable({
      'pageLength': 50,
      'orderCellsTop': true,
      'fixedHeader': true,
      initComplete: function () {
        var api = this.api();
        api
          .columns()
          .eq(0)
          .each(function (colIdx) {
            var cell = $('.filters th').eq(
                $(api.column(colIdx).header()).index()
            );
            var title = $(cell).text();
            $(cell).html('<input type="text"/>');
            $(
              'input',
              $('.filters th').eq($(api.column(colIdx).header()).index())
            )
            .off('keyup change')
            .on('change', function (e) {
                $(this).attr('title', $(this).val());
                var regexr = '({search})';
                var cursorPosition = this.selectionStart;
                api
                    .column(colIdx)
                    .search(
                        this.value != ''
                            ? regexr.replace('{search}', '(((' + this.value + ')))')
                            : '',
                        this.value != '',
                        this.value == ''
                    )
                    .draw();
            })
            .on('keyup', function (e) {
                e.stopPropagation();
                $(this).trigger('change');
                $(this)
                  .focus()[0]
                  .setSelectionRange(cursorPosition, cursorPosition);
            });
          });
      },
    });
    $(document.body).on('click', '[data-toggle="modal"]', function() {
        var id = $(this).attr('id');
        var href = "/inventory/list-device/device-basic-info/delete/" + id
        $('#delete-device-from').attr('action', href)
      });
});
