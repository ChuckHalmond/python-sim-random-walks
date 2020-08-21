
'''
    Utilities related to I/O
'''

import sys

FLOAT_FORMATTER = '{:.2f}'

def inputInt(prompt = 'an int', defaultValue = None):

    prompt = 'Please enter ' + prompt + ' [int]'
    if (defaultValue != None):
        prompt += ' (default value is ' + str(defaultValue) + ')'
    prompt += ':'

    print(prompt)

    while (True):
        num = input('> ')
        if (num == '' and defaultValue != None):
            print(str(defaultValue) + ' (default value)')
            return defaultValue
        try:
            num = int(num)
            return num
        except:
            print('Please enter a valid int')

def inputFloat(prompt = 'a float', defaultValue=None):

    prompt = 'Please enter ' + prompt + ' [float]'
    if (defaultValue != None):
        prompt += ' (default value is ' + str(defaultValue) + ')'
    prompt += ':'

    print(prompt)

    while (True):
        num = input('> ')
        if (num == '' and defaultValue != None):
            print(str(defaultValue) + ' (default value)')
            return defaultValue
        try:
            num = float(num)
            return num
        except:
            print('Please enter a valid float')
        

def inputChoice(choices, prompt = 'an option'):
    string = None
    
    prompt = 'Please choose ' + prompt + ':\n'

    for i in range(len(choices)):
        if (i < len(choices) - 1):
            prompt += '- \'' + choices[i]['value'] + '\' : ' + choices[i]['desc'] + ';\n'
        else:
            prompt += '- \'' + choices[i]['value'] + '\' : ' + choices[i]['desc'] + '.'
    print(prompt)

    string = input('> ')
    while (not string in [choice['value'] for choice in choices]):
        print('Please enter a valid option')
        string = input('> ')

    return string

def progressBar(value, endvalue, bar_length = 40):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rProgress : [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()