#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses in the clipboard
# koment

import pyperclip, re

phoneRegex= re.compile(r'''(
    (\(?\+?\d{3}\)?)?      #czech or slovakian state number
    (\s)?                  #possible space
    (\d{9}|\d{3}\s?\d{3}\s?\d{3}|\d{3}\s?\d{2}\s?\d{2}\s?\d{2})     #different formats of the rest
    )''', re.VERBOSE)

mailRegex = re.compile('''(
    ([a-zA-Z0-9._%+-]+)     # username
    (@)                     #@ symbol
    ([a-zA-Z0-9.-]+)        #domain name
    (\.[a-zA-Z]{2,4})       #dot-something
    )''', re.VERBOSE)

finalNumbers = []
finalEmails=[]

inserted = str(pyperclip.paste())
if inserted == None:
    inserted=input('Give me some text: ')

for i in phoneRegex.findall(inserted):
    finalNumbers.append(i[0].strip())
    '''my original solution / worse because this is not working with the list but the string
    if finalNumbers == '':
        finalNumbers = ''.join((i)).strip()
    else:
        finalNumbers = finalNumbers + '\n' + ''.join(i).strip()'''

for i in mailRegex.findall(inserted):
    finalEmails.append(i[0].strip())
    ''' my original solution / worse because this is not working with the list but the  string
    if finalEmails == '':
        finalEmails = ''.join((i)).strip()
    else:
        finalEmails = finalEmails + '\n' + ''.join(i).strip()'''

if len(finalNumbers) > 0 and len(finalEmails) > 0:
    print('\n'.join(finalNumbers))
    print('\n'.join(finalEmails))
    pyperclip.copy('\n'.join(finalNumbers)+'\n'+'\n'.join(finalEmails))
    print('Everything copied to clipboard')
else:
    print('Nothing relevant found')