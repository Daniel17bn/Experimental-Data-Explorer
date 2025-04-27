import matplotlib.pyplot as plt
import neurokit2 as nk# Download data

data = nk.data("bio_eventrelated_100hz")

condition_list = ["Negative", "Neutral", "Neutral", "Negative"]

# Find events
events = nk.events_find(data["Photosensor"], threshold_keep='below', event_conditions=condition_list)

# Plot the location of event with the signals
plot = nk.events_plot(events, data)

plt.show()
