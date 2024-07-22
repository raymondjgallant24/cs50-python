import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define the schedule with days and activities
times = [
    "5:00 AM", "5:15 AM", "5:30 AM", "5:45 AM", "6:00 AM", "6:15 AM", "6:30 AM", "6:45 AM", "7:00 AM",
    "7:15 AM", "7:30 AM", "7:45 AM", "8:00 AM", "8:15 AM", "8:30 AM", "8:45 AM", "9:00 AM", "9:15 AM",
    "9:30 AM", "9:45 AM", "10:00 AM", "10:15 AM", "10:30 AM", "10:45 AM", "11:00 AM", "11:15 AM", "11:30 AM",
    "11:45 AM", "12:00 PM", "12:15 PM", "12:30 PM", "12:45 PM", "1:00 PM", "1:15 PM", "1:30 PM", "1:45 PM",
    "2:00 PM", "2:15 PM", "2:30 PM", "2:45 PM", "3:00 PM", "3:15 PM", "3:30 PM", "3:45 PM", "4:00 PM",
    "4:15 PM", "4:30 PM", "4:45 PM", "5:00 PM", "5:15 PM", "5:30 PM", "5:45 PM", "6:00 PM", "6:15 PM",
    "6:30 PM", "6:45 PM", "7:00 PM", "7:15 PM", "7:30 PM", "7:45 PM", "8:00 PM", "8:15 PM", "8:30 PM",
    "8:45 PM", "9:00 PM", "9:15 PM", "9:30 PM", "9:45 PM", "10:00 PM", "10:15 PM", "10:30 PM", "10:45 PM",
    "11:00 PM", "11:15 PM", "11:30 PM", "11:45 PM"
] * 7

activities = [
    "Wake Up", "Ice Bath", "Morning Meditation", "Strength Training", "Strength Training", "Strength Training",
    "Strength Training", "Strength Training", "Cool Down and Shower", "Cool Down and Shower", "Cool Down and Shower",
    "Breakfast", "Breakfast", "Breakfast", "Stretching/Yoga", "Stretching/Yoga", "Aqua Aerobics (MW) / Rest",
    "Aqua Aerobics (MW) / Rest", "Online Class: Programming Fundamentals", "Online Class: Programming Fundamentals",
    "Online Class: Programming Fundamentals", "Online Class: Programming Fundamentals", "Online Class: Programming Fundamentals",
    "Online Class: Programming Fundamentals", "Online Class: Programming Fundamentals Laboratory", "Online Class: Programming Fundamentals Laboratory",
    "Online Class: Programming Fundamentals Laboratory", "Online Class: Programming Fundamentals Laboratory", "Online Class: Programming Fundamentals Laboratory",
    "Online Class: Programming Fundamentals Laboratory", "Focused Work/Study Time", "Focused Work/Study Time", "Focused Work/Study Time",
    "Focused Work/Study Time", "Break", "Break", "Online Class: Firewalls and How They Work", "Online Class: Firewalls and How They Work",
    "Online Class: Firewalls and How They Work", "Online Class: Firewalls and How They Work", "Online Class: Firewalls and How They Work",
    "Online Class: Firewalls and How They Work", "Online Class: Firewalls and How They Work", "College Algebra", "College Algebra",
    "College Algebra", "College Algebra", "Lunch", "Lunch", "Lunch", "Online Class: National Cyber League (NCL)",
    "Online Class: National Cyber League (NCL)", "Online Class: National Cyber League (NCL)", "Online Class: National Cyber League (NCL)",
    "Online Class: National Cyber League (NCL)", "Online Class: National Cyber League (NCL)", "Deep Work/Study Session", "Deep Work/Study Session",
    "Deep Work/Study Session", "Deep Work/Study Session", "Cool Down and Stretching", "Cool Down and Stretching", "Post-Workout Nutrition",
    "Post-Workout Nutrition", "HIIT Training", "HIIT Training", "HIIT Training", "HIIT Training", "HIIT Training", "HIIT Training",
    "HIIT Training", "Dinner", "Dinner", "Dinner", "College Algebra Homework", "College Algebra Homework", "Leisure/Relaxation",
    "Leisure/Relaxation", "Evening Meditation", "Evening Meditation", "Plan for Tomorrow", "Plan for Tomorrow", "Wind Down", "Wind Down",
    "Bedtime Routine", "Bedtime Routine", "Sleep", "Sleep", "Sleep"
] * 7

days = ["Monday"] * 75 + ["Tuesday"] * 75 + ["Wednesday"] * 75 + ["Thursday"] * 75 + ["Friday"] * 75 + ["Saturday"] * 75 + ["Sunday"] * 75

# Adjust for specific days
for i in range(7):
    if i == 0:  # Monday
        activities[i * 75 + 47] = "Fraternity Meeting"
    if i == 2:  # Wednesday
        activities[i * 75 + 16] = "Aqua Aerobics"
    if i in [5, 6]:  # Saturday and Sunday
        activities[i * 75 + 16] = "Rest Day"
        activities[i * 75 + 17] = "Rest Day"

# Create a DataFrame
df = pd.DataFrame({"Time": times, "Activity": activities, "Day": days})

# Color coding based on activity type
colors = {
    "Wake Up": "#FFDDC1", "Ice Bath": "#FFABAB", "Morning Meditation": "#FFC3A0", "Strength Training": "#FF677D", 
    "Cool Down and Shower": "#D4A5A5", "Breakfast": "#392F5A", "Stretching/Yoga": "#31A2AC", 
    "Online Class: Programming Fundamentals": "#61C0BF", "Online Class: Programming Fundamentals Laboratory": "#6B4226", 
    "Focused Work/Study Time": "#D9BF77", "Break": "#ACD8AA", 
    "Online Class: Firewalls and How They Work": "#FFD3B5", "College Algebra": "#E8A87C", 
    "Lunch": "#C38D9E", "Online Class: National Cyber League (NCL)": "#41B3A3", "Deep Work/Study Session": "#E27D60", 
    "Cool Down and Stretching": "#85DCB0", "Post-Workout Nutrition": "#E8A87C", 
    "HIIT Training": "#7FB3D5", "Online Class: Ethical Hacking, Network Defense, and Counter Measures": "#C38D9E", "Dinner": "#41B3A3", 
    "College Algebra Homework": "#E27D60", "Leisure/Relaxation": "#85DCB0", "Evening Meditation": "#FFDDC1", 
    "Plan for Tomorrow": "#FFABAB", "Wind Down": "#FFC3A0", "Bedtime Routine": "#FF677D", "Sleep": "#D4A5A5",
    "Fraternity Meeting": "#A7226E", "Rest Day": "#2A4D69"
}

# Add a color column
df["Color"] = df["Activity"].map(colors)

# Create a pivot table
pivot_df = df.pivot("Time", "Day", "Activity")

# Create color mapping for pivot table
color_map = df.pivot("Time", "Day", "Color").values

# Plot the schedule
fig, ax = plt.subplots(figsize=(15, 18))

# Create the table with color coding
the_table = ax.table(cellText=pivot_df.values, rowLabels=pivot_df.index, colLabels=pivot_df.columns, cellLoc='center', loc='center',
                     cellColours=color_map)

# Adjust layout
ax.axis('off')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(1.2, 1.2)

# Title
plt.title('Weekly Schedule', fontsize=16)

# Display the plot
plt.tight_layout()
plt.show()
