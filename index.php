<?php
 
$dataPoints = array();
$y = 0;
for($i = 0; $i < 10; $i++){
	$j=$i;
	$j--;
	if ($i>=0) {
		# code...
		array_pop($dataPoints);
	}	
	$y = trim(file_get_contents('test.txt')); 
	array_push($dataPoints, array("x" => 1, "y" => $y));
	// print_r($dataPoints);

}
 
?>
<!DOCTYPE HTML>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.3/Chart.min.js"></script> 
</head>
<body>
<script>
window.onload = function() {
 
var dataPoints = <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>;
 
var chart = new CanvasJS.Chart("chartContainer", {
	theme: "light3",

	data: [{
		type: "column",
		yValueFormatString: "#,##0.0#",
		toolTipContent: "{y} Mbps",
		dataPoints: dataPoints
	}]
});
chart.render();
 
var updateInterval = 1500;
setInterval(function () { updateChart() }, updateInterval);

var xValue = dataPoints.length;
var yValue = dataPoints[dataPoints.length].y;

setInterval(function() {
		var x = (new Date()).getTime(); // current time
                var y=$.get('test.txt', function(data) {
                         $('.result').txt(data);
                         });
		data.dataPoints([x,y], true, false);
		}, 100);
 
 
function updateChart() {
		// yValue += (Math.random() - 0.5) * 0.1;
		
		dataPoints.pop({ x: xValue, y: yValue });
		dataPoints.push({ x: xValue, y: yValue });
		// location.reload();
		
		chart.render();
	};

}
</script>

<div align="center">
<div id="chartContainer" style="height: 370px; width: 50%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script> 
<button type="button" id="myBtn">Update Data Point</button>
<input type="button" value="Add Data" onclick="upg()">
<meter value="30" min="1" max="100">30 out of 100</meter>
</body>
</html>   