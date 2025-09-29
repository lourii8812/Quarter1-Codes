name = input('Enter your full name(First, Middle, Last): ')
substrings = name.split(",")
First , Middle , Last = substrings
capt_firstname = str.capitalize(First)
capt_middlename = str.capitalize(Middle)
capt_lastname = str.capitalize(Last)
Mi = capt_middlename[:1]+"."
print('Formatted Name: ', capt_lastname, ",", capt_firstname, Mi)