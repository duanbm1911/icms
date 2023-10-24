var chart = new CanvasJS.Chart("chartContainer-02", {
	animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	title: {
		text: "Count device by vendor"
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
		yValueFormatString: "#,##0.0#\"\"",
		dataPoints: [
			{ label: "Cisco", y: 300 },	
			{ label: "Checkpoint", y: 200 },	
			{ label: "Fortigate", y: 10 },
			{ label: "Symantec", y: 10 },	
			{ label: "F5", y: 5 },
			{ label: "Citrix", y: 4 }
		]
	}]
});
chart.render();
