
from kivy.network.urlrequest import UrlRequest
import urllib


endpoint = 'http://localhost:3000/'

def getData(query):
    '''
        This function will return the first match from the database, according
        to the query object

        the query variable is an json object that contains the field to look by
        and the values to look
        example:
        user_to_find = {
            'first_name': 'Ofry',
            'last_name': 'Makdasy',
            'username': 'ofryma'
        }

    '''


    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}users?{params}')
    req.wait()

    return req.result
def login_check(query):
    '''
       This function will verify the login details (username and password)
       against the database, and will return True is the user is in the database
       and False if it is not
    '''

    params = urllib.parse.urlencode(query)



# def TEST_WEATHER_API():
#     '''
#         This function is here to check the INTERNET connection of the app
#         it called from the render_login_page and shows the weather description
#         in the username field in the login and signup pages.
#
#         This function is NOT relevant to the app and should be removed after
#         the check is done
#
#     '''
#
#     test = 'https://api.openweathermap.org/data/2.5/weather?q=באר שבע, חיים נחמן ביאליק 3&appid=c0d8f4929cdcdf553d6e9298178ae058&units=metric'
#     x = UrlRequest(f'https://api.openweathermap.org/data/2.5/weather?q=באר שבע, חיים נחמן ביאליק 3&appid=c0d8f4929cdcdf553d6e9298178ae058&units=metric')
#     x.wait()
#     print(x.result)
#     return x.result
