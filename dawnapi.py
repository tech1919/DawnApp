from kivy.network.urlrequest import UrlRequest
import urllib


endpoint = 'https://dawnapi.herokuapp.com/'
test_endpoint = 'http://localhost:3000/'

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
    # req = UrlRequest(f'{endpoint}test?{params}')
    req = UrlRequest(f'{endpoint}test')
    req.wait()

    return req.result
