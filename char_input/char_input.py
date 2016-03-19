class StringChallenge:
    def get_reversed_string(self, text_input):
        text_input_list = text_input.split(' ')
        return ' '.join(text_input_list[::-1])


