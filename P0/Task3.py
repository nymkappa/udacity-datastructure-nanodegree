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

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def is_bangalor_number(phone_number):
    """
    Return True if the phone_number if from Bangalor, False otherwise
    """
    if phone_number.find("(080)") != -1:
        return True
    return False

def extract_codes_or_mobile_prefix(phone_number):
    phone_number = phone_number.strip()
    if phone_number[0:2] == "(0":
        return phone_number[1:phone_number.find(")")]
    elif phone_number[0:3] == "140":
        return "140"
    else:
        return phone_number[0:4]

def find_codes_called_by_bangalor_number(calls):
    """
    Part A: Find all of the area codes and mobile prefixes called by people
    in Bangalore.
    """
    area_code_called_by_bangalore = []
    for call in calls:
        if is_bangalor_number(call[0]):
            # print call
            area_code_called_by_bangalore.append(
                extract_codes_or_mobile_prefix(call[1]))

    ratio_bangalore_bangalor = round(area_code_called_by_bangalore.count("080") /
        len(area_code_called_by_bangalore) * 100, 2)

    print("The numbers called by people in Bangalore have codes:",
        *sorted(set(area_code_called_by_bangalore)), sep="\n")
    print(str(ratio_bangalore_bangalor)
        + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

find_codes_called_by_bangalor_number(calls)

def tests():
    """
    Run basic tests
    """
    assert(is_bangalor_number("(080)123456") == True)
    assert(is_bangalor_number("(080) 123 456") == True)
    assert(is_bangalor_number("080123456") == False)

    assert(extract_codes_or_mobile_prefix("(01234)123456") == "01234")
    assert(extract_codes_or_mobile_prefix("(01)123456") == "01")
    assert(extract_codes_or_mobile_prefix("123498765431") == "1234")
    assert(extract_codes_or_mobile_prefix("140498765431") == "140")

tests()
