from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen ,WipeTransition, FadeTransition , NoTransition , SlideTransition , FallOutTransition , RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.config import Config
import json
import time

Config.set('kivy','window_icon','icon.ico')


class ProfileScreen(Screen):
    pass


class LoadingScreen(Screen):
    pass


class SignScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class Question(Screen):
    pass

class DemoProject(ScreenManager):
    pass


class DawnApp(MDApp):

    def go_to(self,screen_name):
        # saves the last screen before changing

        self.last_screen = self.root.current
        try:
            if self.last_screen == 'login':
                self.root.transition = SlideTransition(direction='up')
            elif screen_name == 'next_question':
                self.next_question()
                self.change_text(f'question{self.cur_question_idx + 1}', self.cur_question)
                self.change_text(f'Q_number_{self.cur_question_idx + 1}', f'QUESTION {self.cur_question_idx + 1} OF {self.number_of_questions}')
                # self.change_photo(f'img_Q{self.cur_question_idx + 1}',f'Q{self.cur_question_idx + 1}.png')
                self.change_photo(f'count{self.cur_question_idx + 1}',f'count_{self.cur_question_idx + 1}.png')

                self.root.transition = SlideTransition(direction='left')
                screen_name = f'question{self.cur_question_idx + 1}'
            elif screen_name == 'home':
                self.sizes()
            else:
                self.root.transition = NoTransition()


            self.root.current = screen_name
        except:
            self.root.current = 'profile'
    def load_app(self):

        self.go_to('login')
    def hello(self,say_something):
        print(say_something)
    def google_login(self):
        print("Google login")
    def facebook_login(self):
        print("Facebook login")
    def forgot_password(self):
        print("forgot password")
    def on(self,check):
        try:
            if(check == 'yes'):
                self.root.ids[f'btn_yes_{self.cur_question_idx + 1}'].source = 'button_yes_p.png'
                self.root.ids[f'btn_no_{self.cur_question_idx + 1}'].source = 'button_no.png'
            if(check == 'no'):
                self.root.ids[f'btn_yes_{self.cur_question_idx + 1}'].source = 'button_yes.png'
                self.root.ids[f'btn_no_{self.cur_question_idx + 1}'].source = 'button_no_p.png'
        except:
            pass



    def change_text(self, id , text):
        self.root.ids[id].text = text
    def change_photo(self, id , new_path):
        self.root.ids[id].source = new_path
    def sizes(self):
        # Home Screen
        big_logos = 140
        logos_ids = ['blood_test_logo','diagnose_logo','symptoms_logo','doctor_logo']
        for id in logos_ids:
            self.root.ids[id].width = big_logos
            self.root.ids[id].height = big_logos

    def back(self):
        self.root.transition = SlideTransition(direction='right')
        temp_last_screen = self.root.current
        self.root.current = self.last_screen
        self.last_screen = temp_last_screen


    def next_question(self,first=False):
        questions = [
            'Can you now (or could you ever) place your hand flat on the floor without bending your knees?',
            'Write your details',
            'Can you now (or could you ever) bend your thumb to touch your forearm?',
            'As a child, did you amuse your friends by contorting your body into storage shapes or could you do the splits?',
            'As a child ot teenager, did your shoulder or kneecap dislocate on more than one occasion?',
            'Do you consider yourself "double jointed"?'
        ]
        self.number_of_questions = len(questions)
        if first:
            # first question
            self.cur_question_idx = 0
        else:

            self.cur_question_idx += 1

        self.cur_question = questions[self.cur_question_idx]



    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "DeepOrange"
        self.last_screen = 'loading'
        self.next_question(first=True)
        Builder.load_file('home.kv')
        Builder.load_file('login.kv')

        Builder.load_file('diagnose.kv')
        Builder.load_file('profile.kv')
        Builder.load_file('loading.kv')
        Builder.load_file('question.kv')
        Builder.load_file('question_details.kv')
        Builder.load_file('question3.kv')
        Builder.load_file('question4.kv')
        Builder.load_file('question5.kv')
        Builder.load_file('signup.kv')
        Builder.load_file('daily.kv')


        return DemoProject()




if __name__ == '__main__':
    DawnApp().run()
