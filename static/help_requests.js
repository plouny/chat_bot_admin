$(() => {
    var socket = io.connect('http://localhost:5000');

    socket.on("change", (data) => {
        var events = data.events;
        var help_requests = data.help_requests;
        console.log(data);
        $("#help_requests").empty();
        help_requests.forEach(help_request => {
            $("#help_requests").append(`<div сlass="grid-item">${help_request.time_requested} ${help_request.question}</div>`)
        });
    });
    socket.on("connect", () => {
        socket.emit("update");
    });

    $(".button_delete").click(() => {
        socket.emit("change", {delete: $(this).metadata()});
    });
});