import re
#test
# to_camel_case(''), '', "An empty string was provided but not returned")
# to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")

text = "the_stealth_warrior"
def to_camel_case(text):
    regex = re.compile(r'([A-Za-z0-9]+)')
    if text != '':
        search = regex.findall(text)
        output_string = ''
        for i in range(len(search)) :
            if i == 0 and not search[i][0].isupper():
                output_string += search[i]
            else :
                search[i] = search[i][0].upper() + search[i][1:len(search[i])]
                output_string += search[i]
    else: 
        output_string = text
    return output_string

print(to_camel_case(text))

