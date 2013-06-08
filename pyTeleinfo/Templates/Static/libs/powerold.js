$(document).ready(
function() {setTimeout(requestInventory,100);}
);

function requestInventory() {
jQuery.getJSON('//localhost:9090/power',

function(data, status, xhr) {
$('#pow').html(data['power']);
setTimeout(requestInventory, 0);}
);}


$(document).ready(
function() {
	setTimeout(requestInventory,100);}
);

function requestInventory() {


$.getJSON('//localhost:9090/power',
function(data) {   
$('#pow').html(data['power']);       
}
);
	
setTimeout(requestInventory,1000);


}




$.getJSON('fichier.json', 
function(donnees) {
        $('#r').html('<p><b>Nom</b> : ' + donnees.nom + '</p>');
      });

</script>

$(document).ready(
function() {
	setTimeout(requestInventory,100);}
);



function requestInventory() {


jQuery.getJSON('//localhost:9090/power', {},


function(data) {
	$('#pow').html(Math.random());
	setTimeout(requestInventory,1000);
	}

	);
}//fin du script
