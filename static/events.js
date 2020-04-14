$(() => {
    var socket = io.connect('http://localhost:5000');

    socket.on("change", (data) => {
        var events = data.events;
        var help_requests = data.help_requests;
        console.log(data);
        $("#events").empty();
        events.forEach(event => {
            $("#events").append(`<div>${event.id}: ${event.name}</div>`);
        });
    });
    socket.on("connect", () => {
        socket.emit("update");
    });

    $(".button_delete").click(() => {
        socket.emit("change", {delete: $(this).metadata()});
    });
});