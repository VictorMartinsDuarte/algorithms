def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first = first_string.lower()
    second = second_string.lower()
    for letter in first:
        if letter in second:
            second = second.replace(letter, "", 1)
        else:
            return False
    return True
