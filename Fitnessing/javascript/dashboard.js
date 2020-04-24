/*eslint-env browser*/
var filters = document.querySelectorAll(".filter_button");
var complete_button = document.querySelectorAll(".complete");
var sets = document.querySelectorAll(".set");
var deleteSetButton = document.querySelector("#delete_button");
var addSetButton = document.querySelector("#add_button");
var deleteExerciseButton = document.querySelector(".delete_button");
var closeModalButton = document.querySelector(".close");

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

function addSet(event, button) {
    var container = document.querySelector(".sets_container");
    var sets = document.querySelectorAll(".set_container");
    var set_id = sets.length;

    var set = document.createElement("div");
    set.setAttribute('id', set_id);
    set.setAttribute('class', "row set_container");
    var html = 
    `<div class="col-sm-3"> 
        <p class="set_num">SET ` + (set_id + 1) + `</p> 
    </div> 
    <div class="col-sm-3 text-center">
        <div class="row">
            <div class="col-sm-12">
                <input type="text" value="" id="reps" class="form-control"/>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <label for="reps" class="set_subtitle">reps</label>
            </div>
        </div>
    </div>
    <div class="col-sm-3 text-center">
        <p class="set_subtitle">*</p>
    </div>
    <div class="col-sm-3 text-center">
        <div class="row">
            <div class="col-sm-12">
                <input type="text" value="" id="weight" class="form-control"/>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <label for="weight" class="set_subtitle">lbs</label>
            </div>
        </div>
    </div>`;
    set.innerHTML = html;
    if (set_id == 0) {
        insertAfter(set, document.querySelector(".exercise_name").parentNode.parentNode);
    } else {
        insertAfter(set, sets[sets.length-1]);
    }
}

function deleteSet(event) {
    var sets = document.querySelectorAll(".set_container");
    sets[sets.length-1].parentNode.removeChild(sets[sets.length-1]);
}

function deleteExercise(event) {
    var exercises = document.getElementsByName("exercise_checkbox");
    
    for (var i = 0; i < exercises.length; i++) {
        if (exercises[i].checked) {
            var id = exercises[i].id;
            jQuery(function($) {
                $('label[for=' + id + ']').remove();
            }); 
            exercises[i].parentNode.removeChild(exercises[i]);
       }
    }
}

function addExercise(event) {
    
}

$(document).ready(function(){
    /* Get iframe src attribute value i.e. YouTube video url
    and store it in a variable */
    var url = $("#video").attr('src');
    
    /* Assign empty url value to the iframe src attribute when
    modal hide, which stop the video playing */
    $("#detailsModal").on('hide.bs.modal', function(){
        $("#video").attr('src', '');
    });
    
    /* Assign the initially stored url back to the iframe src
    attribute when modal is displayed again */
    $("#detailsModal").on('show.bs.modal', function(){
        $("#video").attr('src', url);
    });
});

filters.forEach(function (filter) {
    filter.addEventListener("click", function () { toggleSelected(event, filter); }, true);
});

complete_button.forEach(function (button) {
    button.addEventListener("click", function () { markComplete(event, button.parentNode.parentNode.parentNode); }, true);
});

sets.forEach(function (set) {
    set.addEventListener("click", function () { completed(event, set); }, true);
});

deleteSetButton.addEventListener("click", function () { deleteSet(event); }, true);
addSetButton.addEventListener("click", function () { addSet(event, add_button); }, true);
deleteExerciseButton.addEventListener("click", function() {deleteExercise(event); }, true)

getURL();