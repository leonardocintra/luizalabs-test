var express = require('express');
var load = require('express-load');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var app = express();
var server = require('http').createServer(app)
var port = process.env.PORT || 3000;

var error = require('./middleware/error');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// uncomment after placing your favicon in /public
//app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


// load modules
load('controllers')
    .then('routes')
    .into(app);


// error handlers
app.use(error.notFound);
app.use(error.serverError);


server.listen(port, function() {
  console.log("Listen http://127.0.0.1:3000/")
});

module.exports = app;
