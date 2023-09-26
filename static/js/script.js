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
