		$(function () {
		    var chart = new Highcharts.Chart({
			
			    chart: {
			        renderTo: 'gauge',
			        type: 'gauge',
			        plotBackgroundColor: null,
			        plotBackgroundImage: null,
			        plotBorderWidth: 0,
			        plotShadow: true
			    },
			    
			    title: {
			        text: 'Actual power consumption : '
			    },
			    
			    pane: {
			        startAngle: -150,
			        endAngle: 150,
			        background: [{
			            backgroundColor: {
			                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
			                stops: [
			                    [0, '#FFF'],
			                    [1, '#333']
			                ]
			            },
			            borderWidth: 0,
			            outerRadius: '105%'
			        }, {
			            backgroundColor: {
			                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
			                stops: [
			                    [0, '#333'],
			                    [1, '#FFF']
			                ]
			            },
			            borderWidth: 1,
			            outerRadius: '80%'
			        }, {
			            // default background
			        }, {
			            backgroundColor: '#DDD',
			            borderWidth: 0,
			            outerRadius: '105%',
			            innerRadius: '103%'
			        }]
			    },
			       
			    // the value axis
			    yAxis: {
			        min: 0,
			        max: 7000,
			        
			        minorTickInterval: 'auto',
			        minorTickWidth: 1,
			        minorTickLength: 11,
			        minorTickPosition: 'inside',
			        minorTickColor: '#666',
			
			        tickPixelInterval: 40,
			        tickWidth: 2,
			        tickPosition: 'inside',
			        tickLength: 10,
			        tickColor: '#666',
			        labels: {
			            step: 2,
			            rotation: 'auto'
			        },
			        title: {
			            text: 'Watts'
			        },
			        plotBands: [{
			            from: 0,
			            to: 1000,
			            color: '#55BF3B' // green
			        }, {
			            from: 1000,
			            to: 3000,
			            color: '#DDDF0D' // yellow
			        }, {
			            from: 3000,
			            to: 7000,
			            color: '#DF5353' // red
			        }]        
			    },
			
			    series: [{
			        name: 'Actual power consumption',
			        data: [80],
			        tooltip: {
			            valueSuffix: 'Watts'
			        }
			    }]
			
			}, 
			
		
			// Add some life
			function (chart) {
			    setInterval(function () {
			    	
			        var point = chart.series[0].points[0],
			            //newVal,
			           // inc = Math.round(Math.random()*7000);
			        
			        newVal = parseInt(power) //parseInt($('#pow').val());
			       // if (newVal < 0 || newVal > 7000) {
			         //   newVal = point.y - inc;
			        //}
			        
			        point.update(newVal);
			        
			    }, 2000);
			   
			});
		    
		    
		    
		});