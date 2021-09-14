<html>
<body>
%if extra == None:
    <h2> Hello, {{name.upper()}}!</h2>
%else :
    <h2> Hello, {{name}}! {{extra}}</h2>
%end
... from the template!
</body>
</html>