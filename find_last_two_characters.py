# Get a string made of the first two and the last two characters from a given a string.If the string length is less than two, return instead of the empty string.
# Sample String : 'Rajesh'
# Expected Result : 'Rash'
# Sample String : 'Ku'
# Expected Result : 'KuKu'
# Sample String : 'a'
# Expected Result : Empty String

def getStartEndCharString(input_str):
    if len(input_str) >= 2:
        return input_str[0:2]+input_str[-2:]
    return 'Its an Empty String'

if __name__ == "__main__":
    in_string = input('Enter the string : ')
    print(getStartEndCharString(in_string))
