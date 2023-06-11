# Write your code below this line 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / (height_as_float ** 2)

bmi_as_float = float(bmi)

if bmi_as_float < 18.5:

    print(f" your bmi is {bmi_as_float},you are underweight  ")
elif 25 > bmi_as_float:

    print(f" your bmi is {bmi_as_float},you are normal weight  ")
elif bmi_as_float <= 30:
    print(f" your bmi is {bmi_as_float},you are slightly overweight  ")
elif bmi_as_float <= 35:
    print(f" your bmi is {bmi_as_float},you are obese ")
else:
    print(f" your bmi is {bmi_as_float}, you are clinically obese.  ")



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
