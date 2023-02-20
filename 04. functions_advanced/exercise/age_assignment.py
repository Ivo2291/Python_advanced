def age_assignment(*args, **kwargs):
    people = {}
    result = ''

    for key, value in kwargs.items():
        for name in args:
            if name[:1] == key:
                people[name] = value

    for name, age in dict(sorted(people.items())).items():
        result += f"{name} is {age} years old." + '\n'

    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
