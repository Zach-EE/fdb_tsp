console.log('first')
var socket = new WebSocket('ws://localhost:8000/ws/pages/');

socket.onmessage = function(event){
    var wsData = JSON.parse(event.data);
    console.log(wsData);
    document.querySelector('#app').innerText = wsData.value;
}