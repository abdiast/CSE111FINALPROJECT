// This function is called when the user submits the form
function submitForm() {
    // Get the user's input from the form
    var product = document.getElementById('product').value;

    // Store the user's input in a JavaScript file
    localStorage.setItem('product', product);

    // Redirect the user to the searchquery.html page
    window.location.href = 'searchquery';
    window.open('searchquery', '_self');
}

// This function is called when the page loads
function init() {
    // Check if the user's input is stored in localStorage
    var product = localStorage.getItem('product');
    if (product) {
        // If the user's input is stored, display it on the page
        var message = 'You have selected: ' + product;
        document.getElementById('message').innerHTML = message;
    }
}

// Add an event listener to call the init() function when the page loads
document.addEventListener('DOMContentLoaded', init);
