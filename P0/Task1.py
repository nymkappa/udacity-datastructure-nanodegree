"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def add_unique_number(all_phone_number, phone_number):
    if (phone_number not in all_phone_number):
        all_phone_number.append(phone_number)

def get_unique_phone_numbers(texts, calls):
    """
    TASK 1:
    How many different telephone numbers are there in the records?
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    all_phone_number = [];

    # Add unique phone number for text
    for text in texts:
        add_unique_number(all_phone_number, text[0])
        add_unique_number(all_phone_number, text[1])

    # Add unique phone number for calls
    for call in calls:
        add_unique_number(all_phone_number, call[0])
        add_unique_number(all_phone_number, call[1])

    print("There are %d" % len(all_phone_number) + " different telephone numbers in the records.")

get_unique_phone_numbers(texts, calls)

# def tests():
#     """
#     Run basic tests
#     """
#     unique_phone_number = [];
#     add_unique_number(unique_phone_number, "123")
#     assert(len(unique_phone_number) == 1)
#     add_unique_number(unique_phone_number, "123")
#     assert(len(unique_phone_number) == 1)
#     add_unique_number(unique_phone_number, "321")
#     assert(len(unique_phone_number) == 2)

# tests()
