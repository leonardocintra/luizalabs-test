API_URL = "http://127.0.0.1:8080/api/";
API_USER_LIST_URL = API_URL + "users";
API_USER_URL = API_URL + "user/";
API_FACEBOOK_URL = API_URL + "facebook/";

dateRE = /^\d{4}\-\d{1,2}\-\d{1,2}$/;
//dateRE = '/^\d{4}\/d{1,2}\/d{1,2}$/';

new Vue({
  el: "#users",
  events: {
    "hook:ready": function() {
      var self = this;

      if (window.location.pathname == '/users/') {
        self.list(1);
      };
    },
  },
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
    isFBLogged: false,
    user: {
      id: null,
      fb_id: null,
      username: "",
      name: "",
      gender: "",
      birthday: null,
    },
    newUser: {
      id: null,
      fb_id: null,
      username: "",
      name: "",
      gender: "",
      birthday: null,
    },
    validation: {
      name: false,
      gender: false,
      birthday: false
    },
    message: '',
    messages: {
      error: false,
      success: false,
      info: false
    },
    newMessages: {
      error: false,
      success: false,
      info: false
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
  filters: {
    nameValidator: function(val) {
      this.validation.name = !!val && !(val.length < 5);
      return val;
    },
    genderValidator: function(val) {
      this.validation.gender = !!val;
      return val;
    },
    birthdayValidator: function(val) {
      this.validation.birthday = dateRE.test(val);
      return val;
    },
  },
  computed: {
    isValid: function() {
      var valid = true;
      for (var key in this.validation) {
        if(!this.validation[key]) {
          valid = false;
        }
      }
      return valid;
    }
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
      });
      self.isList = true;
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

      if (this.isValid) {
        jQuery.ajax(settings)
        .done(function(data) {
          self.user = self.newUser;;
          self.isForm = false;
          self.message = "Usuário cadastrado com sucesso.";
          self.messages = self.newMessages;
          self.messages.success = true;
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
          if (jqXHR.status != 400) {
            self.message = "Usuário já registrado em nossa base de dados.";
            self.messages = self.newMessages;
            self.messages.error = true;
          };
        });
      };
    },
    edit: function(item, e) {
      e.preventDefault();
      var self = this;

      self.detail(item.id);
      self.isForm = true;
      self.isList = false;
      self.message = "";
      self.messages = self.newMessages;
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
            self.message = "Usuário cadastrado com sucesso.";
            self.messages = self.newMessages;
            self.messages.success = true;
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

        self.message = 'Usuário excluído com sucesso.';
        self.messages = self.newMessages;
        self.messages.info = true;
      });
    },
    cancel: function(e) {
      e.preventDefault();
      var self = this;

      self.user = self.newUser;
      self.isForm = false;
      self.isList = true;

      self.message = "";
      self.messages = self.newMessages;
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

        self.message = "";
        self.messages = self.newMessages;
        self.isForm = true;
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        var status = jqXHR.status;
        if (status == 428) {
          self.message = "Facebook ID é obrigatório."
          self.messages = self.newMessages;
          self.messages.info = true;
        } else if (status == 404) {
          self.message = "Usuário não encontrado. Informe um ID válido."
          self.messages = self.newMessages;
          self.messages.error = true;
        }
      });
    },
    fbLogin: function() {
      var self = this;
      self.message = '';
      self.messages = self.newMessages;

      jQuery.ajaxSetup({ cache: true });
      jQuery.getScript('//connect.facebook.net/en_US/sdk.js', function(){
        FB.init({
          appId: '896437553749930',
          version: 'v2.3'
        });
        FB.getLoginStatus(function(response) {
          if (response.status == 'connected') {
            self.getFBAPIuser(FB);
            self.isForm = true;
            self.isList = false;
          } else {
            FB.login(function(response) {
              if (response.status != "not_authorized") {
                self.getFBAPIuser(FB);
                self.isForm = true;
                self.isList = false;
              }
            });
          }
        });
      });
    },
    getFBAPIuser: function(FB) {
      var self = this;
      FB.api('/me', function(response) {
        self.user.fb_id = response.id;
        self.username = response.username;
        self.user.name = response.name;
        self.user.gender = response.gender;
        self.user.birthday = response.birthday;
      });
    }
  }
});
