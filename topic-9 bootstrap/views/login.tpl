<html>
%include header
<body>
<div class="container">
  <h2>Login</h2>
  <form action="/login" method="post">
    <div class="form-group">
      <label for="username">Name:</label>
      <input type="text" class="form-control" id="username" name="username" placeholder="Enter name"/>
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" class="form-control" id="password" name="password" placeholder="Enter password"/>    
    </div>
    <div class="form-group form-check">
      <label class="form-check-label">
         <input class="form-check-input" type="checkbox" name="remember">Remember me</input>
      </label>
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
<div>
<hr>
<a href="/signup">If you need a new account, you can sign up...</a>

<div class="container">
  <div class="row">
     <div class="col-4 bg-info">Hello</div>
     <div class="col-8 bg-warning">Goodbye</div>
  </div>
  <div class="row">
     <div class="col-4 bg-success">Hola</div>
     <div class="col-8 bg-danger">Adios</div>
  </div>
  <div class="row">
     <div class="col-4 bg-success"></div>
     <div class="col-8">
                <div class="container">
                  <div class="row">
                    <div class="col-4 bg-info">Hello</div>
                    <div class="col-8 bg-warning">Goodbye</div>
                  </div>
                  <div class="row">
                    <div class="col-4 bg-success">Hola</div>
                    <div class="col-8 bg-danger">Adios</div>
                  </div>
                </div>
     </div>
  </div>

</div>
<hr/>
<div class="container">
  <div class="row">
     <div class="col-sm-5 col-md-3 bg-info">Hello</div>
     <div class="col-sm-7 col-md-8 bg-warning">Goodbye</div>
     <div class="col-sm-0 col-md-1 bg-success">!!</div>
  </div>
  <div class="row">
     <div class="col-sm-5 col-md-3 bg-success">Hola</div>
     <div class="col-sm-7 col-md-8 bg-danger">Adios</div>
     <div class="col-sm-0 col-md-1 bg-success">!!</div>
  </div>
</div>
</body>
</html>
