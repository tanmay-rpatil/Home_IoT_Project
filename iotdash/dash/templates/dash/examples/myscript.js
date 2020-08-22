var req = new XMLHttpRequest();
req.open('GET', 'http://192.168.29.103:8000/api/');
req.onload= function(){
	console.log("Hi, here")
    var data_c = JSON.parse(req.responseText);
    // console.log("Hi"+data[0].temperature + " C");
    // document.getElementById("temperature").innerHTML = data[0].temperature + " C";
    // document.getElementById("humidity").innerHTML = data[0].humidity + "%";
};
req.send();