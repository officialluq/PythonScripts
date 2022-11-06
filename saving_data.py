HARD_CODED_CODE = 2204

print("Enter your pass code")
try:
    input_code = int(input())
except:
    input_code = 0
if input_code == HARD_CODED_CODE:
    print("SUCCESS")
else:
    print("Try Again")
