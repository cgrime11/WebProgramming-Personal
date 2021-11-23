<html>
<body>
<h2>Hello!</h2>
<button type="button" onclick="ajax('/weather_text',show_text)">Show Weather</button>
<hr>
<div id="weather_text">Weather data goes here</div>
<hr>
<button type="button" onclick="do_something()">Do Something</button>
<hr>
<div id="text"></div>
<hr>
<div id="alpha"></div>
<hr>
<div id="beta"></div>
<script>

function ajax(url, handler) {
    var xhttp;
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            handler(this.responseText);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send();
}

function show_text(text) {
    element = document.getElementById("weather_text");
    element.innerHTML = text;
}

function do_something() {
  text = '{"alpha":"12", "beta":"14"}';
  element = document.getElementById("text");
  element.innerHTML = text;
  object = JSON.parse(text);
  console.log(object);
  console.log(object.alpha);
  console.log(Object.keys(object));
  keys = Object.keys(object);
  console.log(keys);
  //document.getElementById(keys[0]).innerHTML = object[keys[0]];
  //document.getElementById("beta").innerHTML = object.beta;

  for (i = 0; i < 2; i++) {
    document.getElementById(keys[i]).innerHTML = object[keys[i]];
  }
      
}

</script>
</body>
</html>