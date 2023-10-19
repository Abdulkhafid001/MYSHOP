// on the app i want to add a feature to show all tasks completed and pending so i am using tabs to create that
// create a function to show the current clicked tab
function showCurrentTab(evt, taskStage) {
    // Declare all variables
    var i, tabContent, tabLinks;
    // Get all elements with class="tabcontent" and hide them
    tabContent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
    // Get all elements with class="tablinks" and remove the class "active"
    tabLinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tabLinks.length; i++) {
        tabLinks[i].className = tabLinks[i].className.replace(" active", "");
    }
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(taskStage).style.display = "block";
    evt.currentTarget.className += " active";
}