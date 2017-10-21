function addField() {

    var fieldName = document.getElementById("fieldName").value;

    if (document.getElementById(fieldName)) {
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

function removeField(button) {
    button_id = button.id;
    field_id = button_id.replace("delete_", "");

    input_field = document.getElementById(field_id);
    
    container = input_field.parentElement;
    
    container.removeChild(button);
    container.removeChild(input_field);

    return false;
}