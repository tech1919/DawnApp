
const express = require("express");
const https = require("https");
const request = require("request");
const bodyParser = require("body-parser");

const mongoose = require("mongoose");
const encrypt = require("mongoose-encryption");
const md5 = require("md5");

var fs = require('fs');
var path = require('path');
require('dotenv/config');
var multer = require('multer');

const app = express();
app.set('view engine', 'ejs');
app.use(express.static("public"))
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json())


// set up multer for storing uploaded files
var storage = multer.diskStorage({
	destination: (req, file, cb) => {
		cb(null, 'uploads')
	},
	filename: (req, file, cb) => {
		cb(null, file.fieldname + '-' + Date.now())
	}
});

var upload = multer({ storage: storage });


// DB setup
const database_name = "dawnAppDB";
mongoose.connect('mongodb+srv://dawn-user-01:dawn-password-01@cluster01.vlzzyf3.mongodb.net/' + database_name);


const userSchema = new mongoose.Schema({
  first_name: String,
  last_name: String,
  height: String,
  weight: String,
  username: String,
  date_of_birth: String,
  email: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  },
  questions: [String],
  answers: [String],
  diagnose: String,
  user_image: {
    data: Buffer,
    contentType: String
  }
});

// userSchema.plugin(encrypt,{secret: process.env.SECRET , encryptedFields: ["password"]});

const User = mongoose.model('User', userSchema);



app.get('/' , function(req,res){
  User.find({} , function(err , results){
    if(err){
      console.log(err);
    }else{
      res.render("uploadimage" , {
        Docs: results
      })
    }
  })
})
app.get('/signuser' , function(req,res){
  const newUser = req.query;
  // checking if any of the values from query is in the database_name


  // adding hash incription to the password and email address
  const sign_user = new User({
    first_name: newUser.first_name,
    last_name: newUser.last_name,
    username: newUser.username,
    email: newUser.email,
    password: newUser.password,
    height: newUser.height,
    weight: newUser.weight
  });

  // adding the new user to the database
  sign_user.save(function(err,results){
    if(err){
      // console.log(err);
      res.send(err);
    }
    else{
      console.log(results);
      // sending back the record
      res.send(results);
    }
  })

})
app.get('/verifyuser' , function(req,res){
  const verify_user = req.query;
  console.log(verify_user);
  User.findOne(verify_user,function(err,results){
    console.log(results);
    if(err){
      console.log(err);
      res.send(false);
    }
    else if (results == null) {
      res.send(false);
    }
    else{
      // console.log(results);
      res.send(results);
    }
  })

})
app.get('/updateuser' , function(req,res){
  const update_user = req.query;
  update_user.answers = update_user.answers.split(',')
  User.findOne({username: update_user.username},function(req,res){});
  User.updateOne({username: update_user.username},update_user,function(err , results){
    if(err){
      res.send(false);
    }
    else{
      console.log(results);
      res.send(true);
    }
  });
})



// test get requests
app.get('/deleteallusers' ,function(req,res){
  User.deleteMany(function(err){
    if(err){
      console.log(err);
      res.send(err)
    }else{
      let msg = 'All users have been deleted!';
      console.log(msg);
      res.send(msg)
    }
  })
})
app.get('/test1' , function(req,res){
  User.find(function(err,results){
    if(err){
      console.log(err);
      res.send(err);
    }else{
      console.log(results);
      res.send(results)
    }
  })
})
app.get("/addone",function(req,res){

  const newUser = new User({
    first_name: 'Ofry',
    last_name: 'Makdasy',
    height: 172,
    weight: 62,
    username: 'ofryma',
    date_of_birth: '20/11/1994',
    email: 'ofry60000@gmail.com',
    password: '2419',
    questions: [],
    diagnose: '',
  });

  newUser.save(function(err,results){
    if(err){
      console.log(err);
      res.send(err);
    }
    else{
      // console.log(results);
      res.send(results);
    }
  })
})
app.route("/users")
  .get(function(req,res){
    // gets all the data from the mongodb server
    const cur_query = req.query
    User.findOne({cur_query},function(err,results){
      if(err){
        res.send(err);
      }
      else{
        // console.log(results);
        res.send(results);
      }
    })
})



// listening to a dinamic port (for using heroku) and on our localhost at port 3000
app.listen(process.env.PORT || 3000,function(){
  console.log("Server is up and running");
});
