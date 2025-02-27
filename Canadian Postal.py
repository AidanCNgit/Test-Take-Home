def main():

    #Didn't want to put a bunch of duplicates in the dictionary, so I did this:
    quebec_values = ["G", "H", "J"]
    ontario_values = ["K", "L", "M", "N", "P"]
    #Easiest, probably not efficent, way to check the alternating letters + nums. Space in code makes things difficult.
    letters = [0, 2, 5]
    #For the loop to check if code is valid.
    valid_code = 0

    code = str(input("Please give me a postal code: "))

    #Massive loop to check if code is valid. Tried to make it less complex with match case, but couldn't figure out how simply

    while valid_code == 0:
        for i in range(7):
            valid_code = 1
            if not(len(code) == 7):
                code = str(input("Make sure your code is a valid length: "))
                valid_code = 0
            if not(code[3] == " "):
                code = str(input("Please make sure your code has valid spacing: "))
                valid_code = 0
            if i in letters:
                if code[i].isupper() == False or code[i].isnumeric() == True or (not(code[0] in location_index) 
                and not(code[0] in quebec_values) and not(code[0] in ontario_values)):
                    code = str(input(f"""Letter {i + 1} of postal code is invalid, make sure to capitalize, and make sure the area code
is valid: """))
                    valid_code = 0
            else:
                if code[i].isnumeric() == False and not(i == 3):
                    code = str(input(f"Number {i + 1} is invalid. Please enter a valid code, and make sure number {i + 1} of the code is numerical: "))
                    valid_code = 0
            
    #Area code, "n urban" because of grammar 

    area = ""
    area_type = " rural" if code[1] == "0" else "n urban"

    #Checks for Quebec or Ontario area code.

    if code[0] in quebec_values:
        area = location_index[1]
    elif code[0] in ontario_values:
        area = location_index[2]
    else:
        area = location_index[code[0]]


    print(f"This area code seems to be for a{area_type} area in {area}.")
    
    

#Dictionary for area codes.

location_index = {

    "A" : "Newfoundland",
    "B" : "Nova Scotia",
    "C" : "Prince Edward Island",
    "E" : "New Brunswick",
    1 : "Quebec",
    2 : "Ontario",
    "R" : "Manitoba",
    "S" : "Saskatchewan",
    "T" : "Alberta",
    "V" : "British Columbia",
    "X" : "Nunavut or Northwest Terriotories",
    "Y" : "Yukon"

}

main()