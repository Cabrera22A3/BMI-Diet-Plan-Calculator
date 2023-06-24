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
'''
# LOGIN - Temporary Feature
def login():
    username = str("admin")
    password = str("123456")
    print()
    attempts = 3
    for password_ in range(1, 4):

        print("Your Current Attempt(s):", attempts)
        user_username = str(input("Enter your username: "))
        user_password = str(input("Enter your password: "))
        print()
        if user_username == username and user_password == password:
            print("You Logged in Successfully!")
            break
        elif user_username != username and user_password == password:
            print("Your Username is Invalid!")
        elif user_username == username and user_password != password:
            print("Your Password is Invalid!")
        elif user_username != username and user_password != password:
            print("Both Username and Password are Invalid!")

        attempts = attempts - 1

login()
print("Loading...")

'''
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
    print("   Your Current BMI is: ", BMI.__round__(2))
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
    print("||          • Eat a variety of nutrient-dense foods to meet your body's needs. Includes      ||")
    print("||            fruits, vegetables, whole grains, lean proteins, and healthy fats in           ||")
    print("||            your meals.                                                                    ||")
    print("||          • Each night, aim for 7-9 hours of quality sleep.                                ||")
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
    print("||          • For Men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For Women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
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
    print("||          • Focus on consuming a balanced diet that includes a variety of whole,           ||")
    print("||            unprocessed foods.                                                             ||")
    print("||          • Be mindful of portion sizes to avoid overeating. Use smaller plates and        ||")
    print("||            bowls, and be aware of recommended serving sizes.                              ||")
    print("||          • Aim for 7-9 hours of quality sleep each night.                                 ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Vegetable omelet made with 2 egg whites and 1 whole egg, mixed with        ||")
    print("||                spinach, bell peppers, and onions.                                         ||")
    print("||              - Yogurt topped with fresh berries, a sprinkle of nuts or seeds, and         ||")
    print("||                a drizzle of honey or a dollop of nut butter.                              ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Whole-wheat wrap filled with lean turkey or grilled vegetables, along      ||")
    print("||                with lettuce, tomato, and hummus.                                          ||")
    print("||              - Lentil or chickpea soup with a side of mixed green salad and a slice of    ||")
    print("||                whole-grain bread.                                                         ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Grilled salmon or baked chicken breast, served with roasted vegetables     ||")
    print("||                and a small portion of quinoa or sweet potato.                             ||")
    print("||              - Zucchini noodles with a tomato-based sauce and a side salad.               ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For Men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For Women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
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
    print("||          • Aim for gradual and sustainable weight loss through a combination of healthy   ||")
    print("||            eating and regular physical activity.                                          ||")
    print("||          • Focus on adopting a balanced and nutritious eating plan.                       ||")
    print("||          • Avoid crash diets or extreme measures that are difficult to maintain.          ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Veggie scramble made with egg whites or egg substitute, sautéed vegetables ||")
    print("||                and a sprinkle of low-fat cheese.                                          ||")
    print("||              - Whole-grain oatmeal cooked with skim milk or plant-based milk, topped with ||")
    print("||                sliced bananas and a sprinkle of cinnamon.                                 ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Roasted vegetables, salsa, and a dollop of Greek yogurt or guacamole.      ||")
    print("||              - Grilled chicken breast or baked fish, served with a generous portion of    ||")
    print("||                mixed green salad                                                          ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Steamed green beans as a side dish.                                        ||")
    print("||              - Grilled chicken breast with a flavorful spice rub.                         ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For Men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For Women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
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
    print("***********************************************************************************************")
    print("||                                                                                           ||")
    print("||     Goals:                                                                                ||")
    print("||          • A realistic target could be losing 10-20% of your current body weight over a   ||")
    print("||            period of six months to a year.                                                ||")
    print("||          • Learn to manage portion sizes to avoid overeating.                             ||")
    print("||          • Make sustainable lifestyle changes to support your weight loss efforts.        ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Greek yogurt topped with mixed berries, a sprinkle of nuts or seeds, and a ||")
    print("||                drizzle of honey or a small amount of granola.                             ||")
    print("||              - Veggie omelet made with egg whites or egg substitute, filled with spinach, ||")
    print("||                bell peppers, onions, and mushrooms.                                       ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Whole wheat wrap filled with lean protein, mixed greens, tomatoes, and a   ||")
    print("||                smear of avocado or hummus.                                                ||")
    print("||              - Mixed green salad with a variety of colorful vegetables, grilled shrimp    ||")
    print("||                or tofu, and a light vinaigrette dressing.                                 ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Stir-fried vegetables with lean protein served over brown rice or quinoa.  ||")
    print("||              - Baked salmon or grilled chicken breast with roasted sweet potatoes and     ||")
    print("||                steamed broccoli.                                                          ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For Men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For Women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
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
    print("||          • It's crucial to consult a healthcare professional, such as a doctor,           ||")
    print("||            registered dietitian, or obesity specialist.                                   ||")
    print("||          • To get a weight loss goal of 1-2 pounds (0.5-1 kg) per week is considered      ||")
    print("||            healthy.                                                                       ||")
    print("||          • Prioritize improving your overall health.                                      ||")
    print("||                                                                                           ||")
    print("||     Meal Planning:                                                                        ||")
    print("||          • Breakfast:                                                                     ||")
    print("||              - Prepare an omelet with egg whites or a combination of whole eggs and egg   ||")
    print("||                whites, loaded with a variety of vegetables such as spinach, bell peppers, ||")
    print("||                onions, and mushrooms.                                                     ||")
    print("||          • Lunch:                                                                         ||")
    print("||              - Start with a bed of mixed greens and add grilled chicken breast, cherry    ||")
    print("||                tomatoes, cucumber slices, shredded carrots, and any other non-starchy     ||")
    print("||                vegetables you prefer.                                                     ||")
    print("||          • Dinner:                                                                        ||")
    print("||              - Season a salmon fillet with herbs, lemon juice, and a little olive oil.    ||")
    print("||                                                                                           ||")
    print("||     Hydration:                                                                            ||")
    print("||          • For Men: Approximately 3.7 liters (or about 13 cups) of total water intake     ||")
    print("||            per day from all beverages and foods                                           ||")
    print("||          • For Women: Approximately 2.7 liters (or about 9 cups) of total water intake    ||")
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

ret = str("Y")
while ret != "N":
    print("||                                                                                           ||")
    print("||                          Have you Calculated your BMI already?                            ||")
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
        print("||                                                                                           ||")

    # BMI na kasama yung naunang BMI Results
    if ThisChoice == "Y":
        print("***********************************************************************************************")
        print("||                                                                                           ||")
        print("||                              KINDLY ENTER YOUR PAST RESULTS:                              ||")
        print("||                                                                                           ||")
        print("***********************************************************************************************")
        print()
        PastBmiRes = float(input("   Past BMI Results: "))
        PastDays = float(input("   Past Day(s): "))
        print()
        calcBMI = calculate_current_bmi().__round__(2)
        Rounded_PastBmiRes = PastBmiRes.__round__(2)
        if calcBMI == Rounded_PastBmiRes:
            print("   Your Current BMI (", calcBMI, ") and your BMI (", Rounded_PastBmiRes, ") in the past",
                  PastDays, "day(s), Doesn't Change.")
        elif calcBMI > Rounded_PastBmiRes:
            print("   Your Current BMI (", calcBMI, ") was Greater than your BMI (", Rounded_PastBmiRes, ") in the past",
                  PastDays, "day(s).")
        elif calcBMI < Rounded_PastBmiRes:
            print("   Your Current BMI (", calcBMI, ") was Smaller than your BMI (", Rounded_PastBmiRes, ") in the past",
                  PastDays, "day(s).")
        print()
        deter_weight()
        print()
        ret = str.upper(input("   Would you like to Re-Run the Program? (Y) Yes or (N) No: "))
        print()
        greet_comeback()

    # BMI na para sa magcacalculate palang ng BMI
    elif ThisChoice == "N":
        calcBMI = calculate_current_bmi().__round__(2)
        # nagdedetermine kung anong weight meron ka
        print()
        deter_weight()
        print()
        ret = str.upper(input("   Would you like to Re-Run the Program? (Y) Yes or (N) No: "))
        print()
        greet_comeback()
