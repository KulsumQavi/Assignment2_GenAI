# Declaring Variables for Biocard information
name    = "Kulsum Qavi"
age     = 22
course  = "Generative AI"
college = "Anjuman University"
email   = "kulsumqavi@example.com"
#  Card Formatting 
card_width = 45 #Declaring width of the card
print("╔" + "═" * card_width + "╗") 
print("║" + "STUDENT BIO CARD".center(card_width) + "║")
print("╠" + "═" * card_width + "╣")
print(f"║  {'Name':<8}: {name:<33}║")
print(f"║  {'Age':<8}: {str(age) + ' years':<33}║")
print(f"║  {'Course':<8}: {course:<33}║")
print(f"║  {'College':<8}: {college:<33}║")
print(f"║  {'Email':<8}: {email:<33}║")
print("╚" + "═" * card_width + "╝")