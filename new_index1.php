<?php
$y = array(trim(file_get_contents('test.txt')));
foreach ($y as $key) {
	$dataPoints = array();
	array_push($dataPoints,array("label"=> "Core 1", "y"=> $key));
} 
?>
<!DOCTYPE HTML>
<html>
<head>

<script>
window.onload = function () {
 
var chart = new CanvasJS.Chart("chartContainer", {
	title: {
		text: "Water Level Measure"
	},
	axisY: {
		minimum: 0,
		maximum: 100,
		suffix: "%"
	},
	data: [{
		type: "column",
		yValueFormatString: "#,##0.00\"%\"",
		indexLabel: "{y}",
		dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>
	}]
});
 
function updateChart() {
	var color,deltaY, yVal;
	var dps = chart.options.data[0].dataPoints;
	for (var i = 0; i < dps.length; i++) {
		deltaY = 0;
        deltaY++;
		yVal =  Math.min(Math.max(dps[i].y, 0), 90);
		color = yVal > 75 ? "#FF2500" : yVal >= 50 ? "#FF6000" : yVal < 50 ? "#41CF35" : null;
		dps[i] = {label: "Core "+(i+1) , y: yVal, color: color};
		
	}
	chart.options.data[0].dataPoints = dps;
	chart.render();
};
updateChart();
 
setInterval(function () { updateChart() }, 1000);
 
}
</script>
</head>
<body>

<div align="center">
<div id="chartContainer" style="height: 370px; width: 55%;"></div></div>
<script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
<button onClick="window.location.reload();">Update Data</button>
</body>
</html>                              