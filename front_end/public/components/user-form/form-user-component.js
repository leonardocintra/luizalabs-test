Vue.component('form-user-component', {
  el: "#form-user-component",
  template: './form.html',
  data: function() {
    return {
      user: {
        id: null,
        fb_id: null,
        username: '',
        name: '',
        gender: '',
        birthday: null
      },
      userExists: false
    }
  },
  filters: { },
  methods: {
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
      if (self.user.id) {
        return self.put(self.user.id);
      } else {
        return self.create();
      }
    },
    create: function(e) {
      e.preventDefault();
      var self = this,
        settings = self.settings;

      settings.url = API_USER_URL;
      settings.type = "POST";
      settings.data = {'fb_id': self.user.fb_id};
      jQuery.ajax(settings)
        .done(function(data) {
          self.user = data;
          window.location = '/users/' + data.id + '/edit';
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
          console.log(jqXHR.statusCode);
          if (jqXHR.status == 404) {
            self.messages.fb_id = "Usuário não encontrado informe um ID válido.";
          } else if (jqXHR.status == 428) {
            self.messages.fb_id = "Informe um Facebook ID válido.";
          }
        });
    },
    update: function(pk) { },
  }
});
