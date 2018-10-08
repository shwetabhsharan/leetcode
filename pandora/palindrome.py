"""
implement palindrome
"""

def check_palindrome(data):
    data = str(data)
    return data == data[::-1]
assert True == check_palindrome("racecar")
assert True == check_palindrome("shwetabh")