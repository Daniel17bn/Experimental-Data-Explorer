import matplotlib.pyplot as plt
import neurokit2 as nk
import pandas as pd

# Load the eye-tracking data file
file_path = r"C:\Users\danie\OneDrive - University of Luxembourg\BSP\test\vrbias-example-user\vrbias-example-user\01\2024-08-29T18-05-00-41\eyetracking-raw.csv"
data = pd.read_csv(file_path)

# Inspect the data (optional)
print(data.head())

# Select the column to analyze (e.g., left eye horizontal position)
gaze_data = data["L_eyeposX"]

# Define conditions (optional, adjust as needed)


# Find events in the gaze data (adjust threshold as needed)
events = nk.events_find(gaze_data, threshold_keep='below')

# Plot the events with the gaze data
plot = nk.events_plot(events, gaze_data)

# Display the plot
plt.show()