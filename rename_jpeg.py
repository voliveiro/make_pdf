"""
  Run this script if you need to rename .jpeg files into .jpg files
"""

import os

def rename_jpeg_to_jpg(folder_path):
  
  for filename in os.listdir(folder_path):
    if filename.endswith(".jpeg"):
      new_filename = filename[:-5] + ".jpg"  # Remove last 5 characters (.jpeg) and add .jpg
      os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
      print(f"Renamed: {filename} -> {new_filename}")

# Replace 'path/to/your/folder' with the actual path if needed
folder_path = os.getcwd()  # Get the current working directory by default
rename_jpeg_to_jpg(folder_path)

print("All .jpeg files renamed to .jpg successfully!")