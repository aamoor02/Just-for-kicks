import datetime 
import re

first_name = input('what is your first name?\n').upper()
last_name = input('what is your last name?\n').upper()
dob = input("What is your date of birth? Please enter in MM/DD/YYYY format.\n")
birthday = datetime.datetime.strptime(dob, '%m-%d-%Y')
height = input('what is your height in inches?\n')
weight = input('what is your weight in pounds?\n')
email = input("What is your email address? \n")



def convert_to_kilogram(user_weight):
    ''' convert user provided weight into kilograms '''
    converted_weight = float(user_weight) * 0.453592
    new_weight = int(converted_weight)
    return new_weight

def convert_to_meters(user_height):
    ''' convert user provided height into meters '''
    converted_height = float(user_height) * .0254
    return converted_height


def print_info():
    print("Your name is {} {}".format(first_name, last_name))
    print("Your birthday is {}-{}-{}".format(birthday.month,birthday.day,birthday.year))
    print("your weight in kilograms is {}.".format(convert_to_kilogram(weight)))
    print("Your height in meters is {}".format(convert_to_meters(height)))
    print("Your email address is {}.".format(check_email(email)))
    

def check_email(user_email):
    ''' Validate correct email formatting '''
    if re.findall(r'[-\w\d+.]+@[-\w\d.]+', user_email):
        print("Your email address is valid!")
        list = re.findall(r'[-\w\d+.]+@[-\w\d.]+', user_email)
        return list[0]
    else:
        print("Your email address is invalid")
    

print_info()


