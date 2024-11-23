def convert_string_to_number(s):
    string_to_number = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
    }

    
    words = s.lower().split()
    total = 0
    current = 0
    

    for word in words:
            if word in string_to_number:
                value = string_to_number[word]
                if value == 100:
                    current *= value
                elif value == 1000:
                    current += current * value  # Scale current for thousands
                else:
                 current += value
            else:
                raise ValueError(f"'{word}' is not a valid number word.")
    
    return total + current

convert_string_to_number("two")
