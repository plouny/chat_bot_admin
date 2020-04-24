$(() => {
    $("#submit").click((ev) => {
        ev.preventDefault();
        var form = $("#admin_form");
        var login = form.find('input[name="login"]').val();
        var password = form.find('input[name="password"]').val();
        $.ajax({
            url: "/admin_auth",
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                login: login,
                password: password
            }),
            success: (data) => {
                console.log(data)
                if (data.ok != undefined) {
                    if (data.ok) {
                        $(location).attr('href', "/events");
                    } else {
                        var res = document.getElementById("response")
                        console.log(res)
                        res.style.paddingBottom = "5px"
                        res.style.paddingTop = "5px"
                        res.style.border = "0"
                        res.style.display = "block"
                        
                        res.innerHTML = data.message
                    }
                }
            }
        });
    });
});