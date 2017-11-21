# CTI 110
# M6T1 - Kilometer Converter
# Jose De Jesus
# November 14, 2017
# converts Kilometers to miles using two functions


# Gets distance in kilometers and calls show_miles function
def main():
    # Asks for user to input their Kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # Displays the distance, but converted into miles
    show_miles(kilometers)

# Converts parameter km from kilometers to miles and then prints results 
def show_miles(km):
    # Converts the km to miles.
    miles = km * 0.6214

    # Displays the miles 
    print(format(km, ',.2f'), 'kilometers equals', format(miles, ',.2f'), 'miles.')

# program start
main()
