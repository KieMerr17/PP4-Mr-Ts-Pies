/**Background Opacity Scrolling function
 * Adjust the opacity shadowed over the background image in index.html */ 
const marketItems = document.getElementById('markets');
const marketScrollWidth = marketItems.scrollWidth;

$(window).scroll(function() {
    var scrollTop = $(this).scrollTop();
    var maxOpacity = 0.8; // maximum opacity value
    var minOpacity = 0.0; // minimum opacity value

    var opacity = maxOpacity - (scrollTop / ($(window).height() * 2)); // opacity based on the user's position
    
    if (opacity < minOpacity) { // ensure the opacity does not go below the minimum value
      opacity = minOpacity;
    }
    
    $('.overlay').css('background-color', 'rgba(0, 0, 0, ' + opacity + ')'); // update the background color opacity
});



/**Auto Scroll the market cards and stop when mouse over, 
 * continue scrolling on mouse out
 */
function autoScrollX() {
    const container = document.getElementById('markets');
    const scrollAmount = 1; // Adjust the scroll speed
    const scrollDelay = 20; // Adjust the scroll delay 
  
    // Add all features and append them to a container
    const featureItems = container.querySelectorAll('.feature-item');
    featureItems.forEach(function(item) {
        const clonedItem = item.cloneNode(true);
        container.appendChild(clonedItem);
    });
  
    // Start scrolling
    let scrollPosition = 0;
    const scrollInterval = setInterval(function() {
        container.scrollLeft += scrollAmount;
        scrollPosition += scrollAmount;
        if (scrollPosition >= container.scrollWidth) {
            container.scrollLeft = 0;
            scrollPosition = 0;
        }
    }, scrollDelay);
  
    // Stop scrolling when the mouse hovers over
    container.addEventListener('mouseover', function() {
        clearInterval(scrollInterval);
    });
  
    // Resume scrolling when the mouse leaves
    container.addEventListener('mouseout', function() {
        scrollInterval = setInterval(function() {
            container.scrollLeft += scrollAmount;
            scrollPosition += scrollAmount;
            if (scrollPosition >= container.scrollWidth) {
                container.scrollLeft = 0;
                scrollPosition = 0;
            }
        }, scrollDelay);
    });
}
  
// Start auto-scroll function
autoScrollX();
  