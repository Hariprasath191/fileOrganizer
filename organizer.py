
import os 
import shutil
data = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico'],
    'Text': ['.txt', '.rtf'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Documentation': ['.md', '.rst', '.tex', '.latex'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tgz'],
    'Executables': ['.exe', '.msi', '.bat', '.sh', '.apk', '.deb', '.rpm'],
    'Code': ['.py', '.java', '.c', '.cpp', '.cs', '.go', '.rs', '.html', '.css', '.js', '.ts', '.php', '.rb', '.swift', '.kt'],
    'Data': ['.json', '.csv', '.xml', '.yaml', '.yml', '.parquet', '.db', '.sqlite'],
    'Design Files': ['.psd', '.ai', '.indd', '.fig', '.sketch', '.svg', '.eps'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
    'Logs': ['.log'],
    'Backups': ['.bak', '.old'],
    'Temporary': ['.tmp', '.temp'],
    'Disk Images': ['.iso', '.dmg', '.img', '.vhd', '.vmdk'],
    'System Files': ['.dll', '.sys', '.ini', '.cfg'],
}

extension_map = {}
for folder, extensions in data.items():
    for ext in extensions:
        extension_map[ext] = folder

#path = input("Enter path: ")
path = r"E:\hariprasath\My work 2026\LEARN ROADMAP\PYTHON\Projects\sample"

for file in os.listdir(path):

    source = os.path.join(path, file)

    # skip folders
    if not os.path.isfile(source):
        continue

    ext = os.path.splitext(file)[1].lower()
    
    # find folder
    folder = extension_map.get(ext, "Others")
    destination_folder = os.path.join(path, folder)

    # create folder if needed
    os.makedirs(destination_folder, exist_ok=True)
    destination = os.path.join(destination_folder, file)

    shutil.move(source, destination)

    print(f"Moved: {file} → {folder}")