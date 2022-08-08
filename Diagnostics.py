from kivy.app import App


def diagnose_ads(answers_list = []):

    """
        diagnoses for ads algorithm:
        1. check if there is 2 "Yes" answers at the 5 first answers
        2. check for 5 "Yes" answers at the next 12 questions (6-17)
        3. check for one more "Yes" answer at the last 3 questions (18-20)
        4. if all the the list of answers follows all the criterias above, the user is diagnosed with ads
    """

    if len(answers_list) < 20:
        try:
            user = App.get_running_app().user
            list_for_diagnostic = user.answers
        except:
            print('can able to diagnose, not enough answers')
            return ''
    else:
        list_for_diagnostic = answers_list

    diagnose = ""
    first_counter = 0
    for criteria_one in range(5):
        if list_for_diagnostic[criteria_one] == 'Yes':
            first_counter += 1
    if first_counter >= 2:
        second_counter = 0
        for criteria_two in range(5, 17):
            if list_for_diagnostic[criteria_two] == 'Yes':
                second_counter += 1
        if second_counter >= 5:
            third_counter = 0
            for criteria_three in range(17, 20):
                if list_for_diagnostic[criteria_three] == 'Yes':
                    third_counter += 1
            if third_counter >= 1:
                diagnose = "ADS"


    return diagnose

class Question_sets():

    def ads(self):
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
        return questions