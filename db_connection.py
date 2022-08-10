from kivy.network.urlrequest import UrlRequest
import urllib


endpoint = 'https://dawnapi.herokuapp.com/'

# for tests
# endpoint = 'http://localhost:3000/'

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
    req = UrlRequest(f'{endpoint}test')
    req.wait()
    return req.result

def add_patient(sign_user):
    query = sign_user.user_info(get_object=True)
    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}signuser?{params}')
    req.wait()
    print(req.result)
    return req.result

def verify_patient(query):
    '''
       This function will verify the login details (username and password)
       against the database, and will return True is the user is in the database
       and False if it is not
    '''


    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}verifyuser?{params}')
    req.wait()
    # print(req.result)
    return req.result

def update_patient(query,update_fields):



    query = {**query, **update_fields}

    query['answers'] = ','.join(query['answers'])
    # query['diagnose'] = ','.join(query['diagnose'])
    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}updateuser?{params}')
    req.wait()
    # print(req.result)
    return req.result