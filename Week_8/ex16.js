function Person(name, age, address) {
    this.name = name;
    this.age = age;
    this.address = address;
    function sayHello() {
        console.log("Hello, my name is " + this.name);
    }
}

let person_1 = new Person("anya", 33, "dead");
let person_2 = new Person("swansea", 65, "dead");
let person_3 = new Person("curly", 35, "alive");
let person_4 = new Person("daisuke", 22, "dead");
let person_5 = new Person("j*mmy", 35, "dead");

person_1.sayHello();
