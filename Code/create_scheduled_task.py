import os

task_name = input(f"Task name: ")
executable_path = input(f"Path to the .exe file:\n")
trigger = "hourly"
start_time = input(f"Start time: ")

command_line = f'schtasks /create /tn "{task_name}" /tr "{executable_path}" /sc {trigger} /st {start_time}'
os.system(command_line)