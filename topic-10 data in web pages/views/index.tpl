<html>
<body>
<h2>Hello, {{name}} !</h2>
<hr>
<ul>
% for item in items:
    <li>{{str(item['note'])}}</li>
% end
</ul>
{{str(items)}}
</body>
</html>