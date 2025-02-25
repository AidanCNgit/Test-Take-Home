def main():

    quebec_values = ["G", "H", "J"]
    ontario_values = ["K", "L", "M", "N", "P"]

    code = str(input("Please give me a postal code: "))
    match code:

        case code[0].isupper() == False:


    while code[0].isupper() == False or code[1].isnumeric() == False or not(len(code) == 7) or not(code[3] == " "):
        code = str(input("Please enter a valid postal code: "))
    area = ""
    area_type = " rural" if code[1] == "0" else "n urban"

    if code[0] in quebec_values:
        area = location_index[1]
    elif code[0] in ontario_values:
        area = location_index[2]
    else:
        area = location_index[code[0]]


    print(f"This area code seems to be for a{area_type} area in {area}.")
    
    



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