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
console.log("type of product is", typeof product["title"]);
console.log(typeof product["title"]);

//Array Datatype
const cars = ["Saab","Volvo","BMW"];
console.log("Cars name-", cars);

//Operator
//Arithmatic operator
console.log("Arithamatic Operators-->");
let a = 20;
let b = 10;
console.log("Addition is", a + b);
console.log("substraction is", a - b);
console.log("multiplication is", a * b);
console.log("Division is", a / b);
console.log("Remainder is", a % b);
a++;
let c = a;
console.log("Increment of a is", c++);
a--;
c = a;
console.log("Decrement of a is", c--);

console.log("exponentiation of a is", a**2);
//JavaScript Comparison Operators
console.log("a==b", a == b);
let p = "Aai";
let q = "Aai";
console.log("p===q", p === q);
console.log("a===b", a == b);
console.log("a!=b", a != b);
console.log("a!==b", a !== b);
console.log("a>b", a > b);
console.log("a<b", a < b);
console.log("a>=b", a >= b);
console.log("a<=b", a <= b);
//Logical Operators

//let cond1 = a > b;
//let cond2 = a !=  b;
console.log("a > b && a != b", a > b && a != b);
console.log("a < b || a == b", a < b || a == b);
console.log("! (6 < 5)", ! (6 < 5));


















//Assignment Operator
console.log("Addition assignment of a is", a += 5);
console.log("Subtraction assignment of a is", a -= 5);
console.log("Multiplication assignment of a is", a *= 5);
console.log("Exponentiation assignment of a is", a **= 2);
console.log("Division assignment of a is", a /= 5);
console.log("Remainder assignment of a is", a %= 5);
console.log("Left Shift assignment of a is", a += 5);
console.log("Right shift assignment of a is", a += 5);









