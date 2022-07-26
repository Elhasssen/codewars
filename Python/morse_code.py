# invert values and keys
# inv_map = {v: k for k, v in MORSE_CODE_DICT.items()}
MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
                    '-.-.': 'C', '-..': 'D',
                    '.': 'E', '..-.': 'F',
                    '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J',
                    '-.-': 'K', '.-..': 'L',
                    '--': 'M', '-.': 'N',
                    '---': 'O', '.--.': 'P',
                    '--.-': 'Q', '.-.': 'R',
                    '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V',
                    '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z',
                    '.----': '1', '..---': '2',
                    '...--': '3', '....-': '4',
                    '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8',
                    '----.': '9', '-----': '0',
                    '--..--': ', ', '.-.-.-': '.',
                    '..--..': '?', '-..-.': '/',
                    '-....-': '-', '-.--.': '(',
                    '-.--.-': ')'}
morse_code = '.... . -.--   .--- ..- -.. .'
# def decode_morse(morse_code):
#     MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
#                     '-.-.': 'C', '-..': 'D',
#                     '.': 'E', '..-.': 'F',
#                     '--.': 'G', '....': 'H',
#                     '..': 'I', '.---': 'J',
#                     '-.-': 'K', '.-..': 'L',
#                     '--': 'M', '-.': 'N',
#                     '---': 'O', '.--.': 'P',
#                     '--.-': 'Q', '.-.': 'R',
#                     '...': 'S', '-': 'T',
#                     '..-': 'U', '...-': 'V',
#                     '.--': 'W', '-..-': 'X',
#                     '-.--': 'Y', '--..': 'Z',
#                     '.----': '1', '..---': '2',
#                     '...--': '3', '....-': '4',
#                     '.....': '5', '-....': '6',
#                     '--...': '7', '---..': '8',
#                     '----.': '9', '-----': '0',
#                     '--..--': ', ', '.-.-.-': '.',
#                     '..--..': '?', '-..-.': '/',
#                     '-....-': '-', '-.--.': '(',
#                     '-.--.-': ')'}
#     words = morse_code.split('   ')
#     human_word = ''
#     for x in words :
#         m = x.split(' ')
#         for bite in m :
#             human_word += MORSE_CODE_DICT[bite]
#         human_word += ' '
#     human_word = human_word[0:len(human_word)-1]

#     return human_word
# morse_code = '.... . -.--   .--- ..- -.. .' + ' '
# word_morse = ''
# word_human = ''
# num_space = 0
# for x in range(0, len(morse_code)):
#     if morse_code[x] != ' ' :
#         num_space = 0
#         word_morse += morse_code[x]
#     elif morse_code[x] == ' ':
#         num_space += 1
#         if num_space == 1 :
#             word_human += MORSE_CODE_DICT[word_morse]
#             word_morse = ''
#         elif num_space == 2 :
#             word_human += ' '
#             word_morse = ''
        


# print(word_human)
s = ' . '
x = s.strip()
print(type(x))