window.onload = function() {
  var chart = new CanvasJS.Chart("chartContainer-03", {
	theme: "light2",
	animationEnabled: true,
	exportEnabled: true,
	title: {
		text: "Count of error log"
	},
	subtitles: [{
		//text: "United Kingdom, 2016",
		//fontSize: 16
	}],
	data: [{
		type: "pie",
		indexLabelFontSize: 18,
		radius: 80,
		indexLabel: "{label} - {y}",
		yValueFormatString: "",
		//click: explodePie,
		dataPoints: [
			{ y: 42, label: "DC/DR" },
			{ y: 21, label: "Branch"},
			{ y: 24.5, label: "HO-89LH" },
			{ y: 9, label: "HO-VHT" },
			{ y: 3.1, label: "HO-VAT" },
			{ y: 3.1, label: "HO-MNT" }
		]
	}]
});
chart.render();

}


