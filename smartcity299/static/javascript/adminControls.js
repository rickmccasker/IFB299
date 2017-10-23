/**
Description: 
    Add a field to the related div, primarily used for adding a field to a form using the data to create databases or modify files.
Parameters: 
    N/A
Return: 
    Boolean - Return false in all cases simply to prevent form submission
**/
function addField() {

    var fieldName = document.getElementById("fieldName").value;

    if (document.getElementById(fieldName))
    {
        alert("This item already exists, please choose another name");
        return false;
    }
    var input = document.createElement("input");
    var button = document.createElement("button");
    var container = document.createElement("div");
    var form = document.getElementById("expansion")

    input.setAttribute("id", fieldName);
    input.setAttribute("name", fieldName);
    input.setAttribute("value", fieldName);
    input.setAttribute("readonly", true);
    button.innerHTML = "Delete"
    button.setAttribute("id", "delete_" + fieldName);
    button.setAttribute("onclick", "return removeField(this)");

    form.appendChild(container);
    container.appendChild(input);
    container.appendChild(button);

    return false
}

/**
Description: 
    Delete a field that was previously added when run.
Parameters: 
    Button - A button from the form. Using its ID the relevant field can be selected for deletion.
Return: 
    Boolean - Return false in all cases to prevent form submission
**/
function removeField(button) {
    button_id = button.id;
    field_id = button_id.replace("delete_", "");

    input_field = document.getElementById(field_id);
    
    container = input_field.parentElement;
    
    container.removeChild(button);
    container.removeChild(input_field);

    return false;
}