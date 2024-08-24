const submitEl = document.getElementById("submit");
submitEl.addEventListener("click", () => {
    console.log("Hey");

    const isNameValid = !requiredValidation('name', 'nameError');
    var isEmailValid = !requiredValidation('email', 'emailError');
    isEmailValid = !emailValidation('email', 'emailError');
    const isPassValid = !requiredValidation('pass', 'passError');
    var isPhoneValid = !requiredValidation('phone', 'phoneError');
    isPhoneValid = !phoneValidation('phone', 'phoneError');
    const isAddressValid = !requiredValidation('address', 'addressError');
    if ( isNameValid && isEmailValid && isPassValid && isPhoneValid && isAddressValid){
        const formEl = document.getElementById('myForm');
        alert("Form submitted successfully");
        formEl.reset();
    }
});
function validateEmail(email){
  return String(email)
    .toLowerCase()
    .match(
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};

function emailValidation(id, errorId){
    const el = document.getElementById(id);
    const errorEl = document.getElementById(errorId);
    let isEmailValid = false;
    if ( !validateEmail(el.value.trim())){
        isEmailValid = true;
        errorEl.innerHTML = "Invalid email";
    }
    else{
        isEmailValid = false;
        errorEl.innerHTML = "";
    }
    return isEmailValid;
}

function phoneValidation(id, errorId){
    const el = document.getElementById(id);
    const errorEl = document.getElementById(errorId);
    let isPhoneValid = false;
    if ( el.value.trim().length < 10 ){
        isPhoneValid = true;
        errorEl.innerHTML = "Phone number should not be less than 10 digit";
    }else if ( el.value.trim().length > 10 ){
        isPhoneValid = true;
        errorEl.innerHTML = "Phone number should not be greater than 10 digit";
    }
    else{
        isPhoneValid = false;
        errorEl.innerHTML = "";
    }
    return isPhoneValid;
}

function requiredValidation(id, errorId) {
    const el = document.getElementById(id);
    const errorEl = document.getElementById(errorId);
    const isEmpty = el.value.trim().length == 0;
    if ( isEmpty ){
        errorEl.innerHTML = "This field is required";
    }
    else{
        errorEl.innerHTML = "";
    }
    return isEmpty;
}


//const el = document.getElementById("submit");
//function doSomething() {
//    console.log("I am submit");
//}
//
//el.addEventListener("click", doSomething);




//function myFunction(){
//var a = document.getElementById("name").value;
//var b = document.getElementById("email").value;
//var c = document.getElementById("pass").value;
//var d = document.getElementById("phone").value;
//var e = document.getElementById("website").value;
//var f = document.getElementById("company").value;
//var g = document.getElementById("address").value;
//
//
//
//if( a == "" || b == "" || c == "" || d == "")
//{
//    alert("All fields are required");
//    return false;
//
//}else if(d.length < 10 || d.length > 10)
//{
//    alert("Number should be of 10 digits! Please enter valid number");
//    return false;
//}
//else if(isNaN (d))
//{
//    alert("Only numbers are allowed! Please enter valid number");
//    return false;
//}
//else
//{
//    true;
//}
//
//}
//
//






















//function seterror(id, error){
//    //sets error inside the tag of id
//    element = document.getElementById(id);
//    element.getElementsByClassName('formerror')[0].innerHTML = error;
//
//        }
//
//function validateForm(){
//    var returnval = true;
//
//    var name = document.forms['myForm']["name"].value;
//    if (name.length == 0){
//        seterror("name", "*Length of name is too short");
//        returnval = false;
//
//    }
//
//        }

