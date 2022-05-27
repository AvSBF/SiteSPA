$(document).ready(function() {
   $('.burger').click(function() {
       $('.burger').toggleClass('burger-active');
       $('.navbar-menu').toggleClass('navbar-menu-active');
   });
});