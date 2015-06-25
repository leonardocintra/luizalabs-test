API_URL = "http://127.0.0.1:8080/api/";
API_USER_URL = API_URL + "user/";

new Vue({
  el: "#users",
  data: {
    users: {
      objects: [],
      prev: null,
      next: null,
      pages: 1,
      current: null
    },
    user: {
      id: null,
      fb_id: null,
      username: "",
      name: "",
      gender: "",
      birthday: null,
    },
    settings: {
      async: true,
      crossDomain: true,
      url: "",
      data: null,
      type: "GET",
      dataType: "json",
      headers: {}
    },
  },
  events: {
    "hook:ready": function() {
      var self = this;

      if (self.user.id) {
        self.detail(self.user.id);
      } else{
        self.list(1);
      }
    },
  },
  filters: {
  },
  methods: {
    list: function(page, search) {
      var self = this,
      settings = self.settings
      resp = null,
      url = API_URL + "users/?page=" + page;
      if (search) {
        url += "&search=" + search;
      };

      settings.url = url;
      jQuery.ajax(settings).done(function (resp) {
        self.users = resp;
      });
    },
    detail: function(id) {
      var self = this,
      settings = self.settings,
      url = API_USER_URL + id;

      settings.url = url;
      jQuery.ajax(settings).done(function (resp) {
        self.user = resp;
      });
    },
    submit: function(e) {
      e.preventDefault();
      var self = this;

      if (!self.user.id) {
        self.post();
      } else {
        self.put(self.user.id);
      }
    },
    post: function() {
      var self = this,
      settings = self.settings;

      settings.url = API_USER_URL;
      settings.type = "POST";
      settings.data = self.user;
      jQuery.ajax(settings).done(function(data) {
        self.user = data;
      });
    },
    put: function(id) {
      var self = this,
      settings = self.settings;

      settings.url = API_USER_URL + id;
      settings.type = "PUT";
      settings.data = self.user;
      jQuery.ajax(settings).done(function(data) {
        self.user = data;
      });
    },
    delete: function(item) {
      var self = this,
      settings = self.settings,
      resp = null,
      url = API_USER_URL + item.id;

      settings.url = url;
      settings.type = "DELETE";
      jQuery.ajax(settings).done(function (resp) {
        if (resp.status == 204) {
          self.list(self.users.page);
        };
      });
    }
  }
});
