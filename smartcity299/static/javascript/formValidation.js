/**
Description: 
    Function validates all input fields in a given form and prevents submission when errors detected, 
    displaying in respective error spans.
Parameters: 
    Form - HTML form containing inputs with "fieldName" attribute and error + "fieldName" spans.
Return: 
    Boolean - Return true when input fields are not empty, not all whitespace and satisfy all 
        requirements otherwise return false.
**/
function validateInput(form) {
    validSelectField(form);
    var inputs = form.getElementsByTagName('input');
    var errorCounter = 0;
    for (i = 0; i < inputs.length; i++)
    {
        if (inputs[i].id != '') { //Dont match the csrftoken
            var strError = "error" + inputs[i].id;
            document.getElementById(strError).innerHTML = "";
        }
        
        if (isEmpty(inputs[i])) {
            errorCounter += 5;
        }
        else
        {
            if(inputs[i].value.length > 0)
            {
                if (inputs[i].getAttribute("inputtype") == "letters" && !validAlphaChars(inputs[i]))
                {
                    errorCounter += 1;
                }
                else if (inputs[i].getAttribute("inputtype") == "numbers" && !validNumeralChars(inputs[i]))
                {
                    errorCounter += 1;
                }
                else if (inputs[i].getAttribute("inputtype") == "email" && !validEmailForm(inputs[i]))
                {
                errorCounter += 1;
                }
            }

        }

    }
    if (errorCounter > 0)
    {
        //alert("VALIDATION FAILED"); //Debugging purposes only
        return false;
    }
    else
    {
        //alert("VALIDATION SUCCESS"); //Debugging purposes only
        return true;
    }
    
}

/**
Description: 
    Function checks if all characters in inputs are valid alphabet chars and alters error information
Parameters: 
    input - An input field whose inputtype is "letters" to be validated
Return: 
    Boolean - Return true when input fields are all valid alphabet chars and false if otherwise
**/
function validAlphaChars(input){
    var alphaChar_regex = /^[A-z]+$/;
    if (!alphaChar_regex.test(input.value)) {
        document.getElementById("error" + input.id).innerHTML = "&nbsp*Please ensure only alphabet characters are used. <br>"
        return false
    }
    else
    {
        //alert("ALL ALPHABET") //Debugging purposes only
        return true
    }
}

/**
Description: 
    Function checks if all characters in inputs are valid numeric chars and alters error information
Parameters: 
    input - An input field whose inputtype is "numbers" to be validated
Return: 
    Boolean - Return true when input fields are all valid numeric chars and false if otherwise
**/
function validNumeralChars(input){
    var numericChar_regex = /^[0-9]+$/;
    if (!numericChar_regex.test(input.value)) {
        document.getElementById("error" + input.id).innerHTML = "&nbsp*Please ensure only numbers are used. <br>"
        return false
    }
    else {
        //alert("ALL numbers") //Debugging purposes only
        return true
    }
}

/**
Description: 
    Function checks if string obeys email form e.g. username@domain.com.au OR username@domain.com and alters error information
Parameters: 
    input - An input field whose inputtype is "email" to be validated
Return: 
    Boolean - Return true when input field is in valid form and false if otherwise
**/
function validEmailForm(input) {
    var email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!email_regex.test(input.value)) {
        document.getElementById("error" + input.id).innerHTML = "&nbsp*Please ensure correct email form is used (a@a.com). <br>"
        return false
    }
    else {
        //alert("CORRECT email form") //Debugging purposes only
        return true
    }
}

/**
Description: 
    Function checks if the select field in the formcontains some sort of value and if it doesn't alter error message accordingly
Parameters: 
    form - the entire form which should contain a select field
Return: 
    Boolean - Return true when a value is set and false if otherwise
**/
function validSelectField(form) {
    var inputs = document.getElementsByTagName("select");
    for(i=0; i<inputs.length; i++){
        var input = inputs[i];
        var strError = "error" + input.id;
        if (input.hasAttribute("fieldName")) { //fieldName attribute governs whether a field is compulsory or not
            if (input.options.length == 0 || input.value.length == 0) {
                document.getElementById(strError).innerHTML = "&nbsp*" + input.getAttribute("fieldName") + " field must not be empty. <br>";
                return false
            }
            else {
                document.getElementById(strError).innerHTML = "";
                return true
            }
        }
    }
}

/**
Description: 
    Function checks if input string is empty and alters error information
Parameters: 
    input - An input field which may or may not contain a char/string
Return: 
    Boolean - Return true when input field contains some char or string and false if otherwise
**/
function isEmpty(input) {
    var result = false
    var strError = "error" + input.id;
    if (input.hasAttribute("fieldName")) { //fieldName attribute governs whether a field is compulsory or not
        //alert(input.getAttribute("fieldName"));
        if (input.value.match(/^\s*$/) || input.value == '') {
            document.getElementById(strError).innerHTML = "&nbsp*" + input.getAttribute("fieldName") + " field must not be empty. <br>";
            result = true
        }
    }
    return result
}