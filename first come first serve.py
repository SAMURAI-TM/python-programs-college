def fcfs_scheduling(n, burst_times):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]
    
    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_times[i]
    
    # Calculate average times
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    # Display results
    print("\nProcess	Burst Time	Waiting Time	Turnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# User input
n = int(input("Enter the number of processes: "))
burst_times = []
for i in range(n):
    bt = int(input(f"Enter burst time for process P{i+1}: "))
    burst_times.append(bt)

fcfs_scheduling(n, burst_times)
