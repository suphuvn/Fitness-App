var addButton = document.querySelectorAll('.add_button');

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

 function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

function addSet(event, button, exercise_id) {
    var container = button.parentNode.parentNode.parentNode.parentNode.querySelector(".sets_container");
    var sets = button.parentNode.parentNode.parentNode.querySelectorAll(".set_container");
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
                <input type="number" min="0" value="" id="reps`+ exercise_id + `" class="form-control reps`+ exercise_id + `"/>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <label for="reps`+ exercise_id + `" class="set_subtitle">reps</label>
            </div>
        </div>
    </div>
    <div class="col-sm-3 text-center">
        <p class="set_subtitle">*</p>
    </div>
    <div class="col-sm-3 text-center">
        <div class="row">
            <div class="col-sm-12">
                <input type="number" min="0" value="" id="weight`+ exercise_id + `" class="form-control weight`+ exercise_id + `"/>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <label for="weight`+ exercise_id + `" class="set_subtitle">lbs</label>
            </div>
        </div>
    </div>`;
    set.innerHTML = html;
    if (sets.length == 0) {
        container.insertBefore(set, button.parentNode.parentNode);
    } else {
        insertAfter(set, sets[sets.length-1]);
    }
}

function deleteSet(event, button) {
    var sets = button.parentNode.parentNode.parentNode.querySelectorAll(".set_container");
    sets[sets.length-1].parentNode.removeChild(sets[sets.length-1]);
}

 function addExercise(event, button) {
    var name = button.parentNode.parentNode.querySelector(".library_exercise_title").innerHTML;
    var exerciseBox = document.querySelector(".exercise_box");
    var exercises = document.querySelectorAll(".exercise_sets");
    var exercise_id = exercises.length;
    
    var exercise = document.createElement("div");
    exercise.setAttribute('class', "exercise_sets mb-2");
    exercise.setAttribute('id', exercise_id);

    exercise.innerHTML = 
    `<!-- Exercise Checkbox -->
        <input type="checkbox" id="` + exercise_id + `" name="exercise_checkbox" class="align-top mt-1"> 
        <!-- Exercise Sets (Checkbox 'label') -->
        <label for="`+ exercise_id + `" class="sets_container px-4 pt-2 mx-4 mb-0">
        <div class="row">
        <!-- Exercise Name -->
            <div class="col-sm-12">
                <p class="exercise_name noselect">` + name + `</p>
            </div>
        </div>
        <!-- Exercise Set -->
        <div id =0 class="row set_container">
            <div class="col-sm-3">
                <p class="set_num">SET 1</p>
            </div>
            <div class="col-sm-3 text-center">
                <div class="row">
                    <div class="col-sm-12">
                        <input type="number" min="0" value="" id="reps`+ exercise_id + `" class="form-control reps`+ exercise_id + `"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <label for="reps`+ exercise_id + `" class="set_subtitle">reps</label>
                    </div>
                </div>
            </div>
            <div class="col-sm-3 text-center">
                <p class="set_subtitle">*</p>
            </div>
            <div class="col-sm-3 text-center">
                <div class="row">
                    <div class="col-sm-12">
                        <input type="number" min="0" value="" id="weight`+ exercise_id + `" class="form-control weight`+ exercise_id + `"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <label for="weight`+ exercise_id + `" class="set_subtitle">lbs</label>
                    </div>
                </div>
            </div>
        </div>
        <!-- Add/Delete Set Buttons-->
        <div class="row mb-2">
            <div class="col-sm-6">
                <button id="add_button" class="set_button p-2">ADD SET</button>
            </div>
            <div class="col-sm-6">
                <button id="delete_button" class="set_button p-2">REMOVE SET</button>
            </div>
        </div>
    </label>`

    if (exercises.length == 0) {
        exerciseBox.appendChild(exercise)
    } else {
        insertAfter(exercise, exercises[exercises.length-1]);
    }

    var deleteSetButton = document.querySelectorAll("#delete_button");
    var addSetButton = document.querySelectorAll("#add_button");
    addSetButton[addSetButton.length - 1].addEventListener("click", function () { addSet(event, addSetButton[addSetButton.length-1], addSetButton[addSetButton.length-1].parentNode.parentNode.parentNode.parentNode.id); }, true);
    deleteSetButton[deleteSetButton.length - 1].addEventListener("click", function () { deleteSet(event, addSetButton[deleteSetButton.length-1]); }, true);
    $(document).on('change','.reps' + exercise_id, function(){
        $('.reps' + exercise_id).val($(this).val());
     });
    
    $(document).on('change','.weight' + exercise_id, function(){
        $('.weight' + exercise_id).val($(this).val());
     });
 }

 addButton.forEach(function (button) {
    button.addEventListener("click", function () { addExercise(event, button) }, true);
});