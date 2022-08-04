from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from Diagnostics import diagnose_ads
from db_connection import update_patient


class QuestionScreen(Screen):
    def on_enter(self, *args):
        self.check_user_answers()
        self.clean_layout()

        layout = QuestionLayout()
        self.add_widget(layout)

        buttons_box = layout.children[0]
        question_label = layout.children[1]
        question_number = layout.children[2]
        question_image = layout.children[3]
        back_question_button = layout.children[4]
        back_question_button.bind(on_press=self.back_question)
        question_label.get_next_question()

    def check_user_answers(self):
        # set the answers field of the user
        user = App.get_running_app().user
        questions = App.get_running_app().questions

        if len(user.answers) == 0:
            for _ in questions:
                user.answers.append('')


    def back_question(self , *args):
        layout = self.children[0]
        question_label = layout.children[1]
        question_label.get_next_question('back')

    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

class QuestionLayout(MDFloatLayout):
    pass

class QButton(MDCard):
    pass

class YesButton(Button):

    def turn_button(self , state = ''):
        button_index = 2
        other_button_index = 1
        white = '#FFFFFF'
        black = '#000000'
        dark_blue = '#012241'

        button_card = self.parent
        buttons_box = button_card.parent
        other_button = buttons_box.children[other_button_index].children[0]
        other_button_card = other_button.parent


        try:
            if state == '':
                state = self.next_state

        except:
            state = 'ON'
        finally:
            if state.lower() == 'on' or state == 1 or state == True:
                # change color
                self.color = get_color_from_hex(white)
                button_card.md_bg_color = get_color_from_hex(dark_blue)


                # change color for the other button
                if other_button.color == [0.0, 0.0, 0.0, 1.0]:
                    pass
                else:
                    other_button.turn_button()

                # save state
                self.next_state = 'off'
                self.current_state = 'on'


            elif state.lower() == 'off' or state == 0 or state == False:
                # change color
                self.color = get_color_from_hex(black)
                button_card.md_bg_color = get_color_from_hex(white)
                # save state
                self.next_state = 'on'
                self.current_state = 'off'

class NoButton(Button):
    def turn_button(self, state=''):
        button_index = 1
        other_button_index = 2
        white = '#FFFFFF'
        black = '#000000'
        dark_blue = '#012241'
        button_box = self.parent

        button_card = self.parent
        buttons_box = button_card.parent
        other_button = buttons_box.children[other_button_index].children[0]
        other_button_card = other_button.parent

        try:
            if state == '':
                state = self.next_state

        except:
            state = 'ON'
        finally:
            if state.lower() == 'on' or state == 1 or state == True:
                # change color
                self.color = get_color_from_hex(white)
                button_card.md_bg_color = get_color_from_hex(dark_blue)

                # change state for the other button
                if other_button.color == [0.0, 0.0, 0.0, 1.0]:
                    pass
                else:
                    other_button.turn_button()


                # save state
                self.next_state = 'off'
                self.current_state = 'on'

            elif state.lower() == 'off' or state == 0 or state == False:
                # change color
                self.color = get_color_from_hex(black)
                button_box.md_bg_color = get_color_from_hex(white)
                # save state
                self.next_state = 'on'
                self.current_state = 'off'

class NextButton(Button):
    def next_question(self):

        button_card = self.parent
        buttons_box = button_card.parent
        button_index = {'yes_button' : 2 , 'no_button': 1 , 'next_button': 0}
        yes_button = buttons_box.children[button_index['yes_button']].children[0]
        no_button = buttons_box.children[button_index['no_button']].children[0]


        answer = ''

        # turn the buttons off
        # change color for the other button
        if not yes_button.color == [0.0, 0.0, 0.0, 1.0]:

            try:
                if yes_button.current_state == 'on':
                    answer = 'Yes'
                else:
                    answer = 'No'
            except:
                pass

            yes_button.turn_button()

        if not no_button.color == [0.0, 0.0, 0.0, 1.0]:

            try:
                if no_button.current_state == 'on':
                    answer = 'No'
                else:
                    answer = 'Yes'
            except:
                pass

            no_button.turn_button()


        layout = buttons_box.parent
        question_label = layout.children[1]
        question_image = layout.children[3]
        back_question_button = layout.children[4]

        # do something with the answer
        # this answer is for question index:
        question_index = question_label.current_question_index - 1
        user = App.get_running_app().user
        user.answers[question_index] = answer


        # set the next question
        question_label.get_next_question()

class QImage(Image):
    pass

class QNumber(MDLabel):
    pass

class QuestionLabel(MDLabel):
    def get_next_question(self, current_question_index = ''):
        question_set = App.get_running_app().questions
        user = App.get_running_app().user


        try:
            if current_question_index == 'back':
                current_question_index = self.current_question_index - 2
                if current_question_index == -1:
                    App.get_running_app().go_to('home')
                    self.current_question_index = 0
                    return
            if current_question_index == '':
                current_question_index = self.current_question_index
        except:
            current_question_index = 0
        finally:
            if current_question_index == len(question_set):
                App.get_running_app().go_to('profile')

                # use the answer to diagnose
                user.diagnose = diagnose_ads(user.answers)
                update_patient({'username':user.username},{'height': user.height,
                                                           'weight': user.weight,
                                                           "date_of_birth": user.date_of_birth,
                                                           "diagnose": user.diagnose,
                                                           'questions': user.answers})
                self.current_question_index = 0
                return
            current_question = question_set[current_question_index]
            self.text = current_question


            # change the number of question on screen
            layout = self.parent
            question_number = layout.children[2]
            question_number.text = f'Question {current_question_index + 1} of {len(question_set)}'

            # set the index for the next question
            self.current_question_index = current_question_index + 1

