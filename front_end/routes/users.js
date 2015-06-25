module.exports = function(app) {

  var user = app.controllers.users;

  app.get('/users/', user.index);
  app.get('/users/:id/edit/', user.edit);
};
