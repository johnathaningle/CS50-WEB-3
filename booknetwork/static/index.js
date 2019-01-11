window.onload = function () {
    document.getElementById('search-button').addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('search-results').style.display = "block";
        var searchValue = document.getElementById('search').value;
        console.log(searchValue);
        load_page(searchValue);

    });

    function load_page(text) {
        console.log('searching');
        const request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                data = this.responseText;
                console.log(data);
                return data;
            } 
        };
        request.open('GET', `/search/${text}`, true);
        request.send();
        
    }
};