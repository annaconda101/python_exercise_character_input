class StringChallenge:
    def __init__(self, text_input):
        self.text_input = text_input 

    def get_reversed_string(self):
        text_input_list = self.text_input.split(' ')
        return ' '.join(text_input_list[::-1])


