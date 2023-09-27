/**Background Opacity Scrolling function
 * Adjust the opacity shadowed over the background image in index.html */ 

function OverlayOpacity() {
  var scrollTop = window.scrollY || document.documentElement.scrollTop; // Get the current scroll position
  var maxOpacity = 0.9; // Maximum opacity value
  var minOpacity = 0.4; // Minimum opacity value

  // Calculate opacity based on the user's position
  var opacity = maxOpacity - (scrollTop / (window.innerHeight * 2));

  // Ensure the opacity does not go below the minimum value
  opacity = Math.max(opacity, minOpacity);

  // Update the background color with the class 'overlay'
  var overlayElements = document.querySelectorAll('.overlay');
  for (var i = 0; i < overlayElements.length; i++) {
      overlayElements[i].style.backgroundColor = 'rgba(0, 0, 0, ' + opacity + ')';
  }
}

// Attach the overlay function to the scroll event
window.addEventListener('scroll', OverlayOpacity);

// Call the function
OverlayOpacity();


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
