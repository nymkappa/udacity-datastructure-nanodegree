def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False

    if year % 4 == 0:
        return True

    return False

def daysInMonth(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    return 30

def nextDay(year, month, day):
    new_day = day +1
    new_year = year
    new_month = month

    if (new_day > daysInMonth(year, month)):
        new_day = 1
        new_month = month + 1

    if (new_month > 12):
        new_month = 1
        new_year = year + 1

    return (new_year, new_month, new_day)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    assert (year2, month2, day2) >= (year1, month1, day1)

    if (year2, month2, day2) == (year1, month1, day1):
        return 0

    (curr_year, curr_month, curr_day) = nextDay(year1, month1, day1)
    total_day = 1

    while (curr_year, curr_month, curr_day) < (year2, month2, day2):
        (curr_year, curr_month, curr_day) = nextDay(curr_year, curr_month, curr_day)
        total_day = total_day + 1

    return total_day

def testDaysBetweenDates():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

testDaysBetweenDates()