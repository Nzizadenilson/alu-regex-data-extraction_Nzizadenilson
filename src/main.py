import re
import json
#Open and read the raw-text.txt file
file = open("input/raw-text.txt", "r")
text = file.read()
file.close()
#1.Find all phone numbers in the text
phone_patterns = [
    r'\+\d{1} \(\d{3}\) \d{3}-\d{4}',
    r'\+\d{1,3} \d{1,4} \d{1,4} \d{1,4}',
    r'\(\d{1,3}\) \d{1,4}-\d{1,4}',
    r'\+\d{3}-\d{3}-\d{3}-\d{3}',
    r'\+\d{1,3} \d{1,4} \d{1,4} \d{1,4} \d{1,4} \d{1,4}'
]
phone_numbers = []
for pattern in phone_patterns:
    numbers = re.findall(pattern, text)
    phone_numbers.extend(numbers)


#2.Finding hashtags in text
hashtags= re.findall(r'#\w+', text)


#3.Find all ALU email addresses in the text
ALU_email_pattern = [
    r'[a-zA-Z0-9._%+-]+@alueducation\.com',
    r'[a-zA-Z0-9._%+-]+@alumni\.alueducation\.com',
    r'[a-zA-Z0-9._%+-]+@si\.alueducation\.com'
]
ALU_emails = []
for pattern in ALU_email_pattern:
    emails = re.findall(pattern, text)
    ALU_emails.extend(emails)

    
#4.Find all credit card numbers in the text
credit_card_pattern = [
    r'\d{4}-\d{4}-\d{4}-\d{4}',
    r'\d{4} \d{4} \d{4} \d{4}',
    
]
credit_cards = []
for pattern in credit_card_pattern:
    cards = re.findall(pattern, text)
   
    for card in cards:
        if '-' in card:
            secured_card = "****-****-****-" + card[-4:]
        else:
            secured_card = "**** **** ****" + card[-4:]
        credit_cards.append(secured_card)
        

#Put the results in a dictionary and display them in a json file
output = {
    "phone_numbers": phone_numbers,
    "hashtags": hashtags,
    "ALU_emails": ALU_emails,
    "credit_cards": credit_cards
}
json_file = open("output/sample-output.json", "w")
json.dump(output, json_file, indent=4)
json_file.close()

print("Data has been extracted go and check the json file now")
