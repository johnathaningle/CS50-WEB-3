document.addEventListener("DOMContentLoaded", function(e){
    var searchContentDiv = document.getElementById('search-results');
    document.getElementById('search-button').addEventListener('click', function(e) {
        e.preventDefault();
        searchContentDiv.style.display = "block";
        var searchValue = document.getElementById('search').value;
        //clear any existing search results
        searchContentDiv.innerHTML = "<h1>Search Results:</h1>";
        console.log(searchValue);
        load_page(searchValue);

    });

    function load_page(text) {
        console.log('searching');
        const request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                data = this.responseText;
                data = JSON.parse(data);
                console.log(data);
                isbn = data["data"].isbn;
                console.log(length);
                for (i = 0; i < data["data"].length; i++) {
                    let searchDiv = document.createElement('div');
                    searchDiv.className = "row content-section content-section-result pt-4 mt-4";
                    searchDiv.innerHTML = `<div class='col-md-3'><p><a href='/book/${data["data"][i].isbn}'>${data["data"][i].isbn}</a></p></div><div class='col-md-3'>${data["data"][i].author}</div><div class='col-md-3'>${data["data"][i].title}</div><div class='col-md-3'>${data["data"][i].year_published}</p></div>`;
                    searchContentDiv.appendChild(searchDiv);
                }
            } 
        };
        request.open('GET', `/search/${text}`, true);
        request.send(); 
    }
});
   
