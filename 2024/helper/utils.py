# print helper function
def print_output(data, text):
    print("\n*************************************************\n")
    print(text, "\n")
    print(data)
    print("\n")


# print challenge day
def challenge_day(day):
    from pyfiglet import figlet_format

    print("\n")
    print(figlet_format("Day " + day, font="starwars"))
