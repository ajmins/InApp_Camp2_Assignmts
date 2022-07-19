#using if-elif-else conditional statement

print("Method 1\n")

dobMonth = input("Please enter your dob month number: ")
if(dobMonth == "1"):
    print("Month: January\nPersonality: People born January are bold and alert. \nBirth Stone: Garnet")
elif(dobMonth == "2"):
    print("Month: February\nPersonality: People born February are lucky and loyal.\nBirth Stone: Amethyst")
elif(dobMonth == "3"):
    print("Month: March\nPersonality: People born March are nuaghty and genius \nBirth Stone: Aquamarine")   
elif(dobMonth == "4"):
    print("Month: April\nPersonality: People born April are caring and strong\nBirth Stone: Diamond")
elif(dobMonth == "5"):
    print("Month: May\nPersonality: People born May are loving and practical\nBirth Stone: Emerald")
elif(dobMonth == "6"):
    print("Month: June\nPersonality: People born June are romantic and curious\nBirth Stone: Alexandrite")
elif(dobMonth == "7"):
    print("Month: July\nPersonality: People born July are adventurous and honest\nBirth Stone: Ruby")
elif(dobMonth == "8"):
    print("Month: August\nPersonality: People born August are active and hardworking\nBirth Stone: Peridot")
elif(dobMonth == "9"):
    print("Month: September\nPersonality: People born September are sensitive and pretty\nBirth Stone: Sapphire")
elif(dobMonth == "10"):
    print("Month: October\nPersonality: People born October are stylish and friendly\nBirth Stone: Tourmaline")
elif(dobMonth == "11"):
    print("Month: November\nPersonality: People born November are nice and creative\nBirth Stone: Citrine")
elif(dobMonth == "12"):
    print("Month: December\nPersonality: People born December are confident and freedom loving\nBirth Stone: zircon")
else:
    print("You have entered the WRONG dob month number!")

print("\nMethod 2\n")
#using match-case
def personality_test(dobMonth):
    match dobMonth:
        case "1":
            return "Month: January\nPersonality: People born January are bold and alert. \nBirth Stone: Garnet"
        case "2":
            return "Month: February\nPersonality: People born February are lucky and loyal.\nBirth Stone: Amethyst"
        case "3":
            return "Month: March\nPersonality: People born March are nuaghty and genius \nBirth Stone: Aquamarine" 
        case "4":
            return "Month: April\nPersonality: People born April are caring and strong\nBirth Stone: Diamond"
        case "5":
            return "Month: May\nPersonality: People born May are loving and practical\nBirth Stone: Emerald"
        case "6":
            return "Month: June\nPersonality: People born June are romantic and curious\nBirth Stone: Alexandrite"
        case "7":
            return "Month: July\nPersonality: People born July are adventurous and honest\nBirth Stone: Ruby"
        case "8":
            return "Month: August\nPersonality: People born August are active and hardworking\nBirth Stone: Peridot"
        case "9":
            return "Month: September\nPersonality: People born September are sensitive and pretty\nBirth Stone: Sapphire"
        case "10":
            return "Month: October\nPersonality: People born October are stylish and friendly\nBirth Stone: Tourmaline"
        case "11":
            return "Month: November\nPersonality: People born November are nice and creative\nBirth Stone: Citrine"
        case "12":    
            return "Month: December\nPersonality: People born December are confident and freedom loving\nBirth Stone: zircon"
        case _:
            return "You have entered the WRONG dob month number!"
print(personality_test(dobMonth))




