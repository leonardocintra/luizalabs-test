exports.notFound = function(req, res, next) {
    res.status(404);
    res.render('not-found');
};

exports.serverError = function(err, req, res, next) {
    res.status(500);
    console.log(err.stack);
    res.render('server-error', {error: err});
};