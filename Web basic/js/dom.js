//DOM-The Document Object Model (DOM)
//is a programming interface for web documents that allows programs to change a document's structure, style, and content.

//****DOM Manipulation*****
//Selecting with id -->document.getElementById
let heading = document.getElementById("heading");// If id element was not exist then it will print null.
console.dir(heading);
let button = document.getElementById("myId");// If id element was not exist then it will print null.
console.dir(button);

//Selecting with class-->document.getElementsByClassName("myClass")
let headings = document.getElementsByClassName("heading-class");// If class element not exist then it will print empty html collection.
console.dir(headings);
console.log(headings);

//Selecting with tag-->document.getElementsByTagName("p")
let parahs = document.getElementsByTagName("p");
console.dir(parahs);

//Query Selector-->document.querySelector("")------------It returns first element
let firstEl = document.querySelector("p"); //It will return 1st element
console.dir(firstEl);

//document.querySelectorAll("myId/myClass/tag")
let allEl = document.querySelectorAll("p"); //It will return all matching element
console.dir(allEl);

let allEl1 = document.querySelectorAll(".heading-class");
console.dir(allEl1);


let firstEL1 = document.querySelector("#heading");
console.dir(firstEL1);

//********PROPERTIES(to access the elements and change their value******************
//tagName : returns tag for element nodes

//innerText : returns the text content of the element and all its children
const changePara = document.getElementById("para");
changePara.innerText = "New para";

//innerHTML : returns the plain text or HTML contents in the element
//textContent : returns textual content even for hidden elements.


//**********Attributes*******************
//getAttribute(attr)-->to get the attribute value
let div = document.querySelector("div")
console.log(div);

let id = div.getAttribute("id");
console.log(id);

//setAttribute(attr, value)//to set attribute value
let id1 = div.setAttribute("id", "box1");
console.log(id1);


//***********Style***********8

//node.style