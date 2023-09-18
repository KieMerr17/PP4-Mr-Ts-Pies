/**Background Opacity Scrolling function
 * Adjust the opacity shadowed over the background image in index.html */ 
const marketItems = document.getElementById('markets');

$(window).scroll(function() {
    var scrollTop = $(this).scrollTop();
    var maxOpacity = 0.9; // maximum opacity value
    var minOpacity = 0.4; // minimum opacity value

    var opacity = maxOpacity - (scrollTop / ($(window).height() * 2)); // opacity based on the user's position
    
    if (opacity < minOpacity) { // ensure the opacity does not go below the minimum value
      opacity = minOpacity;
    }
    
    $('.overlay').css('background-color', 'rgba(0, 0, 0, ' + opacity + ')'); // update the background color opacity
});
