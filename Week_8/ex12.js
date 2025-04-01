let show = function(callback) {
    callback("hello there");
}

function printer(total) {
    console.log(total);
}

show(printer);