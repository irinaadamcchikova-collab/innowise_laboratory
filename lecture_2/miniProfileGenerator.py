def generate_profile(age) :
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"
print("Welcome to the Mini-Profile Generator!")
print("______I'll collect some information about you______")

user_name = input("Enter your full name: ")

while True:
    birth_year_str = input("Enter your birth year: ")
    if birth_year_str.isdigit() and len(birth_year_str) == 4:
        birth_year = int(birth_year_str)
        if 1935<=birth_year<=2025:
            current_age = 2025 - birth_year
            break
        else:
            print("Invalid year")
life_stage = generate_profile(current_age)
hobbies = []
while True:
    hobby = input("Enter a favourite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    elif hobby:
        hobbies.append(hobby.capitalize())

user_profile = {"name" : user_name, "age" : current_age, "life_stage" : life_stage, "hobbies" : hobbies}

print("Profile Summary: ")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")
if not user_profile["hobbies"]:
    print("You didn't mention any hobbies")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}): ")
    for hobby in user_profile['hobbies']:
        print(F" - {hobby}")