
input_data = input("Please pass me your First Name, Second Name and Year of birth - separate data with semicolon")
first_name = input_data.split(',')[0]
second_name = input_data.split(',')[1]
birth_year = input_data  .split(',')[2]
print(f'First name: {first_name}')
print(f'Second name: {second_name}')
print(f'Birth year: {birth_year}')