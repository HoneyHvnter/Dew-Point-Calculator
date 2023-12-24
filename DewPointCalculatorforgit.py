#Dew Point Calculator

                                                                            #Introduction
print('Welcome to the Dew Point Calculator Program.')
print('Dew point directly coorelates to how comfortable it is outside.')
print()

air_temperature_fahrenheit = float(input('Please enter the current temperature in Degree fahrenheit (example 81.0):'))     #First input
print()

relative_humidity = float(input('Please enter the current relatative humidity percentage (example 84.0):'))     #Second input
print()


dew_point = air_temperature_fahrenheit - ((100 - relative_humidity)/5)     #Dew point formula 

print('The dew point is', dew_point, 'degrees fahrenheit.')                 #Final output