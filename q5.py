# Given a list of daily temperatures in Celsius: [15, 22, -5, 38, 42, 10, -12].
# Iterate through the list and print a warning message for each:

# If the temperature is below 0, print: "[Temp]°C : Freezing warning!"

# If the temperature is between 0 and 35, print: "[Temp]°C : Normal conditions."

# If the temperature is above 35, print: "[Temp]°C : Heatwave warning!"
## Implement from below line: ##

temp_list = [15, 22, -5, 38, 42, 10, -12]

freeze_temp = []
normal_temp = []
heat_temp   = []

for i in temp_list:
    if i < 0:
        print(f"{i}°C : Freezing warning!")
    elif i in range(0,36):
        print(f"{i}°C : Normal conditions.")
    else:
        print(f"{i}°C : Heatwave warning!")