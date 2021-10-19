<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Material+Icons"
      rel="stylesheet">
</head>
<body>
<h2>Hello, {{name}}!</h2>
<hr>
<table>
% for item in items:
    <tr>
        <td>
          {{item['note']}}
        </td>
        <td>
          <a href="/edit/{{item['id']}}">
            <span class="material-icons">edit</span>
          </a>
        </td>
        <td>
          <a href="/delete/{{item['id']}}">
            <span class="material-icons">delete</span>
          </a>
        </td>
    </tr>
% end
</table>
<hr/>
<a href="/create_note">Create a new note...</a>
</body>
</html>