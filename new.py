import random
import time
i = 0
while (i<1) : 
     time.sleep(2)
     a = (random.randint(0,1))
     # print(a)
     f = open("motor.txt", "w")
     f.write(f"{a}")
     i+=1

# <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>
# var dataPoints = <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>;


# var updateInterval = 1500;
# setInterval(function () { updateChart() }, updateInterval);

# var xValue = dataPoints.length;
# var yValue = dataPoints[dataPoints.length - 1].y;

# function updateChart() {
# 	yValue += (Math.random() - 0.5) * 0.1;
# 	dataPoints.pop({ x: xValue, y: yValue });
# 	dataPoints.push({ x: xValue, y: yValue });
# 	xValue++;
# 	chart.render();
# };

# }