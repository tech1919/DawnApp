
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.utils import platform
from kivy.config import Config
from kivy.core.window import Window


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


class Manager(ScreenManager):
    pass

class DawnApp(MDApp):
    def build(self):

        if 'win' in platform.lower():
            print(platform)
            Window.size = (360, 650)


        self.images_source = 'assets/images/'
        self.kv_file_source = 'libs/uix/kv/'


        self.icon = self.images_source + 'app_logo.png'
        self.last_screen = 'profile'
        self.user = (User())
        question_sets = Question_sets()
        self.questions = question_sets.ads()




        sm = Manager()
        sm.add_widget(Builder.load_file(self.kv_file_source + 'newLogin.kv'))
        sm.add_widget(Builder.load_file(self.kv_file_source + 'newSignup.kv'))

        sm.add_widget(Builder.load_file(self.kv_file_source + 'newHome.kv'))
        sm.add_widget(Builder.load_file(self.kv_file_source + 'newProfile.kv'))
        sm.add_widget(Builder.load_file(self.kv_file_source + 'newDiagnose.kv'))
        sm.add_widget(Builder.load_file(self.kv_file_source + 'newDaily.kv'))

        sm.add_widget(Builder.load_file(self.kv_file_source + 'newQuestion.kv'))


        return sm




    def go_to(self, screen_name):
        """
            This function is switching between screens
            some screen require extra care with animations
            transitions or timing
        """
        if self.root.current == screen_name:
            return

        if screen_name == 'back':
            screen_name = self.last_screen

        # save the last screen
        self.last_screen = self.root.current

        # print(f'Current Screen: {screen_name}')
        self.root.transition = NoTransition()
        self.root.current = screen_name

    def change_navbar(self,screen):
        print(screen)
        self.last_screen = self.root.current

if __name__ == '__main__':
    DawnApp().run()
