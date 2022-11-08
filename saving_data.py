HARD_CODED_CODE = 0

print("Enter your pass code")
try:
    input_code = int(input())
except ValueError:
    input_code = None

if input_code == HARD_CODED_CODE:
    print("SUCCESS")
else:
    print("Try Again")
