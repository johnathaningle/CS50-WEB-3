$(document).ready(function(){
    let rating = $("#rating-number").text();
    console.log(rating);
    var options = {
        max_value: 5,
        step_size: 0.5,
        selected_symbol_type: 'utf8_star',
        initial_value: rating,
        update_input_field_name: $("#rater"),
    }
    $("#rate").rate(options);

});