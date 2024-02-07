$.ajax({
	url: '/api/inventory/dashboard-05',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		var chart = new CanvasJS.Chart("chartContainer-05", {
			animationEnabled: true,
			theme: "light2",
			title:{
				text: "Count device by location",
				fontFamily: "tahoma",
				fontSize: 20,
				fontWeight: "normal"
			},
			data: [{        
				type: "line",
				indexLabelFontSize: 16,
				dataPoints: data.data
			}]
		});
		chart.render();
	}
})


