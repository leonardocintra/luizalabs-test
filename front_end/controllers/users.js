module.exports = function(app) {
  var UserController = {
    index: function(req, res) {
      res.render('users/index');
    },
    new: function(req, res) {
      res.render('users/form', {
        id: null
      });
    },
    edit: function(req, res) {
      var _id = req.params.id;

      res.render('users/form', {
        id: _id
      });
    },
  }
  return UserController;
};
