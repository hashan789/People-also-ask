//open search method when click on it
function get_search_method(){
    var getSelectedValue = document.querySelector('input[name="search"]:checked').value;

    switch(getSelectedValue){
        case "google":
            document.getElementById("google_search").classList.remove('hide');
            document.getElementById("bing_search").classList.add('hide');
            break;
        case "bing":
            document.getElementById("bing_search").classList.remove('hide');
            document.getElementById("google_search").classList.add('hide');
            break;
    }

    console.log(getSelectedValue);
}
