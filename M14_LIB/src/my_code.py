
import string

def ispal(s):
    s = s.translate(str.maketrans('', '', string.punctuation + ' '))
    s = s.lower()
    return s == s[::-1]

def testPalindrome(f):
    test_cases = [
        ("", True),            
        ("a", True),           
        ("anna", True),        
        ("Able was I, ere I saw Elba", True),  
        ("hello", False),      
        ("racecar!", True),   
        ("Python", False),    
        ("step on no pets", True),  
    ]

    for s, expected_result in test_cases:
        result = f(s)
        if result != expected_result:
            return False

    return True

if __name__ == '__main__':
    rc = testPalindrome(ispal)
    print(rc)
