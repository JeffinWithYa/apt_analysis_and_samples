import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

ASPECT_RATIO_10_INCH_WIDE = 10
ASPECT_RATIO_6_INCH_TALL = 6
X_AXIS_INTERVAL_1 = 1
TARGET_PROGRESS_START_0 = 0
TARGET_PROGRESS_END_14 = 14
X_AXIS_LABEL = "Date"
Y_AXIS_LABEL = "Reports Completed"
GRAPH_TITLE = "MCTI 6530 Submission 2 Progress Tracker"
PROGRESS_TRACKER_FILE_BASE = "progress_tracker_with_dates_day"
FILE_EXTENSION_PNG = ".png"


TARGET = "Target"
DASHED_LINE_STYLE = "--"
SET_1_APT_RANGE_1_TO_13 = "apt_1_to_13"
SET_2_APT_RANGE_14_TO_26 = "apt_14_to_26"
SET_3_APT_RANGE_27_TO_40 = "apt_27_to_40"

YEAR_2024 = 2024
MONTH_SEPT = 9
DATE_SEPT_29 = 29
DATE_OCT_10 = 10
MONTH_OCT = 10
DATE_OCT_14 = 14
DATE_OCT_28 = 28


# Create date range from September 29th to October 10th
start_date = datetime(YEAR_2024, MONTH_OCT, DATE_OCT_14)
end_date = datetime(YEAR_2024, MONTH_OCT, DATE_OCT_28)
date_range = pd.date_range(start=start_date, end=end_date)

# Target progress for each day
target = np.linspace(
    TARGET_PROGRESS_START_0, TARGET_PROGRESS_END_14, len(date_range))

# Initialize progress for each person
progress_data = {
    SET_1_APT_RANGE_1_TO_13: [],
    SET_2_APT_RANGE_14_TO_26: [],
    SET_3_APT_RANGE_27_TO_40: []
}

# Track the days passed
days_passed = []


# Function to update progress dynamically and expand arrays
def update_progress(apt_set1, apt_set2,
                    apt_set3, day):
    if len(progress_data[SET_1_APT_RANGE_1_TO_13]) < day+1:
        progress_data[SET_1_APT_RANGE_1_TO_13].append(apt_set1)
        progress_data[SET_2_APT_RANGE_14_TO_26].append(apt_set2)
        progress_data[SET_3_APT_RANGE_27_TO_40].append(apt_set3)
        days_passed.append(date_range[day])
    else:
        print("Progress for this day has already been updated.")


# Function to plot and save the graph
def plot_progress(day):
    plt.figure(figsize=(ASPECT_RATIO_10_INCH_WIDE, ASPECT_RATIO_6_INCH_TALL))
    plt.plot(date_range, target, label=TARGET, linestyle=DASHED_LINE_STYLE)

    plt.axhline(y=13, color="gray", linestyle=DASHED_LINE_STYLE, label="Completion")
 
    for person, progress in progress_data.items():
        plt.plot(days_passed, progress, label=person)

    # Add annotations for "Michael done" and "Amber done"
    #plt.text(days_passed[-1], 13, "Michael DONE!!", fontsize=9, color="green")
    #plt.text(days_passed[-1], 12, "Amber DONE!!", fontsize=9, color="orange")

    # Formatting the date axis
    plt.gca().xaxis.set_major_formatter(
        plt.matplotlib.dates.DateFormatter('%b %d'))
    plt.gca().xaxis.set_major_locator(
        plt.matplotlib.dates.DayLocator(interval=X_AXIS_INTERVAL_1))

    plt.xlabel(X_AXIS_LABEL)
    plt.ylabel(Y_AXIS_LABEL)
    plt.title(GRAPH_TITLE)
    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the graph
    plt.savefig(f"{PROGRESS_TRACKER_FILE_BASE}{day+1}{FILE_EXTENSION_PNG}")
    plt.close()


# Oct 14th
update_progress(0, 0, 0, day=0)  # Day 1 update
plot_progress(day=0)

# Oct 15th
#update_progress(0, 0, 0, day=1)  # Day 2 update
#plot_progress(day=1)

# Oct 16th
#update_progress(0, 0, 0, day=2)  # Day 3 update
#plot_progress(day=2)

# Oct 17th
#update_progress(0, 0, 0, day=3)  # Day 4 update
#plot_progress(day=3)

# Oct 18th
#update_progress(0, 0, 0, day=4)  # Day 5 update
#plot_progress(day=4)

# Oct 19th
#update_progress(0, 0, 0, day=5)  # Day 6 update
#plot_progress(day=5)

# Oct 20th
#update_progress(0, 0, 0, day=6)  # Day 7 update
#plot_progress(day=6)

# Oct 21st
#update_progress(0, 0, 1, day=7)  # Day 8 update
#plot_progress(day=7)

# Oct 22nd
#update_progress(0, 13, 4, day=8)  # Day 9 update
#plot_progress(day=8)

# Oct 23rd
#update_progress(13, 13, 6, day=9)  # Day 10 update
#plot_progress(day=9)

# Oct 24th
# update_progress(14, 14, 14, day=10)  # Day 11 update
# plot_progress(day=10)

# Oct 25th
# update_progress(14, 14, 14, day=11)  # Day 12 update
# plot_progress(day=11)

# Oct 26th
# update_progress(14, 14, 14, day=12)  # Day 13 update
# plot_progress(day=12)

# Oct 27th
# update_progress(14, 14, 14, day=13)  # Day 14 update
# plot_progress(day=13)

# Oct 28th
# update_progress(14, 14, 14, day=14)  # Day 15 update
# plot_progress(day=14)

