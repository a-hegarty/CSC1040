let people = [];

let person_1 = {};

person_1.name = "amanda";
person_1.age = 33;
person_1.address = "123";

people.push(person_1);

let person_2 = {};

person_2.name = "bernard";
person_2.age = 44;
person_2.address = "234";

people.push(person_2);

for(i in people) {
    console.log(people[i]);
}