<html>
<body>
<h1>Signup<?h1>
{{message}}<br/>
<form action="/signup" method="post">
    <hr/>
    <table>
        <tr>
        <td><h3> Name<h3/><td/>
        <td><input type="text" name="username"/><br/><td/>
        <tr/>
        <tr>
        <td><h3> Password<h3/><td/>
        <td><input type="password" name="password"/><td/>
        <tr/>
        <tr>
        <td><h3> Password, again<h3/><td/>
        <td><input type="password" name="password_again"/><td/>
        <tr/>
    <table/>
    <input type="submit" value="Submit"/>
    <hr>
    <a href="/login",">If you have an account, you can login up here</a>
</form>
</body>
</html>