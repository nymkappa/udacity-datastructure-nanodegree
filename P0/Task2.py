"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def increment_time_per_phone_number(time_per_phone_number, phone_number, time_spent):
    if (phone_number not in time_per_phone_number):
        time_per_phone_number[phone_number] = int(time_spent)
    else:
        time_per_phone_number[phone_number] += int(time_spent)

def find_most_active_calling_phone_number(calls):
    """
    TASK 2: Which telephone number spent the longest time on the phone
    during the period? Don't forget that time spent answering a call is
    also time spent on the phone.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during
    September 2016.".
    """
    time_per_phone_number = {};

    # Sum phone call time
    for call in calls:
        increment_time_per_phone_number(time_per_phone_number, call[0], call[3])
        increment_time_per_phone_number(time_per_phone_number, call[1], call[3])

    # Now sort the time_per_phone_number array
    time_per_phone_number_sorted = sorted(time_per_phone_number.items(), key=lambda x: x[1], reverse=True)

    print(time_per_phone_number_sorted[0][0] + " spent the longest time, %d"
        % time_per_phone_number_sorted[0][1] + " seconds, on the phone during September 2016.")

find_most_active_calling_phone_number(calls)

# def tests():
#     """
#     Run basic tests
#     """
#     time_per_phone_number = {}
#     increment_time_per_phone_number(time_per_phone_number, "123", 10)
#     assert(len(time_per_phone_number) == 1)
#     assert(time_per_phone_number["123"] == 10)
#     increment_time_per_phone_number(time_per_phone_number, "123", 10)
#     assert(len(time_per_phone_number) == 1)
#     assert(time_per_phone_number["123"] == 20)
#     increment_time_per_phone_number(time_per_phone_number, "321", 10)
#     assert(len(time_per_phone_number) == 2)
#     assert(time_per_phone_number["123"] == 20)
#     assert(time_per_phone_number["321"] == 10)

# tests()
