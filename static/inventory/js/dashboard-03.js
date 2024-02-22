$.ajax({
	url: '/api/inventory/dashboard-03',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		var chart = new CanvasJS.Chart("chartContainer-03", {
			animationEnabled: true,
			theme: "light2",
			exportEnabled: true,
			title:{
				text: "Device configuration report",
				fontFamily: "tahoma",
				fontSize: 20,
				fontWeight: "normal"

			},
			axisX:{
				valueFormatString: "",
				crosshair: {
					enabled: true,
					snapToDataPoint: true
				}
			},
			axisY: {
<<<<<<< HEAD
				title: "Count of Device",
=======
				title: "Device",
>>>>>>> 132d18df18dbb255136f81d551245bac572c316b
				includeZero: true,
				crosshair: {
					enabled: true
				}
			},
			toolTip:{
				shared:true
			},  
			legend:{
				cursor:"pointer",
				verticalAlign: "bottom",
				horizontalAlign: "center",
				// dockInsidePlotArea: true,
				itemclick: toogleDataSeries
			},
			data: data.data
		});
		chart.render();

		function toogleDataSeries(e){
			if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
				e.dataSeries.visible = false;
			} else{
				e.dataSeries.visible = true;
			}
			chart.render();
		}
	}
})