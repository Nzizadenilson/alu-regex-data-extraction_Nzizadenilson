import re
#Open and read the raw-text.txt file
file = open("raw-text.txt", "r")
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
    credit_cards.extend(cards)
