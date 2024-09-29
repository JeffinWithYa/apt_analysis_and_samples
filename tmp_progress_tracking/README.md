# APT Report Progress Tracker

This Python script(s) is designed to track the progress of completing APT reports/tasks for MCTI 6530 submissions. The script generates a progress graph, showing the number of reports completed each day by each person on the team, alongside a target line representing the expected pace of completion.

## Features
- **Tracks Progress for Three People**: Each person is assigned a set of reports (apt_1_to_13, apt_14_to_26, apt_27_to_40) and their progress is recorded daily.
- **Dynamic Updates**: The script allows you to update progress for each day and generate a new graph.
- **Graph Generation**: A graph is saved as a `.png` file that shows the target progress and individual progress over time.

## Setup Instructions

### 1. Create a Python Virtual Environment

It is recommended to run this script inside a virtual environment to manage dependencies. To create a virtual environment, follow these steps:

1. **Navigate to the Project Directory**:
    ```bash
    cd /path/to/project
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **MacOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. **Install the Required Dependencies**:
    After activating the virtual environment, install the required dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### 2. How to Run the Script

1. **Ensure Dependencies Are Installed**: 
   If you haven't already installed the required dependencies, run the following command inside your virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

2. **Update Progress**: 
   Use the `update_progress()` function to input the number of reports completed by each person for a specific day.
   ```python
   update_progress(apt_set1=4, apt_set2=3, apt_set3=1, day=1)
   ```
   This will record the progress for Day 2 (since `day=1` corresponds to September 30).

3. **Plot the Graph**: 
   After updating the progress, call the `plot_progress()` function to generate the graph for that day.
   ```python
   plot_progress(day=1)
   ```
   This will save the graph as a PNG file with the name `progress_tracker_with_dates_day2.png`.

4. **Automating Updates**: You can uncomment or add new lines in the script to automate updates for each day.

### 3. How to Update the Script

- **Adding New Progress**: For each new day, use the `update_progress()` function with the number of reports completed for each person and the day index (starting from `0` for September 29).
- **Plotting the Updated Graph**: After updating progress, use the `plot_progress()` function to save the graph for the current day.

### Example Workflow

1. **Update Progress for Day 1 (Sept 29):**
   ```python
   update_progress(apt_set1=0, apt_set2=0, apt_set3=0, day=0)
   plot_progress(day=0)
   ```
   This generates `progress_tracker_with_dates_day1.png`.

2. **Update Progress for Day 2 (Sept 30):**
   ```python
   update_progress(apt_set1=4, apt_set2=3, apt_set3=1, day=1)
   plot_progress(day=1)
   ```
   This generates `progress_tracker_with_dates_day2.png`.

## Recent Graph - Sept. 29th, 2024

![Progress Tracker](https://raw.githubusercontent.com/JeffinWithYa/apt_analysis_and_samples/main/tmp_progress_tracking/progress_tracker_with_dates_day1.png)

---

### `requirements.txt` Example

If you need to generate a new `requirements.txt` file for your project, you can create one by running the following command:
```bash
pip freeze > requirements.txt
```
This will save all the dependencies in the `requirements.txt` file for future use.

