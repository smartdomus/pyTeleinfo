$(document).ready(

function() {
var uri="ws://"+namespace+"/ws"
var ws = new WebSocket(uri);

ws.onmessage = function (evt) {
   power=evt.data;
};
	
	
	
	
	}
);




