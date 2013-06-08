$(document).ready(

function() {

	setTimeout(requestPower,100);}
);

function requestPower() {

$.getJSON('192.168.0.19:9090/data', function(data) {
		$('#pow').val(data.power);
});
	
setTimeout(requestPower,1000);
}
