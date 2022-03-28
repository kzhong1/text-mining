from unittest import skip

def skip_header(line):

    return line.split('=--', 1)[1]
       
# def process_line(line, keyword, sentence):
#     words = line.split( ) 
#     for word in words: 
#         if word.endswith('.'):
#             sentence += f' {word}'
#             if sentence.__contains__(keyword):
#                 print(sentence)
#                 print('\n')
#                 sentence = ''
#             else: 
#                 sentence += f' {word}'

def find_keyword_sentence(keyword):
    f = open('test/part_of_history.txt')

    sentence = ''

    for line in f: 
        if line.startswith('='): 
           first_line = skip_header(line)
           words = first_line.split( )
           for word in words:
                if word.endswith('.'):
                    sentence += f' {word}'
                    if sentence.__contains__(keyword):
                        print(sentence)
                        print('\n')
                    sentence = ''
                else: 
                    sentence += f' {word}'
        else: 
            words = line.split()
            for word in words:
                if word.endswith('.'):
                    sentence += f' {word}'
                    if sentence.__contains__(keyword):
                        print(sentence)
                        print('\n')
                    sentence = ''
                else: 
                    sentence += f' {word}'

if __name__ == '__main__':
    find_keyword_sentence('war')

