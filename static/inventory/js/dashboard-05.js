var chart = new CanvasJS.Chart("chartContainer-05", {
	animationEnabled: true,
	exportEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Count of device non-compliance configuration"
	},
  	axisY: {
      includeZero: true
    },
	data: [{
		type: "column", //change type to bar, line, area, pie, etc
		//indexLabel: "{y}", //Shows y value on all Data Points
		indexLabelFontColor: "#5A5757",
      	indexLabelFontSize: 16,
		indexLabelPlacement: "outside",
		dataPoints: [
			{ x: "DC/DR", y: 71 },
			{ x: "Branch", y: 55 },
			{ x: "HO-89LH", y: 50 },
			{ x: "HO-VHT", y: 50 },
			{ x: "HO-VAT", y: 50 },
			{ x: "HO-MNT", y: 50 }
		]
	}]
});
chart.render();
