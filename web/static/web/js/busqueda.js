$(document).ready(function(){
    $("#busca").click(function(){
        $('.collapse').collapse("toggle");
        $('html, body').animate({scrollTop:0}, 1000);
        $("#busqueda").show("slow");
        $('#searchBox').focus();
    });
    $("#cruz").click(function(){
        $("#busqueda").hide("slow");
    });
});

