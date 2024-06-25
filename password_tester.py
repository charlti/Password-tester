import zxcvbn
import getpass
import sys

def test_pass():
    password = getpass.getpass("Enter your password : ")
    result = zxcvbn.zxcvbn(password)
    print(f"Password : {result['password']}")
    print(f"Score : {result['score']}/4")
    print(f"Crack time : {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"Suggestions : {result['feedback']['suggestions']}")

def test_multiple_pass(pass_file):
    try:
        with open(pass_file, 'r') as passwords:
            for password in passwords:
                res = zxcvbn.zxcvbn(password.strip('\n'))
                print('\n[+] ######################')# for readability
                print(f"Password : {res['password']}")
                print(f"Score : {res['score']}/4")
                print(f"Crack time : {res['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
                print(f"Suggestions : {res['feedback']['suggestions']}")
    except Exception:
        print('[!] Please make sure to specify an accessible file containing passwords.')

# If there is one argument
if len(sys.argv) == 2:
    test_multiple_pass(sys.argv[1])
# If there is none
elif len(sys.argv) == 1:
    test_pass()
else:
    print("Usage : python password_tester.py <file> (for a file containing passwords) or python password_tester.py to be prompted")