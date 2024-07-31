$.ajax({
	url: '/api/ipplan/dashboard-03',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		console.log(data)
		var chart = new CanvasJS.Chart("chartContainer-03", {
			animationEnabled: true,
			theme: "light2", // "light1", "light2", "dark1", "dark2"
			exportEnabled: true,
			title: {
				text: "Top 20 subnets with highest IP usage (%)",
				fontFamily: "tahoma",
				fontSize: 20,
				fontWeight: "normal"
			},
			axisY: {
				title: "Percent",
				maximum: 100,
				suffix: ""
			},
			axisX: {
				title: ""
			},
			data: [{
				type: "bar",
				yValueFormatString: "",
				dataPoints: data.data
			}]
		});
		chart.render();
	}
})


