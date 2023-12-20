function validateForm() {
    if (document.forms["myForm"]["email"].value == "") {
        alert("Email must be filled out");
        return false;
    }
    else if (document.forms["myForm"]["fname"].value == "") {
        alert("Name must be filled out");
        return false;
    }
    else if (document.forms["myForm"]["subject"].value == "") {
        alert("Message must be written");
        return false;
    }
    else {
        alert("Your message has been sent");
        return true;
    }
  }