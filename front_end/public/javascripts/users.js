new Vue({
    el: '#list-users',
    data: {
        users: [],
        prev: null,
        next: null,
        pages: null
    }
});


var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:3040/api/users",
  "method": "GET",
  "headers": {}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});