$(() => {
    var socket = io.connect('http://localhost:5000');
    
    socket.on("change", (data) => {
        var events = data.events;
        var help_requests = data.help_requests;
        console.log(data);
        $("#events").empty();
        $("#help_requests").empty();
        events.forEach(event => {
            $("#events").append(`<div>${event.id}: ${event.name}</div>`);
        });
        help_requests.forEach(help_request => {
            $("#help_requests").append(`<div>${help_request.time_requested} ${help_request.question}</div>`)
        });
    });
    socket.on("connect", () => {
        socket.emit("update");
    });

    $(".button_delete").click(() => {
        socket.emit("change", {delete: $(this).metadata()});
    });

    $("form").submit((event) => {
        console.log($(this));
        console.log(event);
        var form = $("form");
        
        var children = form.children();
        console.log(children);
        var name = children[0].value;
        var description = children[1].value;
        var day_start = children[2].value;
        var day_end = children[3].value;
        var form = {
            name: name,
            description: description,
            day_start: day_start,
            day_end: day_end
        };
        console.log(form);
        socket.emit("change", {add: form});
        return false;
    });
});

