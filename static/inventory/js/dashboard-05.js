var chart = new CanvasJS.Chart("chartContainer-05", {
	animationEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title: {
		text: "GDP Growth Rate - 2016"
	},
	axisY: {
		title: "Growth Rate (in %)",
		suffix: "%"
	},
	axisX: {
		title: "Countries"
	},
	data: [{
		type: "column",
        indexLabelPlacement: "outside",
		yValueFormatString: "#,##0.0#\"%\"",
		dataPoints: [
			{ label: "DC/DR", y: 10 },	
			{ label: "Branch", y: 40 },	
			{ label: "HO-89LH", y: 5.00 },
			{ label: "HO-VHT", y: 2.50 },	
			{ label: "HO-VAT", y: 2.30 }
			
		]
	}]
});
chart.render();
