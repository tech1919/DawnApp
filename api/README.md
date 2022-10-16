#Dawn API

This is and API for connecting the Dawn app to the mongoDB. The Dawn app is a Kivy based application.

The app using mainly get requests (with the UrlRequest kivy function) to access this API and by that to the mongoDB.

#Setting the API

This API is deployed on Heroku.

Deploy Steps:

Step | Description
------|------------
1 | python requirements installation 
2 | creating a project using the api folder in this repo
3 | creating a mongoDB of users
4 | configuring the API and deploying on Heroku


#Routes

`/signuser` :
expecting a user dictionary with the fields:


```javascript
{
  "first_name" : "string",
  "last_name" : "string",
  "username" : "string",
  "kids" : 
  "email" : "string",
  "password" : "string",
  "height" : number,
  "weight" : number,
}
```

This route add new user to the DB

`/verifyuser`: 
This route checking if a user is in the DB. If it
does, the response will be the data of the user. If the 
user is not in the database, the response will be False.

`/updateuser`: 
This route check is the username is in the DB, then update
his record with the fields given in the body of the request.
