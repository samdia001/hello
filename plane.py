# Börjar med user friendly meddalande.
print("\n Welcome to Unit Converter! Ready to transform your measurements?\n")
# Använder float function med input istället för int, för att göra användare input mer flexible.
meters = float(input("Enter current hight in meter over sea, and press enter:"))
velocity = float(input("Enter current velocity in km/h, and press enter:"))
temperature = float(input("Enter current outside temperature in °C, and press enter:")) 
# Nu börjar jag göra beräkningarna för att konvertera enheterna .
feet = meters * 3.28084
mph = velocity * 0.62137
fahrenheit = (temperature * 9/5) + 32
# Använder .2f för att få två decimaler.
print(f"\nThe hight {meters} m in feet over the see is {feet:.2f} feet")
print(f"The velocity {velocity} km/h in mph is {mph:.2f} mph")
print(f"The temperature {temperature} °C in Fahrenheit is {fahrenheit:.1f} °F")