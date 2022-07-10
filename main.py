from kivy.uix.screenmanager import ScreenManager, Screen ,WipeTransition, FadeTransition , NoTransition , SlideTransition , FallOutTransition , RiseInTransition
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivymd.uix.picker import MDDatePicker
from kivymd.app import MDApp
from kivy.core.window import Window
from datetime import date , datetime


from kivymd.uix.list import MDList, TwoLineAvatarIconListItem,OneLineListItem ,TwoLineListItem,ThreeLineListItem ,OneLineAvatarIconListItem ,ThreeLineAvatarIconListItem , IconLeftWidget , IconRightWidget
import os.path

def getDay():
    return (date.today().strftime("%A, %d %B, %Y"))

class User:
    def __init__(self , height , weight , dob , first , last, username , password):
        self.height = height
        self.weight = weight
        self.date_of_birth = dob
        self.first_name = first
        self.last_name = last
        self.username = username
        self.password = password
class DemoProject(ScreenManager):
    pass
class DawnApp(MDApp):
################################# LOGIN\SIGUP PAGE ######################################
    def hello(self,say_something):
        print(say_something)
    def google_login(self):
        print("Google login")
    def facebook_login(self):
        print("Facebook login")
    def forgot_password(self):
        print("forgot password")
    def login(self,*args):
        screen_manager.current = "login"
    def render_login_signup_page(self , screen_name):
        screen = self.getScreen(screen_name)
        screen.ids[f'username_{screen_name}'].text = ''
        screen.ids[f'password_{screen_name}'].text = ''
        if screen_name == 'signup':
            screen.ids[f'email_{screen_name}'].text = ''
        screen_manager.current = screen_name
#########################################################################################
################################# PROFILE PAGE ##########################################
    def profile_changes(self,check):
        print(f'{check} changes made')
    def create_scrollview(self):
    # This function create a scroll view for the profile_diagnoseMe page
    # It uses the self.answers dictionary and displays the questions and the answers
    # of the user in the profile_diagnoseMe page

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
    def render_profile_page(self):
        screen_name = 'profile'
        if self.last_screen == 'question_details':
            screen = screen_manager.get_screen('question_details')
            user.weight = screen.ids.weight_input.text
            user.height = screen.ids.height_input.text

        self.change_text('first-last_name', f'{user.first_name} {user.last_name}', screen_name)
        self.change_text('first_name', f'{user.first_name}', screen_name)
        self.change_text('last_name', f'{user.last_name}', screen_name)
        self.change_text('weight', f'{user.weight} kg', screen_name)
        self.change_text('height', f'{user.height} cm', screen_name)
        self.change_text('date_of_birth', f'{user.date_of_birth}', screen_name)
        screen_manager.current = screen_name
    def on_save(self ,instance , value , date_range):
        month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']


        screen = self.getScreen('question_details')
        day = value.day
        month = value.month
        month_name = month_list[month-1]
        year = value.year
        dob = f'{day} - {month_name} - {year}'
        user.date_of_birth = value
        screen.ids['date_of_birth'].text = dob
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_sfave = self.on_save)
        date_dialog.open()
#########################################################################################
################################# DIAGNOSE FUNCTIONS ####################################
    def diagnose(self ,*args):
        self.root.transition = FadeTransition()
        screen = self.getScreen('diagnose')
        screen.ids['date_diagnose'].text = getDay()
        screen_manager.current = "diagnose"
        self.root.transition = NoTransition()
#########################################################################################
################################# QUESTION PAGE #########################################
    def on(self,check):
        # This function controls the buttons in the question page

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

        # if the app go to a question page from a login or signup page
        # the question current number need to reset for starting over
        if self.last_screen == 'login' or self.last_screen == 'signup':
            self.cur_question_idx = 0

        screen_name = 'question'

        # this operations comes from the user's buttons in the question page
        if operation == 'next_question':
            self.cur_question_idx += 1
        elif operation == 'prev_question' and self.cur_question_idx > 0:
            self.cur_question_idx -= 1

        # if the user finished all of the questions
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

        # This part switch the count number at the top of the question page
        # to activate simply uncomment this part down here and the part in the question.kv
        # file with the id of 'count_{number}'

        # try:
        #     self.change_photo(f'count', f'count_{self.cur_question_idx + 1}.png', screen_name)
        # except:
        #     self.change_photo(f'count', f'count_9.png', screen_name)


        # check if there is an image for the current question
        file_exists = os.path.exists(f'Q{self.cur_question_idx + 1}.png')
        if file_exists:
            self.change_photo(f'question_img', f'Q{self.cur_question_idx + 1}.png', screen_name)
        else:
            self.change_photo(f'question_img', f'Q1.png', screen_name)


        # reset the buttons
        self.on('reset')

        return screen_name
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
    def change_ans(self , q_num):
        #### NOT WORKING ###
        # Function for changing the answer for a certain question from the profile page

        cur_ans = self.answers[q_num]
        if cur_ans == 'Yes':
            self.answers[q_num] = 'No'
        else:
            self.answers[q_num] = 'Yes'
#########################################################################################
################################# HOME PAGE #############################################
    def render_home_page(self):
        screen_manager.current = 'home'
#########################################################################################
################################# GENERAL FUNCTIONS #####################################
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
    def change_navbar(self,screen_name):
        # This function controls the bottom navigation bar
        # for a given screen_name, the funtion will switch the
        # source of the photo for the navbar to the right one for this screen

        images_ids = ['home','daily','diagnose','profile']
        flag = False
        for id in images_ids:
            if id == screen_name or screen_name == "presplash_diagnose":
                flag = True
                break

        if not flag:
            return


        screen = screen_manager.get_screen(screen_name)
        for id in images_ids:
            screen.ids[f'{id}_btn'].source = f'{id}.png'

        screen.ids[f'{screen_name}_btn'].source = f'{screen_name}_p.png'
    def go_to(self,screen_name):
        # saves the last screen before changing
        self.root.transition = NoTransition()
        try:
            if screen_name == 'back':
                self.root.transition = SlideTransition(direction="right")
                screen_name = self.last_screen
        except:
            pass
        finally:
            if not self.last_screen == screen_name:
                self.last_screen = screen_manager.current


        # screen = self.getScreen(screen_name)

        try:

            if screen_name == 'question_details':
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
            elif screen_name == 'home':
                screen = self.getScreen(screen_name)
                screen.ids['hello-first_name'].text = f'Hello {user.first_name}'
                screen_manager.current = screen_name
            elif screen_name == 'question_details_datepick':
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
            elif screen_name == 'diagnose' or screen_name == 'presplash_diagnose':
                screen_manager.current = 'presplash_diagnose'
                Clock.schedule_once(self.diagnose, 2)
            elif screen_name == 'profile':
                self.render_profile_page()
            elif screen_name == 'profile_diagnoseMe' or screen_name == 'profile_security':
                screen = screen_manager.get_screen(screen_name)
                screen_manager.current = screen_name
                self.create_scrollview()
                screen.ids['profile_btn'].source = 'profile_p.png'
            elif screen_name == 'next_question' or screen_name == 'prev_question' or screen_name == 'question':
                if self.last_screen == 'login':
                    self.root.transition = SlideTransition(direction='up')

                    # saves the username and password to the user class
                    user.username = screen_manager.get_screen('login').ids.username_login.text
                    user.password = screen_manager.get_screen('login').ids.password_login.text
                if self.last_screen == 'question_details' and screen_name == 'prev_question':
                    self.root.transition = SlideTransition(direction='right')
                elif self.last_screen == 'home':
                    self.cur_question_idx = 0
                else:
                    self.root.transition = SlideTransition(direction='left')



                screen_name = self.render_question(screen_name)
                screen_manager.current = screen_name
            elif screen_name == 'home':
                self.render_home_page()
            elif screen_name == 'login' or screen_name == 'signup':
                self.render_login_signup_page(screen_name)
            else:
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
        except:
            # in case on an error, the app go to profile page
            print(f'error in {screen_name}')
            screen_manager.current = 'profile'

        self.change_navbar(screen_name)
#########################################################################################
################################# BUILD FUNCTIONS #######################################
    def build(self):

        # set the first question in line
        global screen_manager
        global user

        user = User('-','-','-','Dana','Cohen','-','-')

        Window.clearcolor = get_color_from_hex("#F5E5D6")
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
        screen_manager.add_widget(Builder.load_file('presplash_diagnose.kv'))
        screen_manager.add_widget(Builder.load_file('question.kv'))
        screen_manager.add_widget(Builder.load_file('question_details.kv'))
        screen_manager.add_widget(Builder.load_file('question_details_datepick.kv'))


        return screen_manager
    def on_start(self):
        # This function waits for 3 seconds in the presplash screen
        # until switching to the login screen

        Clock.schedule_once(self.login , 3)
#########################################################################################
if __name__ == '__main__':
    DawnApp().run()
