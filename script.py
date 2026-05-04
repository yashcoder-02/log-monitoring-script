logs = ["login success", "failed login", "error", "failed login"]

for log in logs:
    if "failed" in log:
        print("Alert: Suspicious activity ->", log)
