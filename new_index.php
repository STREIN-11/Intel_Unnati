<?php
$y = array(trim(file_get_contents('t.txt')));
foreach ($y as $key) {
	$dataPoints = array();
	array_push($dataPoints,array("label"=> "Capacity 1", "y"=> $key));
}
?>
<!DOCTYPE HTML>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
}

.navbar {
  overflow: hidden;
  background-color: #333;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>
<script>
window.onload = function () {
 
var chart = new CanvasJS.Chart("chartContainer", {
	title: {
		text: "Water Capacity Measure"
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
		color = yVal > 75 ? "#41CF35" : yVal >= 50 ? "#FF6000" : yVal < 50 ? "#FF2500" : null;
		dps[i] = {label: "Core "+(i+1) , y: yVal, color: color};
		
	}
	chart.options.data[0].dataPoints = dps;
	chart.render();
};
updateChart();
 
setInterval(function () { updateChart() }, 1000);

// window.setInterval('refresh()', 1000);

window.setTimeout( function() {
  window.location.reload();
}, 10000)
 
}
</script>
</head>
<body>

<div class="navbar">
  <a href="new_index.php">Home</a>
  <a href="#news">News</a>
  <div class="dropdown">
    <button class="dropbtn">Dropdown 
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="new_index1.php">Water Lavel</a>
      <a href="soil_most.php">Soil Mosture</a>
      <a href="relay_mod.php">Pumping System</a>
    </div>
  </div> 
</div>


<div align="center">
<div id="chartContainer" style="height: 370px; width: 55%;"></div></div>
<script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
<button onClick="window.location.reload();">Update Data</button>
</body>
</html>                              