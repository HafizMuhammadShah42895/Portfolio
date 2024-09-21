// scripts.js
$(document).ready(function() {
    $('.navbar-toggler').click(function() {
        $(this).toggleClass('active');
        $('#navbarNav').slideToggle();
    });
});
