//DOM-The Document Object Model (DOM)
//is a programming interface for web documents that allows programs to change a document's structure, style, and content.

//****DOM Manipulation*****
//Selecting with id -->document.getElementById
let heading = document.getElementById("heading");// If id element was not exist then it will print null.
console.dir(heading);

//Selecting with class-->document.getElementsByClassName("myClass")
let headings = document.getElementsByClassName("heading-class");// If class element not exist then it will print empty html collection.
console.dir(headings);
console.log(headings);

//Selecting with tag-->document.getElementsByTagName("p")

//Query Selector-->document.querySelector("")------------It returns first element

//document.querySelectorAll("myId/myClass/tag")

