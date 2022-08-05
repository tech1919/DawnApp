from kivy.animation import Animation

"""
    Animations specially adapted for this application
"""


SCROLL_DURATION = 0.2

def scroll_up_animation(screen, destination=0.5 , *args):
    """
        given a screen, this function will scroll the layout
        of the screen to a specific destination.
        !!! The layout must have a position (pos_hint) build in the kv file
        or else this function will do noting

    """

    if destination > 1:
        print(f'Error: on screen {screen} , destination given is: {destination}, and it must be less then 1')
        return
    if destination == 0.5:
        print('scroll down')
    else:
        print('scroll up')


    layout = screen.children[0]

    animate = Animation(
        pos_hint={
            "center_x": 0.5,
            "center_y": destination
        },
        duration=SCROLL_DURATION
    )

    animate.start(layout)
