def is_not_multiple_12(eggs):
    return not eggs % 12 == 0


##    if eggs % 12 == 0:
##        return False
##    else:
##        return True


def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'



def weather_report(temp):
    if temp >= 20:
        return 'warm enough for ice cream'
    elif temp >= 0:
        return 'above freezing'

def avg_passgrade(grade1, grade2):
    total = 0
    grade_count = 0
 

##    if grade1 >= 50:
##        total = total + grade1
##        grade_count = grade_count + 1
##    elif grade2 >= 50:
##        total = total + grade2        (FAILED)
##        grade_count = grade_count + 1
##
##    if grade_count > 0:
##        print(total / grade_count)
##    else:
##        print(0.0)




    


##    if grade1 >= 50:
##        total = total + grade1
##        grade_count = grade_count + 1
##    if grade2 >= 50:
##        total = total + grade2      (PASSED)
##        grade_count = grade_count + 1
##
##    if grade_count > 0:
##        print(total / grade_count)
##    else:
##        print(0.0)





    


##    if grade1 >= 50 and grade2 >= 50:
##        total = grade1 + grade2
##        grade_count = 2
##                                  (FAILED)
##    if grade_count > 0:
##        print(total / grade_count)
##    else:
##        print(0.0)










    
##
##    if grade1 >= 50:
##        total = total + grade1
##        grade_count = grade_count + 1
##    else:
##        total = total + grade2      (FAILED)
##        grade_count = grade_count + 1
##
##    if grade_count > 0:
##        print(total / grade_count)
##    else:
##        print(0.0)










def last_vowel(s):
        """(str) -> str
        Return the last vowel in s if one exists; otherwise, return None.
        >>> last_vowel("cauliflower")
        "e"
        >>> last_vowel("pfft")
        None
        """
        i = len(s) - 1
        while i >= 0:
             if s[i] in 'aeiouAEIOU':
                 return s[i]
             i = i - 1
        return None

def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result


def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1

    return total


def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total


def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''

    while playlist.count(song) > 3:
        playlist.pop(song)
 


##def for_version(L):
##    found_even = False
##    total = 0
##
##    for num in L:
##        if num % 2 != 0:
##            total = total + num
##        elif not found_even:
##            found_even = True
##
##    return total



##def for_version(L):
##    found_even = False
##    total = 0
##
##    for num in L:
##        if num % 2 != 0:
##            total = total + num
##            found_even = True
##
##    return total


##def for_version(L):
##    found_even = False
##    total = 0
##
##    for num in L:
##        if num % 2 != 0:
##            total = total + num
##        found_even = True
##
##    return total


