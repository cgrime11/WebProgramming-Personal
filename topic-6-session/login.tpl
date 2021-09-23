<html>
<body>
<h1>Login<?h1>
{{message}}<br/>
<form action="/login" method="post">
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
        <td><h3> Favorite Color<h3/><td/>
        <td><input type="text" name="favcolor"/><td/>
        <tr/>
    <table/>
    <input type="submit" value="Submit"/>
</form>
</body>
</html>