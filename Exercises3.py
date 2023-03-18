#Given Inputs
start_time = 6 * 60 + 52 #hours to minutes + minutes
easy_pace = 8 * 60 + 15 #minutes to seconds + seconds
tempo_pace = 7 * 60 + 12  #minutes to seconds + seconds

# Calculate total time taken for the entire run in seconds
total_running_time = 1 * easy_pace + 3 * tempo_pace + 1 * easy_pace
#secundes to minutes
minutes = total_running_time // 60

# arrival time in minutes
arrival_time_min = (start_time + minutes)%60
arrival_time_hour = round((start_time + minutes -arrival_time_min)/60)

#print(arrival_time)
print(f"You will arrive back home at {arrival_time_hour}:{arrival_time_min} am for breakfast.")

