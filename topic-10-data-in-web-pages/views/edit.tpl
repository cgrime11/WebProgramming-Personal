<html>
<body>
<h1>Edit</h1>
<h2>Editing item {{id}} for {{name}}...</h2>
<form action="/edit/{{id}}" method="post">
  <hr/>
  <table>
    <tr>
      <td><em>Note</em></td>
      <td><input type="text" name="note" value="{{value}}"/><br/></td>
    </tr>
  </table>
  <hr/>
  <input type="submit" value="Update"/>
  <hr>
  <a href="/index">Back to the items...</a>
</form>
</body>
</html>
