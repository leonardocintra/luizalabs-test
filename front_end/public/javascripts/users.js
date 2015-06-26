API_URL = "http://127.0.0.1:8080/api/";
API_USER_LIST_URL = API_URL + "users";
API_USER_URL = API_URL + "users/";
API_FACEBOOK_URL = API_URL + "facebook/";

new Vue({
  el: "#users",
  data: {
    isList: false,
    isForm: false,
    searchText: "",
    query: {
      objects: [],
      prev: null,
      next: null,
      pages: null,
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
      url = API_USER_LIST_URL + "?page=" + page;

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
        return self.update(self.user, e);
      } else {
        return self.create();
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
        self.isForm = false;
        self.messages.success = "Usuário cadastrado com sucesso.";
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        if (jqXHR.status != 400) {
          self.messages.error = "Usuário já registrado em nossa base de dados.";
        };
      });
    },
    edit: function(item, e) {
      e.preventDefault();
      var self = this;

      self.detail(item.id);
      self.isForm = true;
      self.isList = false;
      self.messages.success = "";
    },
    update: function(user, e) {
      e.preventDefault();
      var self = this,
      url = API_USER_URL + user.id;

      jQuery.ajax({
        "async": true,
        "crossDomain": true,
        "url": url,
        "type": "PUT",
        "dataType": "json",
        "contentType": "application/json",
        "mimeType": "multipart/forma-data",
        "headers": {"X-HTTP-Method-Override": "PUT"},
        "data": self.user,
        "statusCode": {
          200: function(resp) {
            self.messages.success = "Usuário cadastrado com sucesso.";
            self.isForm = false;
            self.isList = true;
            self.list(self.query.current);
          }
        }
      });
    },
    delete: function(item, e) {
      e.preventDefault();

      var self = this,
      url = API_USER_URL + item.id;

      var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "type": "DELETE"
      };
      jQuery.ajax(settings).done(function(resp) {
        jQuery('tr.item-' + item.id).addClass('bg-danger').fadeOut(800);
        setInterval(function() {
          jQuery('tr.item-' + item.id).remove()
        }, 1000);
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
        self.isForm = true;
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
      self.isForm = false;
      self.isList = true;

      self.messages.success = "";
      self.messages.error = "";
    }
  }
});
