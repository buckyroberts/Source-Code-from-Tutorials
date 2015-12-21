$("#menu-toggle").click( function (e){
    e.preventDefault();
    $("#wrapper").toggleClass("menuDisplayed");
});


// This is just worthless JavaScript for demo purposes
var x = myFunction(4, 3);

function myFunction(a, b) {
    return a * b;
}