// Get the input field
var input = document.getElementsById("id_name", "new-item");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a clickname
    document.getElementById("btn btn-info").click();
  }
});
