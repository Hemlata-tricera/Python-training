//DAY-10
//Datatypes in JS
let age = 65; //Number
let price = 100.50; //Number
let fullName = "Hemlata V. Raghuvanshi" //string
isFollow = true; //Boolean
let x;  //undefined
let y = null; //
// Date object:
const date = new Date("2024-08-08");
console.log("date" , date);
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
console.log(p + " " + q);//String concatination
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
console.log("Left Shift assignment of a is", a <<= 5);
console.log("Right shift assignment of a is", a >>= 5);


//Bitwise Operator
console.log("5 & 1 ", 5 & 1);
console.log("5 | 1 ", 5 | 1);
console.log("~ 5 ", ~ 5);
console.log("5 ^ 1 ", 5 ^ 1);
console.log("5 << 1 ", 5 << 1);
console.log("5 >> 1 ", 5 >> 1);
console.log("5 >>> 1 ", 5 >>> 1);

//JS Function
function myFunction(p1, p2){
    return p1 * p2;
}
console.log(myFunction(5, 5));
text = myFunction(5, 5)
console.log("The square of 5 is", text);//Using a function as a variable:


//JS String
//You can use quotes inside a string, as long as they don't match the quotes surrounding the string.
let answer1 = "It's alright";
let answer2 = "He is called 'Johnny'";
let answer3 = 'He is called "Johnny"';
console.log(answer1, answer2, answer3);
//With back-ticks, you can use both single and double quotes inside a string:
let test = `He's often called "Johnny"`;
console.log(test);
//The length Property
console.log(test.length);


//String Methods
const s = "HELLO WORLD";
console.log(s.charAt(0));
console.log(s.charCodeAt(0));
//console.log(s.at(2));
console.log(s[2]);
console.log(s[0]);
console.log(s[0]);
console.log(s.slice(2,8));
console.log(s.slice(2));
console.log(s.slice(-16));
console.log(s.slice(-9,-3));
console.log(s.substring(2,8));
console.log(s.substring(2));//If you omit the second parameter, substr() will slice out the rest of the string.
console.log(s.substring(-2));//If the first parameter is negative, the position counts from the end of the string.
console.log(s.toLowerCase());//Convert string to lower case
console.log(s);
s1 = " Hello ";
s2 = "World! ";
console.log(s1.concat(" ", s2));//concat() joins two or more strings
console.log(s1.trim());//The trim() method removes whitespace from both sides of a string:
console.log(s1.trimStart());//The trimStart() method works like trim(), but removes whitespace only from the start of a string.
console.log(s1.trimEnd());//The trimEnd() method works like trim(), but removes whitespace only from the end of a string.
console.log(s1.padStart(12,"0"));//It pads the string with another string (multiple times) until it reaches a given length.
console.log(s1.padStart(12,"x"));//It pads the string with another string (multiple times) until it reaches a given length.
let numb = 5;
let numb1 = numb.toString();
console.log(numb1.padStart(4,"0"));
console.log(numb1.padEnd(4,"0"));//The padEnd() method pads a string from the end.
console.log(numb1.padEnd(4,"x"));

console.log(s.repeat(2));/*The repeat() method returns a string with a number of copies of a string.The repeat() method returns a new string.
The repeat() method does not change the original string.*/
console.log(s.replace("WORLD", "JS"));//The replace() method replaces a specified value with another value in a string:
console.log(s.replace(/world/i, "JS"));//To replace case insensitive, use a regular expression with an /i flag (insensitive)
console.log(s.split(","));
const myArray = s.split("");
console.log(myArray[0]);

//******DAY-11********//
//Arrow Function
let myFun = (a, b) => a * b;//Arrow functions allow us to write shorter function syntax
console.log(myFun(10, 20));

hello = () => "Hello World";//This works only if the function has only one statement.
console.log(hello());
//Arrow Function With Parameters:
hello = (val) => "Hello" + val;
console.log(hello("Dolly"));
hello = val => "HEllo" + val;//In fact, if you have only one parameter, you can skip the parentheses as well:
console.log(hello("Dolly"));

//Conditional Statements
const hour = new Date().getHours();
let greeting;
//The if else Statement
if (hour < 18) {
    greeting = "Good day";
} else {
    greeting = "Good Evening";
}
console.log(greeting);
//The else if Statement
if (hour < 10 ){
    greeting = "Good Morning!";
} else if ( hour < 20 ) {
    greeting = "Good day";
} else {
    greeting = "Good evening";
}

console.log( greeting );

//JS Switch Statement
let day;
switch (new Date().getDay()) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
         day = "Wednesday";
         break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case  6:
        day = "Saturday";
    default:
        text = "Looking forward to the Weekend";
}

console.log( "Today is", + day );











































