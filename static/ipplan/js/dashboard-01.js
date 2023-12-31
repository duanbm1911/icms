var chart = new CanvasJS.Chart("chartContainer-01", {
	animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	exportEnabled: true,
	title: {
		text: "Count device by category",
		fontFamily: "tahoma"
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
		dataPoints: [
			{ label: "Switch", y: 100 },	
			{ label: "Router", y: 200 },	
			{ label: "Firewall", y: 30 },
			{ label: "Proxy", y: 10 },	
			{ label: "WAF", y: 5 },
			{ label: "ADC", y: 4 }
		]
	}]
});
chart.render();



