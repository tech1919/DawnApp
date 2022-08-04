
import time

from kivy.uix.screenmanager import ScreenManager, FadeTransition, NoTransition, SlideTransition, Screen
from kivymd.app import MDApp
from user import User
from Diagnostics import Question_sets

from libs.uix.kv.login import LoginScreen , LoginLayout
from libs.uix.kv.signup import SignupScreen, SignupLayout
from libs.uix.kv.profile import ProfileLayout , ProfileScreen
from libs.uix.kv.home import HomeScreen , HomeLayout
from libs.uix.kv.diagnose import DiagnoseLayout , DiagnoseScreen
from libs.uix.kv.daily import DailyLayout , DailyScreen
from libs.uix.kv.question import QuestionScreen , QuestionLayout
from libs.uix.components.navbar import Navbar
from libs.uix.components.topbar import Topbar


def delay(seconds):
    start = time.time()
    stop = time.time()
    while stop - start < seconds:
        stop = time.time()

class Manager(ScreenManager):
    pass



class DawnApp(MDApp):
    def build(self):
        images_source = 'assets/images/'
        self.icon = images_source + 'app_logo.png'
        self.last_screen = 'profile'
        self.user = (User())
        question_sets = Question_sets()
        self.questions = question_sets.ads()



        sm = Manager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(QuestionScreen(name='question'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(DiagnoseScreen(name='diagnose'))
        sm.add_widget(DailyScreen(name='daily'))

        return sm



    def go_to(self, screen_name):
        """
            This function is switching between screens
            some screen require extra care with animations
            transitions or timing
        """
        if self.root.current == screen_name:
            return
        # print(f'Current Screen: {screen_name}')
        self.root.transition = NoTransition()
        self.root.current = screen_name

    def change_navbar(self,screen):
        print(screen)
        self.last_screen = self.root.current



if __name__ == '__main__':
    DawnApp().run()
