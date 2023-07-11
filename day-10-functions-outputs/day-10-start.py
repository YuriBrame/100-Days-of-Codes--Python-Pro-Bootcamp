#Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    #Utilização de uma Docstring para documentar o uso da sua função.
    #Necessita ser a primeira linha da função.
    if f_name == "" or l_name == "":
        return "You didin't provide a valid input"
    result = f"{f_name} {l_name}".title()
    return result

# formated_name = format_name("yuri", "bRAme")

print(format_name(input("What is your first name?"), input("What is your last name?")))