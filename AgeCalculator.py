try:
    # Today's Date from User 
    print("Enter today's date:")
    current_day=int(input("Today's Day (1-31):"))
    current_month=int(input("Today's Month(1-12):"))
    current_year=int(input("Today's Year:"))

    # Get Birth Year
    birth_year=int(input("Enter your birth year:"))

    if birth_year>current_year:
        print("Error Birth year cannot be in the future")

    elif birth_year<1900:
        print("Error Please enter a valid birth year")

    else:
        current_age= current_year-birth_year
        age_in_months= current_age*12
        age_in_days = current_age*365
        age_in_hours  = age_in_days*24
        age_in_minutes= age_in_hours*60
        years_until_100= 100- current_age

        #Display  Results
        print("Results:")
        print("Current Age :", current_age, "years")
        print("Age in Months:", age_in_months, "months")
        print("Age in Days:", age_in_days, "days")
        print("Age in Hours:", age_in_hours, "hours")
        print("Age in Minutes:", age_in_minutes, "minutes")
        print("Years until 100:", years_until_100, "years")
        
        # BONUS:EXACT BIRTH DATE 

        print("BONUS Exact Birth Date Calculation")

        birth_month=int(input("Enter your birth month (1-12):"))
        birth_day =int(input("Enter your birth day (1-31):"))

        #Exact Age Calculation
        #Simple subtraction of years, months, days
        exact_years=current_year-birth_year
        exact_months=current_month-birth_month
        exact_days= current_day-birth_day

        #If day is negative we should borrow from months
        if exact_days < 0:
            exact_months -= 1
            exact_days   += 30 # approximate days in a month

        #If month is negative need to borrow from years
        if exact_months < 0:
            exact_years  -= 1
            exact_months += 12

        #Total Days Lived 
        total_days_lived=exact_years*365
        total_days_lived +=exact_months*30
        total_days_lived +=exact_days

        exact_hours=total_days_lived*24
        exact_minutes= total_days_lived*24* 60

        #Next Birthday
        if (current_month, current_day) >= (birth_month, birth_day):
            #Birthday already passed 
            next_birthday_year =current_year + 1
        else:
            #Birthday not yet come this year
            next_birthday_year= current_year

        #Days Until Next Birthday
        #Convert everything to approximate total days and subtract
        next_bday_total=next_birthday_year*365+birth_month*30+birth_day
        today_total=current_year* 365+ current_month*30+current_day

        days_to_birthday = next_bday_total-today_total

        print("Bonus Results:")
        print("Exact Age:",exact_years,"years",exact_months,"months",exact_days,"days")
        print("Exact Days Lived :",total_days_lived,"days")
        print("Exact Hours:",exact_hours,"hours")
        print("Exact Minutes:",exact_minutes,"minutes")
        print("Next Birthday:",birth_day,"/",birth_month,"/",next_birthday_year)
        print("Days to Birthday :",days_to_birthday,"days")

except ValueError:
    print("Error Please enter a valid number!")