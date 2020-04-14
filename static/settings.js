$(() => {
    var socket = io.connect('http://localhost:5000');

    socket.on("message", message => {
        alert(message.message);
        if (message.ok) {
            window.location.reload(true);
        }
    });

    $("form").submit((event) => {
        var form = $("form");
        
        var children = form.children();
        console.log(children);
        var old_password = children[0].value;
        var new_password = children[1].value;
        var conf_new_password = children[2].value;
        if (new_password == conf_new_password) {
            socket.emit("change", {
                password: {
                    old: old_password,
                    new: new_password
                }   
            });
        } else {
            alert("Passwords don't match");
        }
        return false;
    });
});