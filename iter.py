import subprocess
num_runs = int(input("enter the num of times you want to run this file.....\n"))
for _ in range(num_runs):
    try:
        result = subprocess.run(["python", "python.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print("Run", _ + 1, "Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Run", _ + 1, "Error:", e)