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

def calculate_current_bmi():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                         KINDLY ANSWER THE FOLLOWING REQUIREMENTS:                         ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    # calculations sa BMI
    BmiMassKG = float(input("Enter your Current Mass in (Kilogram(s)): "))
    BmiHeightCM = float(input("Enter your Current Height in (Centimeter(s)): "))
    BmiHeightM = (BmiHeightCM * .01)
    BMI = (BmiMassKG / (BmiHeightM * BmiHeightM))
    print("Your Current BMI is: ", BMI.__round__(2))
    return BMI

def und_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                     [ UNDER WEIGHT ]                                      ||")
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
    print("||          • Lunch:                                                                         ||")
    print("||              - Grilled chicken or fish                                                    ||")
    print("||              - Steamed vegetables (broccoli, carrots, etc.)                               ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Lean protein (chicken, turkey, tofu) or legumes (lentils, chickpeas)       ||")
    print("||              - Baked sweet potato or whole wheat pasta                                    ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For Men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For Women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Do 50 Squats per Day                                                           ||")
    print("||          • Do 50 Pull-Ups per Day                                                         ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week comeback again to Calculate you BMI                               ||")
    print("||          • If you notices that you adds some weight comeback again to calculate your BMI  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def norm_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                    [ NORMAL WEIGHT ]                                      ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Vegetable omelet made with egg whites or whole eggs, filled with spinach,  ||")
    print("||                bell peppers, and mushrooms.                                               ||")
    print("||              - Greek yogurt topped with mixed berries, a sprinkle of granola, and a       ||")
    print("||                drizzle of honey.                                                          ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Grilled chicken breast with a side of quinoa or brown rice, steamed        ||")
    print("||                broccoli, and a mixed green salad with cherry tomatoes and a light         ||")
    print("||                vinaigrette.                                                               ||")
    print("||              - Whole grain wrap filled with lean turkey or tofu, lettuce, tomato,         ||")
    print("||                avocado slices, and a spread of hummus.                                    ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Baked salmon seasoned with herbs and lemon juice, accompanied by roasted   ||")
    print("||                sweet potatoes, steamed asparagus, and a side of quinoa or whole wheat     ||")
    print("||                couscous.                                                                  ||")
    print("||              - Stir-fried tofu or lean beef with mixed vegetables (such as broccoli, bell ||")
    print("||                peppers, and snap peas) in a light soy sauce and garlic sauce.             ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Do 50 Push-Ups every Morning                                                   ||")
    print("||          • Do 50 Jumping Jacks every Morning                                              ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week comeback again to Calculate you BMI                               ||")
    print("||          • If you notices that you adds some weight comeback again to calculate your BMI  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def ove_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                     [ OVER WEIGHT ]                                       ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Do Jogging every Morning                                                       ||")
    print("||          • Do Bench Press every Morning                                                   ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week comeback again to Calculate you BMI                               ||")
    print("||          • If you notices that you adds some weight comeback again to calculate your BMI  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def ob1_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                   [ OBESITY CLASS I ]                                     ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Do Cardio Vascular Exercises, Jogging, Cycling, Swimming, Zumba, or Dancing    ||")
    print("||          • Do Strength Training Resistance Workouts, Circuit Training, or Squats          ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week comeback again to Calculate you BMI                               ||")
    print("||          • If you notices that you adds some weight comeback again to calculate your BMI  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def ob2_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                   [ OBESITY CLASS II ]                                    ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Do Hiking: Explore nature trails and gradually increase the difficulty         ||")
    print("||            level as your fitness improves                                                 ||")
    print("||          • Do Recreational Sports: Engage in low-impact Sports such as Golf, Tennis,      ||")
    print("||            or Swimming                                                                    ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week comeback again to Calculate you BMI                               ||")
    print("||          • If you notices that you adds some weight comeback again to calculate your BMI  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def ext_weight():
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                                    [ EXTREME OBESITY ]                                    ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||                                                                                           ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||                                                                                           ||")
    print("||     Physical Activity:                                                                    ||")
    print("||          • Do Seated Exercises: Perform seated exercises that target different muscle     ||")
    print("||            groups, using resistance bands or light weights                                ||")
    print("||          • Do Stationary Cycling: Utilize a stationary Bike, which supports your weight   ||")
    print("||            and places less stress on the joints                                           ||")
    print("||                                                                                           ||")
    print("||     Monitoring:                                                                           ||")
    print("||          • After a week comeback again to Calculate you BMI                               ||")
    print("||          • If you notices that you adds some weight comeback again to calculate your BMI  ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")

def deter_weight():
    # nagdedetermine kung anong weight meron ka
    if calcBMI < 18.5:
        und_weight()
    elif 18.5 <= calcBMI <= 24.9:
        norm_weight()
    elif 25 <= calcBMI <= 29.9:
        ove_weight()
    elif 30 <= calcBMI <= 34.9:
        ob1_weight()
    elif 35 <= calcBMI <= 39.9:
        ob2_weight()
    elif calcBMI >= 40:
        ext_weight()

# TIPS - Temporary Feature para sa program
def greet_comeback():
    import random
    Tips = [
        # TIPS #1
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||                Don't be pressured that the changes in BMI should be sudden                ||\n"
        "||                           Just Trust the Process - Vince Aranas                           ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #2
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||          Engage in hobbies or activities that help you unwind and reduce stress.          ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #3
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||        Practice relaxation techniques, such as deep breathing, meditation, or yoga.       ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #4
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||   This could include reading, taking a bath, listening to music, practicing mindfulness,  ||\n"
        "||                      or any other activities that promote self-care.                      ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #5
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||     Take time for yourself and engage in activities that bring you joy and relaxation.    ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #6
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||            Be patient with yourself and celebrate small victories along the way.          ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #7
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||                 Treat yourself with kindness and practice self-compassion.                ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        # TIPS #8
        "***********************************************************************************************\n"
        "||                                                                                           ||\n"
        "||              Remember that achieving a healthy body takes time and effort.                ||\n"
        "||                                                                                           ||\n"
        "***********************************************************************************************",
        ]
    print(random.choice(Tips))

ret = str("Y")
while ret != "N":
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||                          Have you Calculated your BMI already?                            ||")
    print("||                                                                                           ||")
    print("||                                       (Y) YES                                             ||")
    print("||                                                                                           ||")
    print("||                                       (N) NO                                              ||")
    print("||                                                                                           ||")
    print("***********************************************************************************************")
    Choice = str.upper(input("Your Choice: "))
    ThisChoice = Choice
    if ThisChoice != "Y" and ThisChoice != "N":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                                     [ INVALID INPUT ]                                     ||")
        print("||                                                                                           ||")

    # BMI na kasama yung naunang BMI Results
    if ThisChoice == "Y":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                              KINDLY ENTER YOUR PAST RESULTS:                              ||")
        print("||                                                                                           ||")
        print("***********************************************************************************************")
        PastBmiRes = float(input("Past BMI Results: "))
        PastDays = float(input("Past Day(s): "))
        calcBMI = calculate_current_bmi().__round__(2)
        Rounded_PastBmiRes = PastBmiRes.__round__(2)
        if calcBMI == Rounded_PastBmiRes:
            print("Your Current BMI (", calcBMI, ") and your BMI (", Rounded_PastBmiRes, ") in the past",
                  PastDays, "day(s), Doesn't Change.")
        elif calcBMI > Rounded_PastBmiRes:
            print("Your Current BMI (", calcBMI, ") was Greater than your BMI (", Rounded_PastBmiRes, ") in the past",
                  PastDays, "day(s).")
        elif calcBMI < Rounded_PastBmiRes:
            print("Your Current BMI (", calcBMI, ") was Smaller than your BMI (", Rounded_PastBmiRes, ") in the past",
                  PastDays, "day(s).")
        deter_weight()
        ret = str.upper(input("Would you like to Re-Run the Program? (Y) Yes or (N) No: "))
        greet_comeback()

    # BMI na para sa magcacalculate palang ng BMI
    elif ThisChoice == "N":
        calcBMI = calculate_current_bmi().__round__(2)
        # nagdedetermine kung anong weight meron ka
        deter_weight()
        ret = str.upper(input("Would you like to Re-Run the Program? (Y) Yes or (N) No: "))
        greet_comeback()
