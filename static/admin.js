$(() => {
    $("#submit").click((e) => {
        e.preventDefault();
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
                        $(location).attr('href', "/home");
                    } else {
                        $("#response").val(data.message)
                    }
                }
            }
        });
    });
});