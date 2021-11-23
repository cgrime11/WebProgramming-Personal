<html>
<body>
<h1>Ajax Example</h1>
<button type="button" onclick="load_text()">Show Text #1</button>
<button type="button" onclick="ajax('/example_text',show_text)">Show Text #2</button>
<button type="button" onclick="ajax('/other_text',show_text)">Show TTNBC</button>
<hr/>
<h2>The example text is...</h2>
<hr/>
<div id="example_text"></div>
<hr/>
<script>

function load_text() {
    var xhttp;
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            show_text(this.responseText);
        }
    }
    xhttp.open("GET","/example_text",true);
    xhttp.send();
}

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
    element = document.getElementById("example_text");
    element.innerHTML = text;
}
</script>
</body>
</html>