<html>
%include header
<body>
{{message}}<br/>
<div class="container">
<h2>Login</h2>
<form action="/login" method="post">
    <div class="form-group">
    <label for="username">Name:</label>
    <input type="test" class="form-control" id="username" name="username" placeholder="Enter Name"/>
    </div>
    <div class="form-group">
    <label for="password">Password:</label>
    <input type="password" class="form-control" id="password" name="password" placeholder="Enter Password"/>
    </div>
    <div class="form-group form-check">
    <label class="form-check-label></label>
    <input class="form-check-input" type="checkbox" name="remember">Remember Me</input>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button> value="Submit"/>
</form>
<div>
    <hr>
    <a href="/signup",">If you need a new account, you can sign up here</a>
</body>
</html>