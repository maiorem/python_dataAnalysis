import fah_converter

print("Enter a celsius value :")
celsius=float(input())
fahrenheit=fah_converter.convert_c_to_f(celsius)
print("That's ", fahrenheit, " degrees Fahrenheit.")