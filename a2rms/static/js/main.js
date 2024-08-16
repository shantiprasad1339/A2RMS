 
//////////////////////  aside naviteams dropshow   ////////////////
$(document).ready(function () {
    // jQuery for toggle sub menus
    $('.sub-btn').click(function () {
        // Check if the next sub-menu is already visible
        var $nextSubMenu = $(this).next('.sub-menu');
        
        // Slide up all sub-menus except the one that is clicked
        $('.sub-menu').not($nextSubMenu).slideUp();
        
        // Slide toggle the clicked sub-menu
        $nextSubMenu.slideToggle();
        
        // Toggle the rotation class
        $(this).find('.dropdown1').toggleClass('rotate');
    });
});


//////////////////////  aside naviteams dropshow   ////////////////

$('.aside_btn').click(function() {

	$('.main_area').addClass('full');
	$('aside ').addClass('inactive');
	$('.close-full ').addClass('active');

});
 
$('.close-full').click(function() {

	$('.main_area').removeClass('full');
	$('aside ').removeClass('inactive');
	$('.close-full ').removeClass('active');

});
 