
// $(function(){
//   $("#header").load("./header.html"); 
//   $("#footer").load("./footer.html"); 
// });


/* Fuction to control tabs */
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    /* Hide all all the tabs */
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    /* get all the tab links */
    tablinks = document.getElementsByClassName("tablinks");
    /* deactivate all of them */
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    /* Display the tab passed into the code */
    document.getElementById(tabName).style.display = "block";
    /* set its class to active for proper rendering */
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();