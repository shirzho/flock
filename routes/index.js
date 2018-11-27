var express = require('express');
var router = express.Router();
// var bootstrap = require('bootstrap');
// require('bootstrap/dist/css/bootstrap.css');
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
