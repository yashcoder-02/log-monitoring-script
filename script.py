# Log Monitoring Script

with open("logs.txt", "r") as file:
    for line in file:
        if "failed" in line.lower():
            print("Alert: Suspicious activity ->", line.strip())
