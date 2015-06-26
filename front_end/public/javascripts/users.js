API_URL = "http://127.0.0.1:9080/api/";
API_USER_URL = API_URL + "users/";
API_FACEBOOK_URL = API_URL + "facebook/";

new Vue({
  el: "#users",
  data: {
    isList: false,
    userExists: false,
    searchText: "",
    query: {
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
    objUser: {
      id: null,
      fb_id: null,
      username: "",
      name: "",
      gender: "",
      birthday: null,
    },
    messages: {
      error: "",
      success: ""
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

      if (window.location.pathname == '/users/') {
        self.list(1);
      };
    },
  },
  filters: {
  },
  methods: {
    list: function(page, search) {
      var self = this,
      settings = self.settings
      url = API_USER_URL + "?page=" + page;

      if (search) {
        url += "&search=" + search;
      };

      settings.url = url;
      jQuery.ajax(settings).done(function (resp) {
        self.query = resp;
        self.isList = true;
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
    search: function() {
      var self = this;
      this.list(1, self.searchText);
    },
    submit: function(e) {
      e.preventDefault();
      var self = this;

      if (self.user.id) {
        self.update(self.user.id);
      } else {
        self.create();
      }
    },
    create: function() {
      var self = this,
      settings = self.settings;

      settings.url = API_USER_URL;
      settings.type = "POST";
      settings.data = self.user;

      jQuery.ajax(settings)
      .done(function(data) {
        self.user = self.objUser;;
        self.userExists = false;
        self.messages.success = "Usuário cadastrado com sucesso.";
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        if (jqXHR.status != 400) {
          self.messages.error = "Usuário já registrado em nossa base de dados.";
        };
      });
    },
    edit: function(item) {
      var self = this;
      self.detail(item.id);
      self.userExists = true;
      self.isList = false;
    },
    update: function(id) {
      var self = this,
      url = API_USER_URL + id;

      var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "type": "PUT",
        "contentType": "application/json; charset=utf-8",
        "dataType": "json",
        "mimeType": "multipart/form-data",
        "data": self.user
      };
      jQuery.ajax(settings).done(function(resp) {
        console.log(resp);
      });
    },
    delete: function(item) {
      var self = this,
      url = API_USER_URL + item.id;

      var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "method": "DELETE",
        "headers": {}
      };

      jQuery.ajax(settings).fail(function(jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
      });
    },
    getFacebookUser: function(e) {
      e.preventDefault();
      var self = this,
      settings = self.settings,
      url = API_FACEBOOK_URL + self.user.fb_id;

      settings.url = url;
      jQuery.ajax(settings).done(function(data) {
        self.user.id = null;
        self.user.fb_id = data.id;
        self.user.username = data.username;
        self.user.name = data.name;
        self.user.gender = data.gender;
        self.user.birthday = data.birthday;

        self.messages.success = "";
        self.messages.error = "";
        self.userExists = true;
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        var status = jqXHR.status;
        if (status == 428) {
          self.messages.validID = "Facebook ID é obrigatório."
        } else if (status == 404) {
          self.messages.error = "Usuário não encontrado. Informe um ID válido."
        }
      });
    },
    cancel: function(e) {
      e.preventDefault();
      var self = this;

      self.user = self.objUser;
      self.userExists = false;
      self.isList = true;

      self.messages.success = "";
      self.messages.error = "";
    }
  }
});
