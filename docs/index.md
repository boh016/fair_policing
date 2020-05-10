---
layout: default
title: RML vs Traffic Collisions
---
[main page](https://boh016.github.io/fair_policing/)
# RML
in 2016 California has legalized recreational use of marijuana.

picture
![revenue](./assets/revenue.jpg "revenue")


<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/opSiomnDEQo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<iframe class="highcharts-iframe" src="https://app.everviz.com/embed/cUNgFv-c/" title="Chart: " style="border: 0; width: 100%; height: 500px"></iframe>

<html>
   <head>
      <title>Highcharts Tutorial</title>
      <script src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js">
      </script>
      <script src = "https://code.highcharts.com/highcharts.js"></script>    
      <script src = "https://code.highcharts.com/highcharts-more.js"></script>    
      <script src = "https://code.highcharts.com/modules/heatmap.js"></script>  
   </head>
   
   <body>
      <div id = "container" style = "width: 550px; height: 400px; margin: 0 auto"></div>
      <script language = "JavaScript">
         $(document).ready(function() {
            var chart = {
               type: 'heatmap',
               marginTop: 40,
               marginBottom: 80
            };
            var title = {
               text: 'Sales per employee per weekday'   
            };
            var xAxis = {
               categories: ['Alexander', 'Marie', 'Maximilian', 'Sophia', 'Lukas',
                  'Maria', 'Leon', 'Anna', 'Tim', 'Laura']
            };
            var yAxis = {
               categories: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
               title: null
            };
            var colorAxis = {
               min: 0,
               minColor: '#FFFFFF',
               maxColor: Highcharts.getOptions().colors[0]
            };
            var legend = {
               align: 'right',
               layout: 'vertical',
               margin: 0,
               verticalAlign: 'top',
               y: 25,
               symbolHeight: 280
            };
            var tooltip = {
               formatter: function () {
                  return '<b>' + this.series.xAxis.categories[this.point.x] +
                  '</b> sold <br><b>' +
                  this.point.value +
                  '</b> items on <br><b>' +
                  this.series.yAxis.categories[this.point.y] + '</b>';
               }
            };
            var series = [{
               name: 'Sales per employee',
               borderWidth: 1,
               data: [[0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67],
                  [1, 0, 92], [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48],
                  [2, 0, 35], [2, 1, 15], [2, 2, 123], [2, 3, 64], [2, 4, 52],
                  [3, 0, 72], [3, 1, 132], [3, 2, 114], [3, 3, 19], [3, 4, 16],
                  [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], [4, 4, 115],
                  [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120],
                  [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96],
                  [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30],
                  [8, 0, 85], [8, 1, 97], [8, 2, 123], [8, 3, 64], [8, 4, 84],
                  [9, 0, 47], [9, 1, 114], [9, 2, 31], [9, 3, 48], [9, 4, 91]],
               dataLabels: {
                  enabled: true,
                  color: '#000000'
               }
            }];

            var json = {};   
            json.chart = chart; 
            json.title = title;       
            json.xAxis = xAxis; 
            json.yAxis = yAxis; 
            json.colorAxis = colorAxis; 
            json.legend = legend; 
            json.tooltip = tooltip; 
            json.series = series;       

            $('#container').highcharts(json);
         });
      </script>
   </body>
   
</html>