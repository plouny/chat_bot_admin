$(() => {
    var socket = io.connect('http://localhost:5000');

    var changeResponse = (message, ok) => {
        var res = document.getElementById("response")
        res.style.paddingBottom = "5px"
        res.style.paddingTop = "5px"
        res.style.border = "0"
        
        var cl = "alert-danger"
        if (ok) {
            cl = "alert-success"
        }
        res.classList.add(cl)   

        res.style.display = "block"
        res.innerHTML = message
    }

    socket.on("message", message => {
        changeResponse(message.message, message.ok);
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
            changeResponse("Passwords don't match", false);
        }
        return false;
    });
});