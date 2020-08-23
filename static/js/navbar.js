$(document).ready(function(){
    $('.navbar-nav a').click(function(){
        $('a').removeClass("active");
        $(this).addClass("active");
    })
})