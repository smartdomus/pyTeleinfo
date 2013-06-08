$(document).ready(



function() {

	setTimeout(requestInventory,100);}
);

function requestInventory() {

$.getJSON('//localhost:9090/data', function(donnees) {
		$('#pow').val(donnees.power);
});

	
setTimeout(requestInventory,1000);
}
