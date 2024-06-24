import zxcvbn
import getpass
import sys

def test_pass():
    password = getpass.getpass("Enter your password : ")
    result = zxcvbn(password)
    print(f"Password : {result['password']}")
    print(f"Score : {result['score']}")
    print(f"Crack time : {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"Suggestions : {result['feedback']['suggestions']}")

def test_multiple_pass(pass_file):
    with open(pass_file, 'r') as passwords:
        for password in passwords:
            dfv

if len(sys.argv) == 2:
    test_multiple_pass(sys.argv[1])
elif len(sys.argv) == 1:
    test_pass()
else:
    print("Usage : python password_tester.py <file> (for a file containing passwords) or python password_tester.py to be prompted")