def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs based on their deadlines
    n = len(jobs)
    result = [False] * n  # Result list to store the scheduled jobs
    slot = [-1] * n  # Slot list to store the time slots

    for i in range(n):
        # Find a suitable slot for the job
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if slot[j] == -1:
                slot[j] = i
                result[i] = True
                break

    # Gather the scheduled jobs
    scheduled_jobs = []
    for i in range(n):
        if result[i]:
            scheduled_jobs.append(jobs[slot[i]])

    return scheduled_jobs

# Example usage:
jobs = [("Job1", 2), ("Job2", 1), ("Job3", 4), ("Job4", 3)]
scheduled_jobs = job_scheduling(jobs)
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(job[0])
