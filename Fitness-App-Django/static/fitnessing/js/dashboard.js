/*eslint-env browser*/
var filters = document.querySelectorAll(".filter_button");
var complete_button = document.querySelectorAll(".complete");
var sets = document.querySelectorAll(".set");

var deleteExerciseButton = document.querySelector(".delete_button");
var closeModalButton = document.querySelector(".close");
var applyButton = document.querySelector('.apply_button');

function setBackground(element) {
    "use strict";
    element.style.backgroundImage = "url('Images/Tab.svg')";
    element.style.backgroundRepeat = "no-repeat";
    element.style.backgroundPosition = "right center";
    element.style.backgroundSize = "100px 130px";
}

function getURL() {
    "use strict";
    var pathname = window.document.location.pathname;
    var curr;
    
    if (pathname.endsWith("/home.html")) {
        curr = document.querySelector(".link1");
        setBackground(curr);
        document.querySelector(".home").src = "images/Home Icon.svg";
        document.querySelector(".workouts").src = "images/Weight Icon.svg";
        document.querySelector(".stats").src = "images/Bar Chart Icon.svg";
    } else if (pathname.endsWith("/workouts.html") || pathname.endsWith("/currentworkout.html") || pathname.endsWith("/createworkout.html")) {
        curr = document.querySelector(".link2");
        setBackground(curr);
        document.querySelector(".workouts").src = "images/Weight Icon - Purple.svg";
        document.querySelector(".home").src = "images/Home Icon - White.svg";
        document.querySelector(".stats").src = "images/Bar Chart Icon.svg";

    } else if (pathname.endsWith("/stats.html")) {
        curr = document.querySelector(".link3");
        setBackground(curr);
        document.querySelector(".stats").src = "images/Bar Chart Icon - Purple.svg";
        document.querySelector(".workouts").src = "images/Weight Icon.svg";
        document.querySelector(".home").src = "images/Home Icon - White.svg";
    }
}

function toggleSelected(event, element) {
    if (element.classList.contains("selected")) {
        element.classList.remove("selected");
    } else {
        element.classList.add("selected");
    }
}

function markComplete(event, buttonParent) {
    var sets = buttonParent.querySelectorAll(".set");
    var i;
    for (i = 0; i < sets.length; ++i) {
        var check = sets[i].querySelector(".check");
        check.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/2/27/White_check.svg')"
        check.style.backgroundRepeat = "no-repeat"
        check.style.backgroundSize = "contain"
        sets[i].style.backgroundColor = "rgba(255, 255, 255, 0.5)";
      }
}

function completed (event, set) {
    var check = set.querySelector(".check");
    if (check.style.backgroundImage != ""){
        check.style.background = "none"
        check.style.backgroundImage = ""
        set.style.backgroundColor = "transparent";
    } else {
        check.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/2/27/White_check.svg')"
        check.style.backgroundRepeat = "no-repeat"
        check.style.backgroundSize = "contain"
        set.style.backgroundColor = "rgba(255, 255, 255, 0.5)";
    }
}

function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

function deleteExercise(event) {
    var exercises = document.getElementsByName("exercise_checkbox");
    var remove = []
    
    for (var i = 0; i < exercises.length; i++) {
        if (exercises[i].checked) {
            remove.push(exercises[i]);
       }
    }
    
    for (var i = 0; i < remove.length; i++) {
        remove[i].parentNode.remove();
    }
}

function filterWorkout(event) {
    var muscles = [];
    for (var i = 0; i < filters.length; i++) {
        if (filters[i].classList.contains("selected")) {
            muscles.push(filters[i].value);
            filters[i].classList.remove("selected");
        }
    }
    let data = {
        muscle: muscles
    };
    if (muscles.length == 0) {
        window.location.href = "/workouts";
    } else {
        window.location.href = "?" + $.param(data, true);
    }
}

filters.forEach(function (filter) {
    filter.addEventListener("click", function () { toggleSelected(event, filter); }, true);
});

complete_button.forEach(function (button) {
    button.addEventListener("click", function () { markComplete(event, button.parentNode.parentNode.parentNode); }, true);
});

sets.forEach(function (set) {
    set.addEventListener("click", function () { completed(event, set); }, true);
});

applyButton.addEventListener("click", function() {filterWorkout(event); }, true)
deleteExerciseButton.addEventListener("click", function() {deleteExercise(event); }, true)


getURL();