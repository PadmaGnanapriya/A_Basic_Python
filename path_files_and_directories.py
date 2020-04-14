from pathlib import Path

path = Path("Day_02")
for file in path.glob("*.*"):
    print (file)