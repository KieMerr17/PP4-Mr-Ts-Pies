(function() {
    //https://dashboard.emailjs.com/admin/account
    emailjs.init("BPkIdauGmKxEeEMKL");
})();
  
// Connect the form elements
var form = document.getElementById('contact-form');
var submitButton = form.querySelector('[type="submit"]');
var submitting = document.getElementById('submitting');

// Send form data after user submits
form.addEventListener('submit', function(event) {
    event.preventDefault();
  
    // Generate a five digit reference number
    this.contact_number.value = Math.floor(Math.random() * 100000);
  
    // Hide the submit button and show the submitting
    submitButton.style.display = 'none';
    submitting.style.display = '';
  
    // Function to animate dots while waiting for form submission
    function animateDots() {
        var dots = '';
        var count = 0;
        setInterval(function() {
            dots += '.';
            count++;
            if (count > 3) {
                dots = '';
                count = 0;
            }
            document.querySelector('.loading-dots').textContent = dots;
        }, 500);
    }
    animateDots();
  
    /**Use the values from the emailJS form template to send to emailJS
     * Following sending of the form, alerts displayed dependant on result.
     **/

    emailjs.sendForm('contact_service', 'contact_form', this).then(function() {
        console.log('Contact SUCCESS!');
        // Clear the form after submitting
        form.reset();
        // Hide the submitting element
        submitting.style.display = 'none';
        // Show the submit button again
        submitButton.style.display = 'inline-block';
        alert("Thank you for getting in touch!");

    }, function(error) {
        console.log('Contact FAILED...', error);
        // Show the submit button again
        submitButton.style.display = '';
        // Hide the submitting element
        submitting.style.display = 'none';
    });
    
});