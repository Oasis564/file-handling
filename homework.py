# file_operations.py

# --- Writing to files using write() ---
with open("topic1.txt", "w") as f1:
    f1.write("Technology has revolutionized the way we live, work, and communicate.\n")
    f1.write("From smartphones to artificial intelligence, innovations continue to shape our future.\n")
    f1.write("The pace of technological change shows no signs of slowing down.\n")

# --- Writing multiple lines using writelines() ---
lines_topic2 = [
    "Climate change remains one of the biggest challenges facing humanity.\n",
    "Global efforts to reduce carbon emissions are essential to prevent catastrophic consequences.\n",
    "Sustainable energy and responsible consumption can make a real difference.\n"
]
with open("topic2.txt", "w") as f2:
    f2.writelines(lines_topic2)

# --- Writing another file ---
lines_topic3 = [
    "Education is the foundation of personal and societal growth.\n",
    "With the rise of online learning platforms, education has become more accessible than ever.\n",
    "Continuous learning is now a lifelong necessity in a rapidly changing world.\n"
]
with open("topic3.txt", "w") as f3:
    f3.writelines(lines_topic3)

# --- Reading full file content using read() ---
with open("topic1.txt", "r") as f:
    print("Reading with read():\n")
    print(f.read())

# --- Reading line by line using readline() ---
with open("topic2.txt", "r") as f:
    print("\nReading with readline():\n")
    print(f.readline())  # first line
    print(f.readline())  # second line

# --- Reading all lines into a list using readlines() ---
with open("topic3.txt", "r") as f:
    print("\nReading with readlines():\n")
    lines = f.readlines()
    print(lines)  # prints list of all lines
