$(document).ready(

function() {
	setTimeout(requestPower,100);}
);

function requestPower() {

$.getJSON(namespace+'/data', function(data) {
	power=data.Power;
	//$('#pow').val(data.power);

});
	
setTimeout(requestPower,1000);
}
