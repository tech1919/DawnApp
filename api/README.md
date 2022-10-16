#Dawn API

This is and API for connecting the Dawn app to the mongoDB. The Dawn app is a Kivy based application.

The app using mainly get requests (with the UrlRequest kivy function) to access this API and by that to the mongoDB.

#Setting the API

This API is deployed on Heroku.

Deploy Steps:

1.
2.
3.
4.

#Routes

/signuser :
expecting a user dictionary with the fields:
* first_name
* last_name
* username
* email
* password
* height
* weight

This route add new user to the DB

/verifyuser: 
This route checking if a user is in the DB. If it
does, the response will be the data of the user. If the 
user is not in the database, the response will be False.

/updateuser: 
This route check is the username is in the DB, then update
his record with the fields given in the body of the request.