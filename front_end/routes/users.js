module.exports = function(app) {

  var user = app.controllers.users;

  app.get('/', user.index);
  app.get('/new', user.new);
  app.get('/:id/edit/', user.edit);
};
