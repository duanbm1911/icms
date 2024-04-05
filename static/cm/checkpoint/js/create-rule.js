$(document).ready(function () {
  var datalist01 = [[]];
  $.ajax({
    type: "GET",
    url: '/api/cm/checkpoint/get-list-policy',
    success: function (response) {
      var datalist02 = response.data
      var placeholder = document.getElementById('dataTable');
      var myDataGrid = new Handsontable(placeholder, {
        data: datalist01,
        rowHeaders: true,
        colWidths: 200,
        rowHeights: 100,
        colHeaders: ['Policy', 'Name', 'Source', 'Destination', 'Protocol', 'Schedule'],
        manualColumnResize: true,
        columns: [
          {
            type: 'autocomplete',
            source: datalist02,
            strict: true,
            allowInvalid: false
          }, {}, {}, {}, {},
          {
            type: 'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: true,
            datePickerConfig: {
              firstDay: 0,
              showWeekNumber: true,
              numberOfMonths: 1
            },
            allowInvalid: false
          }
        ],
        autoWrapRow: true,
        autoWrapCol: true
      });
      document.querySelector('#add').addEventListener('click', function () {
        var col = myDataGrid.countRows();
        myDataGrid.alter('insert_row_below', col, 1)
      })
      document.querySelector('#submit').addEventListener('click', function () {
        $('#submit').prop('disabled', true)
        let datalist03 = myDataGrid.getData()
        $.ajax({
          type: "POST",
          url: '/api/cm/checkpoint/create-rule',
          dataType: "json",
          data: {
            'datalist': datalist03
          },
          success: function (response) {
            if (response.status == 'success') {
              Swal.fire({
                text: response.message,
                icon: "success"
              }).then(function() {
                window.location = '/cm/checkpoint/list-rule';
              })
            }
            else{
              Swal.fire({
                text: response.message,
                icon: "error"
              }).then(function () {
                $('#submit').prop('disabled', false)
              })
            }
          },
          error: function (response) {
            Swal.fire({
              text: response.responseJSON.message,
              icon: "error"
            }).then(function () {
              $('#submit').text('Submit');
              $('#submit').prop('disabled', false)
            })
          }
        })
      })
    }
  })
})

