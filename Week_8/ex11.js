function printer(total) {
    console.log(total);
}

function add(p1, p2, callback) {
    let z = p1 + p2;
    callback(z);
}

let x = 1;
let y = 3;

add(x, y, printer);