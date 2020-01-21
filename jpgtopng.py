import sys
import os
from PIL import image



if len(sys.argv) != 3:
    print("Usage: python jpgtopng.py source_dir dest_dir")
    exit()

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
    print(f"source_dir {source_dir} must exist and be a directory")
    exit()

if not os.path.exists(dest_dir):
    print(f"dest_dir {dest_dir}  does not exist. Creating.")

print (f"Retrieving from {sys.argv[1]}")
for file in filter(lambda f: f.endswith('.jpg'), os.listdir(source_dir)) :
    print(f"Converting {file} to png")

