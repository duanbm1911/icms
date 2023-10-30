$.ajax({
	url: '/api/inventory/dashboard-01',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		var chart = new CanvasJS.Chart("chartContainer-01", {
			animationEnabled: true,
			theme: "light2", // "light1", "light2", "dark1", "dark2"
			exportEnabled: true,
			title: {
				text: "Count device by category"
			},
			axisY: {
				title: "Device count",
				suffix: ""
			},
			axisX: {
				title: ""
			},
			data: [{
				type: "column",
				yValueFormatString: "",
				dataPoints: data.data
			}]
		});
		chart.render();
	}
})




