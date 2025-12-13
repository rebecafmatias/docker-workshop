from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for i in current_dir.iterdir():
    if i.name == current_file:
        continue
    
    print(f" - {i.name}")