from kivy.animation import Animation

"""
    Animations specially adapted for this application
"""

DICT_TYPE = type({'a':'b'})


SCROLL_DURATION = 0.2

def scroll_up_animation(screen, destination=0.5 , *args):
    """
        given a screen, this function will scroll the layout
        of the screen to a specific destination.
        !!! The layout must have a position (pos_hint) build in the kv file
        or else this function will do noting

        the offset is the calculation of bringing the position of the text field
        to the desired location on screen at height of 0.7

        how to use:
        1. Add self.pos = [0.5, 0.5] to screen class on_enter method
        2. from dawn_animations import scroll_up_animation
        3. Add scroll_layout method to the screen class
        4. Add pos_hint: {"center_x": 0.5 , "center_y": 0.5} to the layout on the kv file
        5. Call the scroll_layout function from any widget and give a destination or just a 0<position<1

        (see example on login screen - libs/uix/kv/login.py and libs/uix/kv/newLogin.kv)
    """

    if type(destination) == DICT_TYPE:
        destination = destination['center_y']

    if destination > 1:
        print(f'Error: on screen {screen} , destination given is: {destination}, and it must be less then 1')
        return
    if destination == 0.5:
        desired_pos = 0.5
        # print(f'scroll down screen {screen.name} to {desired_pos}')
    else:
        desired_pos = 0.6
        # print(f'scroll up screen {screen.name} to {desired_pos}')


    offset = desired_pos - destination

    layout = screen.children[0]

    animate = Animation(
        pos_hint={
            "center_x": 0.5,
            "center_y": 0.5 + offset
        },
        duration=SCROLL_DURATION
    )

    animate.start(layout)
