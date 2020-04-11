$(() => {
    var socket = io.connect('http://localhost:5000');
    
    socket.on("change", (data) => {
        var events = data.events;
        var help_requests = data.help_requests;
        console.log(data);
        events.forEach(event => {
            $("#events").append(`<div>${event.name}</div>`);
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

    $(".button_add").on("click", () => {
        var div = $(this).parent();
        console.log($(this));
        console.log(div);
        var name = div.find($('input[name="event_name"]')).val();
        var description = div.find($('input[name="event_description"]')).val();
        var day_start = div.find($('input[name="day_start"]')).val();
        var day_end = div.find($('input[name="day_end"]')).val();
        var form = {
            name: name,
            description: description,
            day_start: day_start,
            day_end: day_end
        };
        console.log(form);
        socket.emit("change", {add: form});
    });
});

