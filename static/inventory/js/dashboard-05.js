$.ajax({
	url: '/api/inventory/dashboard-05',
	dataType: 'json',
	type: 'GET',
	success: function (data) {
		console.log(data)
		var chart = new CanvasJS.Chart("chartContainer-05", {
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
				title: "Count of Device",
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
				horizontalAlign: "left",
				dockInsidePlotArea: true,
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