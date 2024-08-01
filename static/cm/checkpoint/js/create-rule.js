$(document).ready(function () {
  var initData = [[]];
  var placeholder = document.getElementById('dataTable');
  var hot = new Handsontable(placeholder, {
    data: initData,
    rowHeaders: true,
    colWidths: 'auto',
    rowHeights: 100,
    // height: 600,
    // stretchH: 'all',
    height: 'auto',
    colHeaders: ['Policy', 'Name', 'Source', 'Destination', 'Protocol', 'section','Schedule'],
    manualColumnResize: true,
    columns: [
      {
        type: 'autocomplete',
        strict: true,
        allowInvalid: false,
        source(query, process) {
          $.ajax({
            type: "GET",
            url: '/api/cm/checkpoint/get-list-policy',
            success: function (response) {
              process(response.data)
            }
          })
        }
      }, {}, {}, {}, {},
      {
        type: 'autocomplete',
        source(query, process) {
          let row = this.row
          let policy = hot.getDataAtCell(row, 0)
          console.log(policy)
          $.ajax({
            type: "GET",
            url: '/api/cm/checkpoint/get-rule-section?policy=' + policy,
            success: function (response) {
              process(response.datalist)
            }
          })
        },
        strict: true,
        allowInvalid: false
      },
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
    var col = hot.countRows();
    hot.alter('insert_row_below', col, 1)
  })
  document.querySelector('#submit').addEventListener('click', function () {
    $('#submit').prop('disabled', true)
    let datalist = hot.getData()
    $.ajax({
      type: "POST",
      url: '/api/cm/checkpoint/create-rule',
      dataType: "json",
      data: {
        'datalist': datalist
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
})
