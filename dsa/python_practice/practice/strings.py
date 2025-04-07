def string_substring_range(s, start, end):
    """Returns a substring from the given start and end indices."""
    pass

def string_substring_alternate(s):
    """Returns a substring with alternate characters."""
    pass

def string_substring_last_3(s):
    """Returns the last 3 characters of the string."""
    pass

def string_replace_char_at_index(s, index, char):
    """Replaces the character at the given index with the given character."""
    pass

def string_replace_first_occurrence(s, old_char, new_char):
    """Replaces the first occurrence of the old character with the new character."""
    pass

def string_replace_all_occurrences(s, old_char, new_char):
    """Replaces all occurrences of the old character with the new character."""
    pass

def string_to_list(s):
    """Converts the string to a list of characters."""
    pass

def string_sort_ascii(s):
    """Sorts the string based on ASCII values."""
    pass

def string_char_to_ascii(char):
    """Returns the ASCII value of the given character."""
    pass

def string_ascii_to_char(ascii_val):
    """Returns the character corresponding to the given ASCII value."""
    pass

def string_is_int(char):
    """Checks if the given character is an integer."""
    pass

def string_is_letter(char):
    """Checks if the given character is a letter."""
    pass

def string_list_to_string(char_list):
    """Converts a list of characters back to a string."""
    pass

def string_to_upper(s):
    """Converts the string to uppercase."""
    pass

def string_to_lower(s):
    """Converts the string to lowercase."""
    pass

def string_is_numeric(char):
    """Checks if the given character is numeric."""
    pass

def string_split(s, delimiter):
    """Splits the string using the given delimiter."""
    pass

def string_is_alpha(char):
    """Checks if the given character is alphabetic."""
    pass

def string_sort(s):
    """Sorts the string alphabetically."""
    pass

# Test Cases
def test_string_functions():
    # Test substring range
    s1 = "abcdefg"
    assert string_substring_range(s1, 3, 5) == "de"

    # Test substring alternate
    s2 = "abcdefg"
    assert string_substring_alternate(s2) == "aceg"

    # Test substring last 3
    s3 = "abcdefg"
    assert string_substring_last_3(s3) == "efg"

    # Test replace char at index
    s4 = "abcdefg"
    assert string_replace_char_at_index(s4, 3, "X") == "abcXefg"

    # Test replace first occurrence
    s5 = "aabbccdd"
    assert string_replace_first_occurrence(s5, "b", "X") == "aaXbccdd"

    # Test replace all occurrences
    s6 = "aabbccdd"
    assert string_replace_all_occurrences(s6, "b", "X") == "aaXXccdd"

    # Test to list
    s7 = "hello"
    assert string_to_list(s7) == ['h', 'e', 'l', 'l', 'o']

    # Test sort ascii
    s8 = "dcba"
    assert string_sort_ascii(s8) == "abcd"

    # Test char to ascii
    assert string_char_to_ascii("a") == 97

    # Test ascii to char
    assert string_ascii_to_char(97) == "a"

    # Test is int
    assert string_is_int("1") == True
    assert string_is_int("a") == False

    # Test is letter
    assert string_is_letter("a") == True
    assert string_is_letter("1") == False

    # Test list to string
    l9 = ['h', 'e', 'l', 'l', 'o']
    assert string_list_to_string(l9) == "hello"

    # Test to upper
    s10 = "hello"
    assert string_to_upper(s10) == "HELLO"

    # Test to lower
    s11 = "HELLO"
    assert string_to_lower(s11) == "hello"

    # Test is numeric
    assert string_is_numeric("1") == True
    assert string_is_numeric("a") == False

    # Test split
    s12 = "a,b,c"
    assert string_split(s12, ",") == ["a", "b", "c"]

    # Test is alpha
    assert string_is_alpha("a") == True
    assert string_is_alpha("1") == False

    # Test sort string
    s13 = "dcba"
    assert string_sort(s13) == "abcd"

test_string_functions()