import re

def is_valid(id, text):
    count_bad_ch = 0
    for ch in text:
        if re.match(r'[\W]', ch) is not None:
            count_bad_ch += 1
    #print('count_ch_bad:', count_bad_ch)
    #print(len(text))
    if not id.isdigit() and count_bad_ch <= len(text)/ 2:
        print('Not Spam')
    elif not id.isdigit() and count_bad_ch > len(text)/ 2 and len(re.findall('spam', text.lower())) != 0:
        print('Invalid Content')
    elif id.isdigit() and count_bad_ch > len(text)/ 2 and len(re.findall('spam', text.lower())) != 0:
        print('Fully Invalid')
    elif id.isdigit() and count_bad_ch <= len(text)/ 2 and len(re.findall('spam', text.lower())) != 0:
        print('Invalid Sender')