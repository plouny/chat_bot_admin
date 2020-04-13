$(() => {
    var socket = io.connect('http://localhost:5000');
    
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
})