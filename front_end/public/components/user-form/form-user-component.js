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
      }
    }
  },
  filters: { },
  methods: {
    detail: function() { },
    post: function() { },
    put: function() { },
    delete: function() { },
  }
});
