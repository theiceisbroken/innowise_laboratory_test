"""
This script creates a simple Mini Profile Generator.

It collects personal information from the user, such as user's name,
birth year, hobbies. Using this information, the script calculates the
user's current age, determines life stage ("Child", "Teenager", "Adult"),
gathers all hobbies into a single list.

Finally, it prints a well-formatted summary of the user's profile.
"""


def generate_profile(age: int) -> str:
    """
    Determine the user's life stage based on the age.

    Args:
        age (int): the user's age in full years.

    Returns:
        str: "Child", "Teenager", or "Adult" depending on the age value.
    """
    if age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

# Ask for the user's name
user_name = input("Enter your full name: ")

# Ask for the user's birth year and calculate current age
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Collect hobbies from the user
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    else:
        hobbies.append(hobby)

#Determine the life stage
life_stage = generate_profile(current_age)

# Build the final user's profile
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Display the summary
print("---\nProfile Summary:")
print(f'Name: {user_name}')
print(f'Age: {current_age}')
print(f'Life Stage: {life_stage}')

if hobbies:
    print(f'Favorite Hobbies ({len(hobbies)}):')
    for hobby in hobbies:
        print(f'- {hobby}')
else:
    print("You didn't mention any hobbies.")

print("---")
