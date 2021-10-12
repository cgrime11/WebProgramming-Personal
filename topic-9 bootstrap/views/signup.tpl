<html>
%include header
<body>
<div class="container">
  <h2>Sign Up</h2>
  <form action="/login" method="post">
    <div class="form-group">
      <label for="username">Name:</label>
      <input type="text" class="form-control" id="username" name="username" placeholder="Enter name"/>
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" class="form-control" id="password" name="password" placeholder="Enter password"/>    
    </div>
    <div class="form-group">
      <label for="password2">Password, again:</label>
      <input type="password" class="form-control" id="password2" name="password2" placeholder="Enter password, again"/>    
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
<div>
<hr>
<a href="/login">If you have an account, you can log in...</a>
</body>
</html>
