var chart = new CanvasJS.Chart("chartContainer-01", {
	animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	exportEnabled: true,
	title: {
		text: "Count device by category"
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

var toolBar = document.getElementsByClassName("canvasjs-chart-toolbar")[0];
if(chart.get("exportEnabled")){
  var exportCSV = document.createElement('div');
  var text = document.createTextNode("Save as CSV");
  exportCSV.setAttribute("style", "padding: 12px 8px; background-color: white; color: black")
  exportCSV.appendChild(text);

  exportCSV.addEventListener("mouseover", function(){
    exportCSV.setAttribute("style", "padding: 12px 8px; background-color: #2196F3; color: white")
  });
  exportCSV.addEventListener("mouseout", function(){
    exportCSV.setAttribute("style", "padding: 12px 8px; background-color: white; color: black")
  });
  exportCSV.addEventListener("click", function(){
    downloadCSV({ filename: "chart-data.csv", chart: chart })
  });
  toolBar.lastChild.appendChild(exportCSV);
}
else {
  var exportCSV = document.createElement('button');	
  var text = document.createTextNode("Save as CSV");	
  exportCSV.appendChild(text);
  exportCSV.addEventListener("click", function(){
    downloadCSV({ filename: "chart-data.csv", chart: chart })
  });
  document.body.appendChild(exportCSV)
}


function mergeData(data) {
  var mergedDps = [],
      result = [];
  for (var i = 0; i < data.length; i++) {
    for (var j = 0; j < data[i].dataPoints.length; j++) {
      mergedDps.push(cloneObject(data[i].dataPoints[j]));
    }
  }

  mergedDps.forEach(function (item) {
    var existing = result.filter(function (v, i) {
      return v.x == item.x;
    });
    if (existing.length) {
      var existingIndex = result.indexOf(existing[0]);
      result[existingIndex].y = result[existingIndex].y.concat(item.y);
    } else {
      if (typeof item.y == 'string' || typeof item.y == 'number')
        item.y = [item.y];
      result.push(item);
    }
  });
  for (var i = 0; i < result.length; i++) {
    for (var j = 0; j < result[i].y.length; j++) {
      result[i]["y" + j] = result[i].y[j];
    }
    delete result[i].y;
  }
  return result;
}

function convertChartDataToCSV(args) {
  var result = '',
      ctr, keys, columnDelimiter, lineDelimiter, data;

  data = args.data || null;
  if (data == null || !data.length) {
    return null;
  }

  columnDelimiter = args.columnDelimiter || ',';
  lineDelimiter = args.lineDelimiter || '\n';

  var mergedData = mergeData(data);

  keys = Object.keys(mergedData[0]);
  result = '';
  result += keys.join(columnDelimiter);
  result += lineDelimiter;

  mergedData.forEach(function (item) {
    ctr = 0;
    keys.forEach(function (key) {
      if (ctr > 0) result += columnDelimiter;
      result += (typeof (item[key]) != undefined ? item[key] : "");
      ctr++;
    });
    result += lineDelimiter;
  });
  return result;
}

function parseCSV(args) {
  var csv = "";

  csv += convertChartDataToCSV({
    data: args.chart.options.data
  });

  if (csv == null) return;
  var filename = args.filename || 'chart-data.csv';
  if (!csv.match(/^data:text\/csv/i)) {
    csv = 'data:text/csv;charset=utf-8,' + csv;
  }
  downloadFile(csv, filename);
}

function downloadCSV(args) {
  var data, filename, link;
  var csv = "";
  csv += convertChartDataToCSV({
    data: args.chart.options.data
  });
  if (csv == null) return;

  filename = args.filename || 'chart-data.csv';

  if (!csv.match(/^data:text\/csv/i)) {
    csv = 'data:text/csv;charset=utf-8,' + csv;
  }

  data = encodeURI(csv);
  link = document.createElement('a');
  link.setAttribute('href', data);
  link.setAttribute('download', filename);
  document.body.appendChild(link); // Required for FF
  link.click(); 
  document.body.removeChild(link);   
}

function cloneObject(obj) {
	if (obj === null || typeof obj !== "object") {
		return obj;
	}
	if (obj instanceof Date) {
		return new Date(obj.getTime());
	}
	if (!Array.isArray) {
		Array.isArray = function (arg) {
			return Object.prototype.toString.call(arg) === '[object Array]';
		};
	}
	if (Array.isArray(obj)) {
		var clonedArr = [];
		for (var i = 0; i < obj.length; i++) {
			clonedArr.push(cloneObject(obj[i]))
		}
		return clonedArr;
	}
	var clonedObj = new obj.constructor();
	for (var prop in obj) {
		if (obj.hasOwnProperty(prop)) {
			clonedObj[prop] = cloneObject(obj[prop]);
		}
	}
	return clonedObj;
}
