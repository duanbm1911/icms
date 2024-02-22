$.ajax({
	url: '/api/inventory/dashboard-04',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		var chart = new CanvasJS.Chart("chartContainer-04", {
			animationEnabled: true,
			theme: "light2", // "light1", "light2", "dark1", "dark2"
			exportEnabled: true,
			title: {
				text: "Count device by type",
				fontFamily: "tahoma",
				fontSize: 20,
				fontWeight: "normal"
			},
			axisY: {
				title: "Device",
				suffix: ""
			},
			axisX: {
				title: ""
			},
			data: [{
				type: "line",
				yValueFormatString: "",
				dataPoints: data.data
			}]
		});
		chart.render();
	}
})