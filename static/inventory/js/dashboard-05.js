$.ajax({
	url: '/api/inventory/dashboard-05',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		console.log(data)
		var chart = new CanvasJS.Chart("chartContainer-05", {
			animationEnabled: true,
			exportEnabled: true,
			title: {
				text: "Count device by location",
				fontFamily: "tahoma",
				fontSize: 20,
				fontWeight: "normal"
			},
			axisX: {
				interval: 1
			},
			axisY2: {
				interlacedColor: "rgba(1,77,101,.2)",
				gridColor: "rgba(1,77,101,.1)"
			},
			data: [{
				type: "bar",
				name: "companies",
				axisYType: "secondary",
				color: "#014D65",
				dataPoints: data.data
			}]
		});
		chart.render();
	}
})


