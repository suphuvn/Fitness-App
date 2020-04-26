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

$(document).on('change','.reps', function(){
    $('.reps').val($(this).val());
 });

 $(document).on('change','.weight', function(){
    $('.weight').val($(this).val());
 });