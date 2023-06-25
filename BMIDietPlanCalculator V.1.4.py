def greet_comeback():
    import random
    Tips = [
        # TIPS #1
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||            Tips: Don't be pressured that the changes in BMI should be sudden              ||\n"
        "||                         Just Trust the Process - Vince Aranas                             ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #2
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||      Tips: Engage in hobbies or activities that help you unwind and reduce stress.        ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #3
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||    Tips: Practice relaxation techniques, such as deep breathing, meditation, or yoga.     ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #4
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||         Tips: Just calm down and try reading, taking a bath, listening to music,          ||\n"
        "||          practicing mindfulness, or any other activities that promote self-care.          ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #5
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||  Tips: Take time for yourself and engage in activities that bring you joy and relaxation. ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #6
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||         Tips: Be patient with yourself and celebrate small victories along the way.       ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #7
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||             Tips: Treat yourself with kindness and practice self-compassion.              ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #8
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||           Tips: Remember that achieving a healthy body takes time and effort.             ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        ]
    print(random.choice(Tips))

def rerun_program():
    print()
    ret = str.upper(input("   Would you like to Re-Run the Program? (Y) Yes or (N) No: "))
    print()
    if ret != "Y" and ret != "N":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                                     [ INVALID INPUT ]                                     ||")
        rerun_program()
    if ret == "Y":
        greet_comeback()
        print()
        print("***********************************************************************************************")
        age_deter()
    elif ret == "N":
        greet_comeback()

def men_und_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                  [ UNDER WEIGHT - MALE ]                                  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||          • Increase caloric intake to create a calorie surplus for weight gain            ||")
    print("||          • Focus on consuming nutrient-dense foods that provide essential vitamins        ||")
    print("||            and minerals                                                                   ||")
    print("||          • Prioritize protein intake to support muscle development and repair             ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Whole grain cereal or oatmeal with milk or yogurt                          ||")
    print("||              - Sliced banana or other fruits                                              ||")
    print("||          • Snack:                                                                         ||")
    print("||              - Greek yogurt with mixed berries                                            ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Grilled chicken or fish                                                    ||")
    print("||              - Quinoa or brown rice                                                       ||")
    print("||              - Steamed vegetables (broccoli, carrots, etc.)                               ||")
    print("||          • Snack:                                                                         ||")
    print("||              - Almonds or other nuts and seeds                                            ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Lean protein (chicken, turkey, beef) or legumes (lentils, chickpeas)       ||")
    print("||              - Baked sweet potato or whole wheat pasta                                    ||")
    print("||              - Mixed green salad with vinaigrette dressing                                ||")
    print("||          • Snack:                                                                         ||")
    print("||              - Protein shake with fruits and almond butter                                ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • Approximately 3.7 liters (or about 13 cups) of total water intake per day      ||")
    print("||            from all beverages and foods                                                   ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Engage in regular strength training exercises to build muscle                  ||")
    print("||          • Include cardio exercises like jogging or cycling for overall fitness           ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week, come back to calculate your BMI                                  ||")
    print("||          • If you notice that you've gained some weight, come back again to calculate     ||")
    print("||            your BMI                                                                       ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")


def men_norm_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                 [ NORMAL WEIGHT - MALE]                                   ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def men_ove_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                  [ OVER WEIGHT - MALE]                                    ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def men_ob1_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                [ OBESITY CLASS I - MALE]                                  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def men_ob2_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                [ OBESITY CLASS II - MALE]                                 ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def men_ext_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                 [ EXTREME OBESITY - MALE]                                 ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def fem_und_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                 [ UNDER WEIGHT - FEMALE]                                  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||          • Increase caloric intake to create a calorie surplus for weight gain            ||")
    print("||          • Focus on consuming nutrient-dense foods that provide essential vitamins        ||")
    print("||            and minerals                                                                   ||")
    print("||          • Prioritize protein intake to support muscle development and repair             ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Whole grain cereal or oatmeal with milk or yogurt                          ||")
    print("||              - Sliced banana or other fruits                                              ||")
    print("||          • Snack:                                                                         ||")
    print("||              - Greek yogurt with mixed berries                                            ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Grilled chicken or fish                                                    ||")
    print("||              - Quinoa or brown rice                                                       ||")
    print("||              - Steamed vegetables (broccoli, carrots, etc.)                               ||")
    print("||          • Snack:                                                                         ||")
    print("||              - Almonds or other nuts and seeds                                            ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Lean protein (chicken, turkey, tofu) or legumes (lentils, chickpeas)       ||")
    print("||              - Baked sweet potato or whole wheat pasta                                    ||")
    print("||              - Mixed green salad with vinaigrette dressing                                ||")
    print("||          • Snack:                                                                         ||")
    print("||              - Protein smoothie with fruits and almond milk                               ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • Approximately 2.7 liters (or about 9 cups) of total water intake per day       ||")
    print("||            from all beverages and foods                                                   ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Engage in regular strength training exercises to build muscle                  ||")
    print("||          • Include cardio exercises like jogging or cycling for overall fitness           ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week, come back to calculate your BMI                                  ||")
    print("||          • If you notice that you've gained some weight, come back again to calculate     ||")
    print("||            your BMI                                                                       ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")


def fem_norm_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                [ NORMAL WEIGHT - FEMALE]                                  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def fem_ove_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                 [ OVER WEIGHT - FEMALE]                                   ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def fem_ob1_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                               [ OBESITY CLASS I - FEMALE]                                 ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def fem_ob2_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                               [ OBESITY CLASS II - FEMALE]                                ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def fem_ext_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                [ EXTREME OBESITY - FEMALE]                                ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")


def calculate_current_bmi():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                         KINDLY ANSWER THE FOLLOWING REQUIREMENTS:                         ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    # calculations sa BMI
    print()
    BmiMassKG = float(input("   Enter your Current Mass in (Kilogram(s)): "))
    BmiHeightCM = float(input("   Enter your Current Height in (Centimeter(s)): "))
    BmiHeightM = (BmiHeightCM * .01)
    BMI = (BmiMassKG / (BmiHeightM * BmiHeightM))
    print("   Your Current BMI is: ", BMI.__round__(1))
    return BMI

def current_or_past():
    print("||                                                                                           ||")
    print("||                          Have you Calculated your BMI before?                             ||")
    print("||                                                                                           ||")
    print("||                                       (Y) YES                                             ||")
    print("||                                                                                           ||")
    print("||                                       (N) NO                                              ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print()
    Choice = str.upper(input("   Your Choice: "))
    print()
    ThisChoice = Choice
    if ThisChoice != "Y" and ThisChoice != "N":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                                     [ INVALID INPUT ]                                     ||")
        current_or_past()
    if ThisChoice == "Y":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                              KINDLY ENTER YOUR PAST RESULTS:                              ||")
        print("||                                                                                           ||")
        print("***********************************************************************************************")
        print()
        PastBmiRes = float(input("   Past BMI Results: "))
        print()
        calcBMI = calculate_current_bmi().__round__(1)
        Rounded_PastBmiRes = PastBmiRes.__round__(1)
        if calcBMI == Rounded_PastBmiRes:
            print("   Your Current BMI (", calcBMI, ") and your Past BMI (", Rounded_PastBmiRes, ") Doesn't Change.")
        elif calcBMI > Rounded_PastBmiRes:
            print("   Your Current BMI (", calcBMI, ") was Greater than your Past BMI (", Rounded_PastBmiRes, ").")
        elif calcBMI < Rounded_PastBmiRes:
            print("   Your Current BMI (", calcBMI, ") was Smaller than your Past BMI (", Rounded_PastBmiRes, ").")
        print()
        gen = Choice_gender
        if gen == "M":
            if calcBMI < 18.5:
                men_und_weight()
            elif 18.5 <= calcBMI <= 24.9:
                men_norm_weight()
            elif 25 <= calcBMI <= 29.9:
                men_ove_weight()
            elif 30 <= calcBMI <= 34.9:
                men_ob1_weight()
            elif 35 <= calcBMI <= 39.9:
                men_ob2_weight()
            elif calcBMI >= 40:
                men_ext_weight()
        elif gen == "F":
            if calcBMI < 18.5:
                fem_und_weight()
            elif 18.5 <= calcBMI <= 24.9:
                fem_norm_weight()
            elif 25 <= calcBMI <= 29.9:
                fem_ove_weight()
            elif 30 <= calcBMI <= 34.9:
                fem_ob1_weight()
            elif 35 <= calcBMI <= 39.9:
                fem_ob2_weight()
            elif calcBMI >= 40:
                fem_ext_weight()
        # BMI na para sa magcacalculate palang ng BMI
    elif ThisChoice == "N":
        calcBMI = calculate_current_bmi().__round__(1)
        print()
        gen = Choice_gender
        if gen == "M":
            if calcBMI < 18.5:
                men_und_weight()
            elif 18.5 <= calcBMI <= 24.9:
                men_norm_weight()
            elif 25 <= calcBMI <= 29.9:
                men_ove_weight()
            elif 30 <= calcBMI <= 34.9:
                men_ob1_weight()
            elif 35 <= calcBMI <= 39.9:
                men_ob2_weight()
            elif calcBMI >= 40:
                men_ext_weight()
        elif gen == "F":
            if calcBMI < 18.5:
                fem_und_weight()
            elif 18.5 <= calcBMI <= 24.9:
                fem_norm_weight()
            elif 25 <= calcBMI <= 29.9:
                fem_ove_weight()
            elif 30 <= calcBMI <= 34.9:
                fem_ob1_weight()
            elif 35 <= calcBMI <= 39.9:
                fem_ob2_weight()
            elif calcBMI >= 40:
                fem_ext_weight()

def biological_gender():
    global Choice_gender
    print("||                                                                                           ||")
    print("||                           Kindly enter your Biological Gender:                            ||")
    print("||                                                                                           ||")
    print("||                                       (M) MALE                                            ||")
    print("||                                                                                           ||")
    print("||                                       (F) FEMALE                                          ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print()
    Choice_gender = str.upper(input("   Your Choice: "))
    print()
    if Choice_gender != "M" and Choice_gender != "F":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                                     [ INVALID INPUT ]                                     ||")
        biological_gender()
    if Choice_gender == "M":
        print("***********************************************************************************************")
        current_or_past()
    elif Choice_gender == "F":
        print("***********************************************************************************************")
        current_or_past()
    rerun_program()

def age_deter():
    print("||                                                                                           ||")
    print("||              THIS BMI DIET PLAN IS ONLY FOR ADULTS 18 YEARS OF AGE AND OLDER              ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print()
    age = int(input("   Kindly Enter your Age: "))
    print()
    if age < 1:
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                                     [ INVALID INPUT ]                                     ||")
        age_deter()
    elif age < 18:
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||             [ We apologize, but this program is not compatible with minors ]              ||")
        age_deter()
    else:
        print("***********************************************************************************************")
        biological_gender()

from datetime import datetime
date = datetime.now().strftime("%d%m%Y%H%M%S")
dateformat = datetime.now().strftime("%d-%m-%y %H:%M:%S")

print()
print("                                  [ LYCEUM OF ALABANG ]")
print(" ")
print("                [ Km.30 National Road, Tunasan, Muntinlupa, 1773 Metro Manila ]")
print(" ")
print("                          [ WELCOME TO BMI DIET PLAN CALCULATOR ]")
print(" ")
print("                                   [", dateformat, "]")
print(" ")
print("***********************************************************************************************")
age_deter()