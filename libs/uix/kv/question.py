from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout


class QuestionScreen(Screen):
    def on_enter(self, *args):
        layout = QuestionLayout()
        self.add_widget(layout)

    def back_question(self):
        print('back question')

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

        print(answer)