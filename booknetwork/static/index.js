document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('search-button').addEventListener("click", function(e){
        e.preventDefault();
        const request = new XMLHttpRequest();
        request.open("POST", "{{ url_for('search') }}")
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            console.log(data);
        }
        document.getElementById('search-results').style.display = "block";
    });
});