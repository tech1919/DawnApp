from kivy.uix.screenmanager import ScreenManager, Screen ,WipeTransition, FadeTransition , NoTransition , SlideTransition , FallOutTransition , RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import IRightBodyTouch
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem,OneLineListItem ,TwoLineListItem,ThreeLineListItem ,OneLineAvatarIconListItem ,ThreeLineAvatarIconListItem , IconLeftWidget , IconRightWidget
from kivy.uix.widget import Widget




class DemoProject(ScreenManager):
    pass


class DawnApp(MDApp):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 5)

    def change_ans(self , q_num):
        cur_ans = self.answers[q_num]
        if cur_ans == 'Yes':
            self.answers[q_num] = 'No'
        else:
            self.answers[q_num] = 'Yes'


    def create_scrollview(self):

        if self.first_scroll_view:
            self.first_scroll_view = False
        elif self.first_scroll_view == False:
            return

        screen = screen_manager.get_screen('profile_diagnoseMe')
        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)


        i = 0
        for c in self.questions:
            item = TwoLineListItem(
                text=c,
                secondary_text = self.answers[i],
                font_style='Caption',


            )



            i += 1
            ml.add_widget(item)

        screen.ids['diagnose_me'].add_widget(sv)

    def create_datepicker(self):
        screen = screen_manager.get_screen('question_details_datepick')
        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)

        for i in range(1,31):
            item = OneLineListItem(
                text = f'{i}',


            )
            ml.add_widget(item)




    def go_to(self,screen_name):
        # saves the last screen before changing


        try:
            if screen_name == 'back':
                screen_name = self.last_screen
        except:
            pass
        finally:
            if not self.last_screen == screen_name:
                self.last_screen = screen_manager.current


        # screen = screen_manager.get_screen(screen_name)

        try:

            if screen_name == 'question':
                if self.last_screen == 'login':
                    self.root.transition = SlideTransition(direction='up')
                    self.username = screen_manager.get_screen('login').ids.username_login.text
                    self.password = screen_manager.get_screen('login').ids.password_login.text
                else:
                    self.root.transition = SlideTransition(direction='left')

                screen_manager.current = screen_name
            elif screen_name == 'question_details':
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
            elif screen_name == 'question_details_datepick':
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
            elif screen_name == 'profile':

                if self.last_screen == 'question_details':
                    screen = screen_manager.get_screen('question_details')
                    self.weight = screen.ids.weight_input.text
                    self.height = screen.ids.height_input.text
                    self.change_text('weight_field',f'{self.weight} kg',screen_name)
                    self.change_text('height_field', f'{self.height} cm',screen_name)
                    screen_manager.current = screen_name
                else:
                    screen_manager.current = screen_name
            elif screen_name == 'profile_diagnoseMe' or screen_name == 'profile_security':
                screen = screen_manager.get_screen(screen_name)
                screen_manager.current = screen_name

                self.create_scrollview()


                screen.ids['profile_btn'].source = 'profile_p.png'



            elif screen_name == 'next_question' or screen_name == 'prev_question':


                screen_name = self.render_question(screen_name)





            elif screen_name == 'home':
                screen_manager.current = screen_name
            elif screen_name == 'login' or screen_name == 'signup':
                screen = self.getScreen(screen_name)
                screen.ids[f'username_{screen_name}'].text = ''
                screen.ids[f'password_{screen_name}'].text = ''
                if screen_name == 'signup':
                    screen.ids[f'email_{screen_name}'].text = ''
                screen_manager.current = screen_name
            else:
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
        except:
            pass
            # screen_manager.current = 'profile'

        self.change_navbar(screen_name)

    def hello(self,say_something):
        print(say_something)
    def google_login(self):
        print("Google login")
    def facebook_login(self):
        print("Facebook login")
    def forgot_password(self):
        print("forgot password")
    def profile_changes(self,check):
        print(f'{check} changes made')
    def on(self,check):
        screen_name = 'question'
        screen = screen_manager.get_screen(screen_name)

        try:
            if check == 'yes':
                self.answers[self.cur_question_idx] = 'Yes'
                screen.ids[f'no_btn'].md_bg_color =  get_color_from_hex("#FFFFFF")
                screen.ids[f'no_btn_label'].color = get_color_from_hex("#000000")
            elif check == 'no':
                self.answers[self.cur_question_idx] = 'No'
                screen.ids[f'yes_btn'].md_bg_color =  get_color_from_hex("#FFFFFF")
                screen.ids[f'yes_btn_label'].color = get_color_from_hex("#000000")
            elif check == 'reset':
                screen.ids[f'yes_btn'].md_bg_color =  get_color_from_hex("#FFFFFF")
                screen.ids[f'yes_btn_label'].color = get_color_from_hex("#000000")
                screen.ids[f'no_btn'].md_bg_color =  get_color_from_hex("#FFFFFF")
                screen.ids[f'no_btn_label'].color = get_color_from_hex("#000000")



            screen.ids[f'{check}_btn'].md_bg_color =  get_color_from_hex("#012241")
            screen.ids[f'{check}_btn_label'].color = get_color_from_hex("#FFFFFF")



        except:
            pass

    def render_question(self,operation):
        if self.last_screen == 'login' or self.last_screen == 'signup':
            self.cur_question_idx = 0

        screen_name = 'question'
        if operation == 'next_question':
            self.cur_question_idx += 1
        elif operation == 'prev_question' and self.cur_question_idx > 0:
            self.cur_question_idx -= 1

        if self.cur_question_idx >= self.number_of_questions:
            screen_name = 'question_details'
            screen_manager.current = screen_name
            return screen_name

        q_num = self.cur_question_idx

        self.cur_question_idx = q_num
        self.cur_question = self.questions[q_num]
        # change the text in the page
        self.change_text(f'question_text', self.cur_question, screen_name)
        self.change_text(f'question_number', f'QUESTION {self.cur_question_idx + 1} OF {self.number_of_questions}',
                         screen_name)
        try:
            self.change_photo(f'count', f'count_{self.cur_question_idx + 1}.png', screen_name)
        except:
            self.change_photo(f'count', f'count_9.png', screen_name)

        try:
            self.change_photo(f'question_img', f'Q{self.cur_question_idx + 1}.png', screen_name)
        except:
            self.change_photo(f'question_img', f'Q1.png', screen_name)

        self.on('reset')

        return screen_name

    def getScreen(self,screen_name):
        return screen_manager.get_screen(screen_name)
    def change_text(self, id , text , screen_name):
        # This function can change the text for a label in a given screen
        screen = screen_manager.get_screen(screen_name)
        screen.ids[id].text = text
    def change_photo(self, id , new_path , screen_name):
        # This function can change an image that has a id
        # in a given screen

        screen = screen_manager.get_screen(screen_name)
        screen.ids[id].source = new_path

    def first_question(self,first=False):
        # This function sets up the questions list and the answers dictionary

        self.questions = [
            'Can you now (or could you ever) place your hand flat on the floor without bending your knees?',
            'Can you now (or could you ever) bend your thumb to touch your forearm?',
            'As a child, did you amuse your friends by contorting your body into storage shapes or could you do the splits?',
            'As a child ot teenager, did your shoulder or kneecap dislocate on more than one occasion?',
            'Do you consider yourself "double jointed"?',
            'Unusually soft or velvety skin',
            'Mild skin hyperextensibility',
            'Unexplained striae distensae or rubae at the back, groins, thighs, breasts and/or abdomen in adolescents, men or pre-pubertal women without a history of significant gain or loss of body fat orweight',
            'Bilateral piezogenic papules of the heel',
            'Recurrent or multiple abdominal hernia(s)',
            'Atrophic scarring involving at least nwo sites and without the formation of truly papyraceous and/or hemosideric scars as seen in classical EDS ',
            'Pelvic floor, rectal, and/or uterine prolapse in children, men or nulliparous women without a history of morbid obesity or other known '
            + 'predisposing medical condition',
            'Dental crowding and high or narrow palate',
            'Arachnodactyly, as defined in one or more of the following:' +
            '(1) positive wrist sign (Walker sign) on both sides, (2) positive thumb sign (Steinberg sign) on both sides',
            'Arm span-to-height ratio =1.05',
            'Mitral valve prolapse (MVP) mild or greater based on strict echocardiographic criteria',
            'Aortic root dilatation with Z-score >+2',
            'Musculoskeletal pain in two or more limbs, recurring daily for at least 3 months',
            'Chronic, widespread pain for 3 months or more',
            'Recurrent joint dislocations or frank joint instability, in the absence of trauma'
        ]
        if first:
            self.answers = {}
            # first question
            self.cur_question_idx = 0
            self.number_of_questions = len(self.questions)
            for i in range(0, self.number_of_questions):
                self.answers[i] = 'No'

        self.cur_question = self.questions[self.cur_question_idx]
    def change_navbar(self,screen_name):
        # This function controls the bottom navigation bar
        # for a given screen_name, the funtion will switch the
        # source of the photo for the navbar to the right one for this screen

        images_ids = ['home','daily','diagnose','profile']
        flag = False
        for id in images_ids:
            if id == screen_name:
                flag = True
                break

        if not flag:
            return


        screen = screen_manager.get_screen(screen_name)
        for id in images_ids:
            screen.ids[f'{id}_btn'].source = f'{id}.png'

        screen.ids[f'{screen_name}_btn'].source = f'{screen_name}_p.png'
    def build(self):

        # set the first question in line
        global screen_manager

        self.first_scroll_view = True
        self.icon = 'app_logo.png'
        self.first_question(first=True)
        self.last_screen = 'login'

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('profile.kv'))
        screen_manager.add_widget(Builder.load_file('signup.kv'))
        screen_manager.add_widget(Builder.load_file('daily.kv'))
        screen_manager.add_widget(Builder.load_file('home.kv'))
        screen_manager.add_widget(Builder.load_file('profile_diagnoseMe.kv'))
        screen_manager.add_widget(Builder.load_file('profile_security.kv'))
        screen_manager.add_widget(Builder.load_file('diagnose.kv'))
        screen_manager.add_widget(Builder.load_file('question.kv'))
        screen_manager.add_widget(Builder.load_file('question_details.kv'))
        screen_manager.add_widget(Builder.load_file('question_details_datepick.kv'))




        return screen_manager
        # return DemoProject()
    def on_start(self):
        # This function waits for 3 seconds in the presplash screen
        # until switching to the login screen
        Clock.schedule_once(self.login , 3)
    def login(self,*args):
        screen_manager.current = "login"


if __name__ == '__main__':
    DawnApp().run()
