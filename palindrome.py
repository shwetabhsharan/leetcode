"""
check if string is palindrome or not
"""
 
def check_palindrome(sentence):
    """
          
    """
    reverse_list = []
    l1 = [i for i in sentence]
  
    # next 3 lines can be replaced with l1[::-1] reverse parsing
  
    for i in range(len(l1) -1, -1, -1):
        reverse_list.append(sentence[i])
    reverse_string = "".join(reverse_list)
    if reverse_string == sentence:
        print "Valid Palindrone"
    else:
        print "Not a Palindrome"
  
check_palindrome("racecar")
