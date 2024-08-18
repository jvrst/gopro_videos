import os
import re

# Define the path containing your MP4 files
path = '/media/T7/GoPro/import_21072024_2323'

# Initialize lists to hold filenames
chaptered_videos = {}
all_chaptered = set()
single_videos = []
chaptered_nrs = set()

# Process the files in the path
files = os.listdir(path)
files = [file for file in files if file.endswith('.MP4')]
print(files)

for filename in files:
    if filename.endswith('.mp4') or filename.endswith('.MP4'):
        parts = re.findall(r'(.*)(\d{2})(\d{4})\..*', filename)[0]
        prefix = parts[0]
        chapter_nr = parts[1]
        file_nr = parts[2]

        print(filename, parts, chapter_nr, file_nr)
        if int(chapter_nr) > 1:
            key = prefix + file_nr
            chaptered_nrs.add(key)
            if not chaptered_videos.get(key, None):
                chaptered_videos[key] = []
                first_file = re.sub(r'(\d{2})', '01', filename, 1)
                chaptered_videos[key].append(first_file)
                all_chaptered.add(first_file)
            chaptered_videos[key].append(filename)
            all_chaptered.add(filename)

print(chaptered_videos)
for file in files:
    if file not in all_chaptered:
        single_videos.append(file)

for key, files in chaptered_videos.items():
    with open(f'{path}/chaptered_videos_{key}.txt', 'w') as f:
       for file in sorted(files):  # Ensure the files are sorted
            f.write(f"file '{file}'\n")

print(single_videos)
for file in single_videos:
    os.rename(f"{path}/{file}", f"{path}/single_{file}")

print("Text files for ffmpeg concatenation have been created successfully.")

