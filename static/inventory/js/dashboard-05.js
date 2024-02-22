$.ajax({
	url: '/api/inventory/dashboard-05',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		var chart = new CanvasJS.Chart("chartContainer-05", {
			animationEnabled: true,
<<<<<<< HEAD
			exportEnabled: true,
			title: {
=======
			theme: "light2",
			title:{
>>>>>>> 132d18df18dbb255136f81d551245bac572c316b
				text: "Count device by location",
				fontFamily: "tahoma",
				fontSize: 20,
				fontWeight: "normal"
<<<<<<< HEAD
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
=======
			},
			axisY: {
				title: "Device",
				suffix: ""
			},
			data: [{        
				type: "line",
				indexLabelFontSize: 16,
>>>>>>> 132d18df18dbb255136f81d551245bac572c316b
				dataPoints: data.data
			}]
		});
		chart.render();
	}
})


