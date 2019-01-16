$(document).ready(function(){
    let rating = $("#rating-number").text();
    var options = {
        max_value: 5,
        step_size: 0.5,
        selected_symbol_type: 'utf8_star',
        initial_value: rating,
        update_input_field_name: $("#rater"),
    }
    $("#rate").rate(options);
    $("#add-review").click(function(){
        $("#review-box").toggle();
    });
    $("#cancel-review").click(function(){
        $("#review-box").toggle();
    });
});