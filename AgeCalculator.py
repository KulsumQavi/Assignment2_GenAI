#Importing date from datetime module to get current date
from datetime import date
# Get today's date
today = date.today()
current_year = today.year
#Get Input from User
try:
    birth_year = int(input("Enter your birth year: "))

    # To Check if birth year is valid
    if birth_year>current_year:
        print("Error Birth year cannot be in the future!")

    elif birth_year<1900:
        print("Error Please enter a valid birth year!")

    else:
        #Current age
        current_age =current_year-birth_year

        #Age in months 12 months in a year
        age_in_months=current_age*12

        #Age in days 365 days approx in a year
        age_in_days=current_age*365

        #Age in hours 24 hours in a day
        age_in_hours =age_in_days*24

        #Age in minutes 60 minutes in an hour
        age_in_minutes=age_in_hours*60

        #Years until Age 100
        years_until_100=100-current_age
        print("Results:")
        print("Current Age:", current_age,"years")
        print("Age in Months:", age_in_months,"months")
        print("Age in Days:", age_in_days,"days")
        print("Age in Hours:", age_in_hours,"hours")
        print("Age in Minutes:", age_in_minutes,"minutes")
        print("Years until 100:", years_until_100,"years")

    #Exact Birth Date Calculation
        birth_month=int(input("Enter your birth month (1-12): "))
        birth_day =int(input("Enter your birth day   (1-31): "))

    # Create birth date object
        birth_date=date(birth_year, birth_month, birth_day)

    # Exact Days, Hours, Minutes
    #Subtract birth date from today to get exact days
        exact_days= (today-birth_date).days
        exact_hours=exact_days*24
        exact_minutes=exact_days*24*60

     #Next Birthday
        next_birthday =date(current_year, birth_month, birth_day)

        # If birthday already passed need to add 1 to current year
        if next_birthday <today:
            next_birthday=date(current_year+1,birth_month,birth_day)

        #Display Bonus Results
        print("\nBonus Results:")
        print("Exact Days Lived :", exact_days, "days")
        print("Exact Hours      :", exact_hours, "hours")
        print("Exact Minutes    :", exact_minutes, "minutes")
        print("Next Birthday    :", next_birthday)

except ValueError:
    print("Error: Please enter a valid number / date!")