function testMessage() {
    alert("THE JAVASCRIPT FILE HAS BEEN Re/LOADED");
}

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
function validateInput(form){
    var inputs = form.getElementsByTagName('input');
    var errorCounter = 0;
    for (i = 0; i < inputs.length; i++)
    {
        var strError = "error" + inputs[i].id;
        if (inputs[i].hasAttribute("fieldName"))
        {
            document.getElementById(strError).innerHTML = "";
            if (inputs[i].value.match(/^\s*$/))
            {
                document.getElementById(strError).innerHTML = inputs[i].getAttribute("fieldName") + " field must not be empty. <br>";
                errorCounter += 1;
            }
        }
    }
    if (errorCounter > 0)
    {
        alert("VALIDATION FAILED"); //Debugging purposes only
        return false;
    }
    else
    {
        alert("VALIDATION SUCCESS"); //Debugging purposes only
        return true;
    }
    
}