from kivy.uix.screenmanager import ScreenManager, Screen ,WipeTransition, FadeTransition , NoTransition , SlideTransition , FallOutTransition , RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

# Config.set('kivy','window_icon','icon.ico')

class DemoProject(ScreenManager):
    pass


class DawnApp(MDApp):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 5)

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
            elif screen_name == 'question_details' or screen_name == 'question_details_datepick':
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
                screen.ids['profile_btn'].source = 'profile_p.png'
            elif screen_name == 'next_question':
                screen_name = 'question'
                try:
                    self.next_question()
                except:
                    screen_name = 'question_details'
                    screen_manager.current = screen_name
                    return


                # change the text in the page
                self.change_text(f'question_text', self.cur_question,screen_name)
                self.change_text(f'question_number', f'QUESTION {self.cur_question_idx + 1} OF {self.number_of_questions}',screen_name)
                try:
                    self.change_photo(f'count',f'count_{self.cur_question_idx + 1}.png',screen_name)
                except:
                    self.change_photo(f'count', f'count_9.png',screen_name)

                try:
                    self.change_photo(f'question_img',f'Q{self.cur_question_idx + 1}.png',screen_name)
                except:
                    self.change_photo(f'question_img', f'Q1.png',screen_name)

                self.on('reset')
                # self.root.transition = SlideTransition(direction='left')
            elif screen_name == 'home':
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
    def on(self,check):
        screen_name = 'question'
        screen = screen_manager.get_screen(screen_name)

        try:
            if check == 'yes':

                screen.ids[f'no_btn'].md_bg_color =  get_color_from_hex("#FFFFFF")
                screen.ids[f'no_btn_label'].color = get_color_from_hex("#000000")
            elif check == 'no':
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



    def change_text(self, id , text , screen_name):
        screen = screen_manager.get_screen(screen_name)
        screen.ids[id].text = text
    def change_photo(self, id , new_path , screen_name):
        screen = screen_manager.get_screen(screen_name)
        screen.ids[id].source = new_path
    def profile_changes(self,type):
        print(f'{type} Changes made')
    def next_question(self,first=False):
        questions = [
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
            'Atrophic scarring involving at least nwo sites and without the formation of truly papyraceous and/or hemosideric scars as seen in classical EDS '
            + 'Pelvic floor, rectal, and/or uterine prolapse in children, men or nulliparous women without a history of morbid obesity or other known '
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
        self.number_of_questions = len(questions)
        if first:
            # first question
            self.cur_question_idx = 0
        else:

            self.cur_question_idx += 1

        self.cur_question = questions[self.cur_question_idx]

    def change_navbar(self,screen_name):


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

        self.icon = 'app_logo.png'
        self.next_question(first=True)
        self.last_screen = 'login'

        screen_manager = ScreenManager()
        # screen_manager.add_widget(Builder.load_file('loading.kv'))
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

        # Builder.load_file('classes.kv')
        # Builder.load_file('loading.kv')
        # Builder.load_file('login.kv')
        # Builder.load_file('daily.kv')
        # Builder.load_file('home.kv')
        # Builder.load_file('profile.kv')
        # Builder.load_file('profile_diagnoseMe.kv')
        # Builder.load_file('diagnose.kv')
        # Builder.load_file('question_details.kv')
        # Builder.load_file('question.kv')
        # Builder.load_file('signup.kv')
        # Builder.load_file('question_details_datepick.kv')
        # Builder.load_file('profile_security.kv')



        return screen_manager
        # return DemoProject()

    def on_start(self):
        Clock.schedule_once(self.login , 5)

    def login(self,*args):
        screen_manager.current = "profile"


if __name__ == '__main__':
    DawnApp().run()
