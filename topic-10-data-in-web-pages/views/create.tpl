<html>
<body>
<h1>Create</h1>
<h2>New item for {{name}}...</h2>
<form action="/create_note" method="post">
  <hr/>
  <table>
    <tr>
      <td><em>Note</em></td>
      <td><input type="text" name="note"/><br/></td>
    </tr>
  </table>
  <hr/>
  <input type="submit" value="Save"/>
  <hr>
  <a href="/index">Back to the items...</a>
</form>
</body>
</html>
