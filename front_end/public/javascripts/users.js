API_URL = "http://127.0.0.1:7030/api/";
API_USER_URL = API_URL + "/user";

new Vue({
  el: "#users",
  data: {
    user: null,
    users: [],
    prev: null,
    next: null,
    pages: 1,
    current: null
  },
  events: {
    'hook:ready': function() {
      var self = this;
      self.list(1);
    },
  },
  methods: {
    list: function(page) {
      var self = this,
          resp = null,
          url = API_URL + "users?page=" + page;

      var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "method": "GET",
        "dataType": "json",
        "headers": {}
      };
      jQuery.ajax(settings)
        .done(function (resp) {
          self.users = resp.objects;
          self.next = resp.next;
          self.prev = resp.prev;
          self.pages = resp.pages;
          self.current = resp.current;
      });
    },
    delete: function(item) {
        console.log(item.el.detached());

        var self = this,
          resp = null,
          url = API_USER_URL + "/" + item.pk;

      /*
      var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "method": "DELETE",
        "dataType": "json",
        "headers": {}
      };
      jQuery.ajax(settings).done(function (resp) {

      }); */
    }
  }
});
