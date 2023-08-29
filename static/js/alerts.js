/**Fade out animation for sign in/out success notifications on index.html */ 
const alertMessages = document.querySelectorAll(".alert-success");
setTimeout(function() {
  alertMessages.forEach(function(alertMessages) {
    alertMessages.style.animation = "fadeout 1s forwards";
  });
  // set fade out to 2 seconds
}, 2000);



/**Event listener for delete comment confirmation for comments
 * related to the user */ 
document.addEventListener("DOMContentLoaded", function() {
  const deleteContainers = document.querySelectorAll(".delete-container");

  deleteContainers.forEach(container => {
    // Select all variables
      const deleteButton = container.querySelector(".delete-comment");
      const confirmationDiv = container.querySelector(".confirmation");
      const confirmDeleteButton = container.querySelector(".confirm-delete");
      const cancelDeleteButton = container.querySelector(".cancel-delete");

      // Hide delete button and show confirmation event listeners
      deleteButton.addEventListener("click", function() {
          deleteButton.classList.add("hidden");
          confirmationDiv.classList.remove("hidden");
      });

      // hide confirmation if no
      cancelDeleteButton.addEventListener("click", function() {
          confirmationDiv.classList.add("hidden");
          deleteButton.classList.remove("hidden");
      });

      // submit form if yes
      confirmDeleteButton.addEventListener("click", function() {
          const form = container.querySelector(".delete-form");
          form.submit();
      });
  });
});