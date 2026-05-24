# ALU Regex Data Extraction

## Overview
This project is a regex-based data extraction and validation system built with Python. The program processes raw text data from a text file and extracts structured information such as:

- Phone numbers
- Hashtags
- ALU email addresses
- Credit card numbers

The goal of this assignment is to demonstrate practical use of Regular Expressions (Regex) for real-world text processing, validation, and secure handling of sensitive data.



# Project Structure


alu-regex-data-extraction_Nzizadenilson/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md




# Features

## Extracts:
- Phone numbers
- Hashtags
- ALU official email addresses
- ALU alumni email addresses
- ALU SI email addresses
- Credit card numbers

## Validation:
The program validates:
- Properly formatted ALU-related email addresses
- Correct phone number formatting
- Credit card number formatting
- Valid hashtag structure

## Output:
All extracted data is stored in a structured JSON file for easy verification.

---

# Regex Patterns Used

## 1. Phone Numbers

```python
r'\+\d{1} \(\d{3}\) \d{3}-\d{4}'
r'\+\d{1,3} \d{1,4} \d{1,4} \d{1,4}'
r'\(\d{1,3}\) \d{1,4}-\d{1,4}'
r'\+\d{3}-\d{3}-\d{3}-\d{3}'
```

Examples:
- +1 (800) 555-1234
- +250 788 123 456
- (250) 123-4567

---

## 2. Hashtags

```python
r'#\w+'
```

Examples:
- #Python
- #Regex
- #ALU

---

## 3. ALU Email Validation

The following ALU-specific domains are validated:

```python
r'[a-zA-Z0-9._%+-]+@alueducation\.com'
r'[a-zA-Z0-9._%+-]+@alumni\.alueducation\.com'
r'[a-zA-Z0-9._%+-]+@si\.alueducation\.com'
```

Examples:
- student@alueducation.com
- graduate@alumni.alueducation.com
- mentor@si.alueducation.com

---

## 4. Credit Card Numbers

```python
r'\d{4}-\d{4}-\d{4}-\d{4}'
r'\d{4} \d{4} \d{4} \d{4}'
```

Examples:
- 1234-5678-9012-3456
- 1234 5678 9012 3456

---

# Security Considerations

This project demonstrates defensive programming practices by:

- Validating structured data before extraction
- Ignoring malformed patterns
- Restricting accepted email domains to ALU-approved domains only
- Preventing unsafe or unrelated text from being treated as valid data
- Storing extracted results in JSON instead of printing sensitive information repeatedly

Sensitive information such as credit card numbers and emails should always be handled carefully in production systems.

---

# How the Program Works

1. The program opens and reads the `raw-text.txt` file.
2. Regex patterns are applied to the text.
3. Matching data is extracted and stored in lists.
4. All extracted data is organized into a Python dictionary.
5. The results are exported into `sample-output.json`.

---

# How to Run the Program

## Requirements
Make sure Python is installed on your machine.

Check Python version:

```bash
python --version
```

---

## Run the Program

Navigate to the project folder and run:

```bash
python src/main.py
```

After execution, the extracted results will be saved in:

```bash
output/sample-output.json
```

---

# Example Output

```json
{
    "phone_numbers": [
        "+1 (800) 555-1234"
    ],
    "hashtags": [
        "#Python",
        "#Regex"
    ],
    "ALU_emails": [
        "student@alueducation.com"
    ],
    "credit_cards": [
        "1234-5678-9012-3456"
    ]
}

# Technologies Used

- Python 3
- Regular Expressions (`re` module)
- JSON (`json` module)


# Notes

- The input text is intentionally designed to resemble realistic production-style raw text.
- The project focuses on regex extraction and validation logic rather than UI design.
- Multiple regex patterns are used to support variations in real-world data formatting.



# Future Improvements

Possible future enhancements include:

- Adding URL extraction
- Supporting time formats
- Adding HTML tag extraction
- Implementing stronger credit card validation (Luhn Algorithm)
- Masking sensitive extracted data
- Improving duplicate filtering

