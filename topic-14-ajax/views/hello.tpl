<html>
<body>
<h2>Hello, {{name}}!</h2>
Your favorite color is {{color}}!
The weather is:
<hr>
{{str(weather)}}
<hr>
{{(weather['main']['temp'] - 273.15) * (9/5) + 32}}
<hr>
<table>
%for key in weather['main'].keys():
  <tr>
     <td>{{key}}</td>
     <td>{{weather['main'][key]}}</td>
  </tr>
%end
</table>
<hr>
<hr>
</body>
</html>