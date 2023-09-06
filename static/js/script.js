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


/** Function to display and hide the comments in the news detail */

document.getElementById('toggle-comments').addEventListener('click', function () {
  var commentsBox = document.getElementById('comments-box');

  if (commentsBox.style.display === 'none') {
      commentsBox.style.display = 'block';
      this.innerText = 'Hide Comments';
  } else {
      commentsBox.style.display = 'none';
      this.innerText = 'View Comments';
  }
});