

var socket = new WebSocket("ws://localhost:8000/ws/data/");
socket.onopen = function(e){
    socket.send(data)
}

socket.onmessage = function(e){
    var recData = JSON.parse(e.data);
    // console.log(recData);
    document.querySelector('#app').innerText = recData.value.y;
    };
