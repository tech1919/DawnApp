from kivy.uix.screenmanager import ScreenManager, Screen ,WipeTransition, FadeTransition , NoTransition , SlideTransition , FallOutTransition , RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.config import Config

# Config.set('kivy','window_icon','icon.ico')


class DemoProject(ScreenManager):
    pass


class DawnApp(MDApp):

    def go_to(self,screen_name):
        # saves the last screen before changing
        self.last_screen = self.root.current
        try:

            if screen_name == 'question':
                if self.last_screen == 'login':
                    self.root.transition = SlideTransition(direction='up')
                    self.username = self.root.ids.username_login.text
                    self.password = self.root.ids.password_login.text
                else:
                    self.root.transition = SlideTransition(direction='left')

                self.root.current = screen_name
            elif screen_name == 'question_details':
                self.root.transition = NoTransition()
                self.root.current = screen_name
            elif screen_name == 'profile':
                if self.last_screen == 'question_details':
                    self.weight = self.root.ids.weight_input.text
                    self.height = self.root.ids.height_input.text
                    self.change_text('weight_field',f'{self.weight} kg')
                    self.change_text('height_field', f'{self.height} cm')
                    self.root.current = screen_name
                else:
                    self.root.current = screen_name

            elif screen_name == 'next_question':
                try:
                    self.next_question()
                except:
                    screen_name = 'question_details'
                    self.root.current = screen_name
                    return

                # change the text in the page
                self.change_text(f'question_text', self.cur_question)
                self.change_text(f'question_number', f'QUESTION {self.cur_question_idx + 1} OF {self.number_of_questions}')

                try:
                    self.change_photo(f'question_img',f'Q{self.cur_question_idx + 1}.png')
                except:
                    self.change_photo(f'question_img', f'Q1.png')
                try:
                    self.change_photo(f'count',f'count_{self.cur_question_idx + 1}.png')
                except:
                    self.change_photo(f'count', f'count_9.png')

                self.root.ids[f'btn_yes'].source = 'button_yes.png'
                self.root.ids[f'btn_no'].source = 'button_no.png'

                # self.root.transition = SlideTransition(direction='left')



            elif screen_name == 'home':
                self.sizes()
                self.root.current = screen_name
            else:
                self.root.transition = NoTransition()
                self.root.current = screen_name



        except:
            self.root.current = 'profile'




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
                self.root.ids[f'btn_yes'].source = 'button_yes_p.png'
                self.root.ids[f'btn_no'].source = 'button_no.png'
            if(check == 'no'):
                self.root.ids[f'btn_yes'].source = 'button_yes.png'
                self.root.ids[f'btn_no'].source = 'button_no_p.png'
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
        self.cur_question_idx -= 2
        self.next_question()
        self.go_to('next_question')
    def changes(self,type):
        print(f'{type} Changes made')
        self.go_to('profile')

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

    def build(self):

        # set the first question in line
        self.next_question(first=True)


        Builder.load_file('classes.kv')
        Builder.load_file('question_details.kv')
        Builder.load_file('profile.kv')
        
        Builder.load_file('signup.kv')
        Builder.load_file('login.kv')


        Builder.load_file('signup.kv')
        Builder.load_file('loading.kv')

        Builder.load_file('question.kv')

        Builder.load_file('question_details_datepick.kv')

        Builder.load_file('profile.kv')
        Builder.load_file('profile_security.kv')
        Builder.load_file('profile_diagnoseMe.kv')


        Builder.load_file('home.kv')
        Builder.load_file('diagnose.kv')
        Builder.load_file('daily.kv')






        return DemoProject()




if __name__ == '__main__':
    DawnApp().run()
