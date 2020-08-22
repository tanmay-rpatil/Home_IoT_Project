var req = new XMLHttpRequest();
req.open('GET', 'http://127.0.0.1:8000/polls/iot'); // replace "127.0.0.1" with your local IP address
req.onload= function(){
    var data = JSON.parse(req.responseText);
    console.log(data);
    document.getElementById("temperature").innerHTML = data[0].temperature + " C"
    document.getElementById("humidity").innerHTML = data[0].humidity + "%"
}
req.send();