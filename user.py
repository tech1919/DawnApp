from datetime import date, datetime

class Date:
    def __init__(self , day = '' , month = '', year = ''):
        self.day = day
        self.month = month
        self.year = year
    def month_name(self):
        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        return month_list[self.month - 1]
    def dob(self):
        try:
            d = f'{self.day} {self.month_name()}, {self.year}'
        except:
            d = '-'
        return d
class Question:
    def __init__(self, number, question, answer):
        self.q_number = number
        self.question = question
        self.answer = answer
class User:

    def __init__(self, height, weight, dob, first, last, username, password, email=''):
        self.height = height
        self.weight = weight
        self.date_of_birth = dob
        self.first_name = first
        self.last_name = last
        self.username = username
        self.password = password
        self.email = email
        self.diagnose = []

    def create_diagnose(self, q_arr, a_arr):
        num = 1
        for q, a in zip(q_arr, a_arr):
            self.diagnose.append([num, q, a])
            num += 1

    def user_info(self):

        # print()
        # print(f'    First name: {self.first_name}')
        # print(f'    Last name: {self.last_name}')
        # print(f'    Username: {self.username}')
        # print(f'    Email: {self.email}')
        # print(f'    Password: {self.password}')
        # print(f'    Date of birth: {self.date_of_birth}')
        # print(f'    Height: {self.height} , Weight: {self.weight}')
        # print()

        user_json_object = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'height': self.height,
            'weight': self.weight
            # 'date_of_birth': self.date_of_birth,


        }
        return user_json_object

def date_validation_1(date_string):
    test_format = '04-01-1997'
    # initializing format
    format = "%d-%m-%Y"
    # checking if format matches the date
    res = True
    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(test_format, format))
    except ValueError:
        res = False

    return res
def number_validatin(string):
    try:
        int(string)
        return True
    except:
        return False
