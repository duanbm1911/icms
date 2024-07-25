$(document).ready(function () {
    $('#id_subnet').select2()
    $('#id_ip_address').select2()
    $('#id_subnet').change(function() {
        let subnet_id = $('#id_subnet option:selected').text()
        $.ajax({
            type: 'GET',
            url: '/api/ipplan/get-list-ip-available?subnet=' + subnet_id,
            dataType:"json",
            success: function(response) {
                if (response.status == 'success') {
                    var list_ip_available = response.data
                    $('#id_ip_address').text('')
                    list_ip_available.forEach(ip => {
                        $('#id_ip_address').append($('<option>', { 
                            value: ip,
                            text : ip 
                        }))
                    });
                    $('#ip-available').text('')
                    $('#ip-available').html('<strong style="color:red">Available: ' + list_ip_available.length + ' IP</strong>')
                }
                else {
                    $('#ip-available').text('')
                    $('#ip-available').html('<strong style="color:red">' + response.error + '</strong>')
                }
            },
        });
    });
});