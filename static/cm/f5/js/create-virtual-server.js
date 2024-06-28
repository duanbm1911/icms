$(document).ready(function () {
  var datalist01 = [[]];
  $.ajax({
    type: "GET",
    url: '/api/cm/f5/get-list-device',
    success: function (response) {
      var datalist02 = response.data
      var placeholder = document.getElementById('dataTable');
      var myDataGrid = new Handsontable(placeholder, {
        data: datalist01,
        rowHeaders: true,
        colWidths: 180,
        rowHeights: 100,
        colHeaders: ['F5 device', 'Service name', 'Virtual server IP', 'Pool member', 'Client SSL profile', 'Server SSL profile', 'F5 template'],
        manualColumnResize: true,
        columns: [
          {
            type: 'autocomplete',
            source: datalist02,
            strict: true,
            allowInvalid: false
          }, {}, {}, {}, {
            type: 'autocomplete',
            strict: true,
            allowInvalid: false,
            source(query, process) {
              let row = this.row
              let f5_device_ip = myDataGrid.getDataAtCell(row, 0)
              $.ajax({
                type: "GET",
                url: '/api/cm/f5/get-list-client-ssl-profile?f5_device_ip=' + f5_device_ip,
                success: function (response) {
                  process(response.datalist)
                }
              })
            },
          },
          {
            type: 'autocomplete',
            strict: true,
            allowInvalid: false,
            source(query, process) {
              let row = this.row
              let f5_device_ip = myDataGrid.getDataAtCell(row, 0)
              $.ajax({
                type: "GET",
                url: '/api/cm/f5/get-list-server-ssl-profile?f5_device_ip=' + f5_device_ip,
                success: function (response) {
                  process(response.datalist)
                }
              })
            }
          },
          {
            type: 'autocomplete',
            strict: true,
            allowInvalid: false,
            source(query, process) {
              $.ajax({
                type: "GET",
                url: '/api/cm/f5/get-list-template',
                success: function (response) {
                  process(response.datalist)
                }
              })
            }
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
          url: '/api/cm/f5/create-virtual-server',
          dataType: "json",
          data: {
            'datalist': datalist03
          },
          success: function (response) {
            if (response.status == 'success') {
              Swal.fire({
                text: response.message,
                icon: "success"
              }).then(function () {
                window.location = '/cm/f5/list-virtual-server';
              })
            }
            else {
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

