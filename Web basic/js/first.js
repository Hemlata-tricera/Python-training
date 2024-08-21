//DAY-10
//Datatypes in JS
let age = 65; //Number
let price = 100.50; //Number
let fullName = "Hemlata V. Raghuvanshi" //string
isFollow = true; //Boolean
let x;  //undefined
let y = null; //
//Object Example 1
const student = {
    name: "Hemlata",
    age: 30,
    cgpa: 8.9,
    isPass: true,
};

console.log(student["cgpa"]);
console.log(student["name"]);
//Object Example 2
const product = {
    title: "Ball pen",
    rating: 5,
    offer: 5,
    price: 270,
};
console.log(typeof product);
document.write("type of product is",'<br>', typeof product["title"],'<br>');
console.log(typeof product["title"]);

//Array Datatype
const cars = ["Saab","Volvo","BMW"];
document.write("Cars name-", cars);


