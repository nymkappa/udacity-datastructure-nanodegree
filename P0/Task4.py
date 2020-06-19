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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def get_unique_calling_number(calls):
    calling_numbers = []
    for call in calls:
        calling_numbers.append(call[0])

    return set(calling_numbers)

def find_telemarketers(calls, texts):
    unique_calling_numbers = list(get_unique_calling_number(calls))

    # we merge both array to we can run comparaison on everything at one
    communications = calls + texts
    for communication in communications:
        for unique_calling_number in unique_calling_numbers[:]:
            # phone call - simply check the recipient number
            if (len(communication) == 4 and unique_calling_number == communication[1]):
                unique_calling_numbers.remove(unique_calling_number)
                break

            # message  - check both sending and receiving numbers
            elif(len(communication) == 3 and unique_calling_number in [communication[0], communication[1]]):
                unique_calling_numbers.remove(unique_calling_number)
                break

    print("These numbers could be telemarketers: ", *sorted(unique_calling_numbers), sep="\n")

find_telemarketers(calls, texts)
