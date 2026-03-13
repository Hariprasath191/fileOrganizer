import os 
import shutil
data = {

    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',
    '.webp': 'Images',
    '.ico': 'Images',

    # Text / Documents
    '.txt': 'Text',
    '.rtf': 'Text',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.xls': 'Documents',
    '.xlsx': 'Documents',
    '.ppt': 'Documents',
    '.pptx': 'Documents',

    # Documentation / Markup
    '.md': 'Documentation',
    '.rst': 'Documentation',
    '.tex': 'Documentation',
    '.latex': 'Documentation',

    # Audio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.aac': 'Audio',
    '.flac': 'Audio',
    '.ogg': 'Audio',
    '.m4a': 'Audio',
    '.wma': 'Audio',

    # Videos
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.wmv': 'Videos',
    '.flv': 'Videos',
    '.webm': 'Videos',

    # Archives / Compressed
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.bz2': 'Archives',
    '.xz': 'Archives',
    '.tgz': 'Archives',

    # Executables / Installers
    '.exe': 'Executables',
    '.msi': 'Executables',
    '.bat': 'Executables',
    '.sh': 'Executables',
    '.apk': 'Executables',
    '.deb': 'Executables',
    '.rpm': 'Executables',

    # Programming Code
    '.py': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
    '.cs': 'Code',
    '.go': 'Code',
    '.rs': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.js': 'Code',
    '.ts': 'Code',
    '.php': 'Code',
    '.rb': 'Code',
    '.swift': 'Code',
    '.kt': 'Code',

    # Data Files
    '.json': 'Data',
    '.csv': 'Data',
    '.xml': 'Data',
    '.yaml': 'Data',
    '.yml': 'Data',
    '.parquet': 'Data',
    '.db': 'Data',
    '.sqlite': 'Data',

    # Design Files
    '.psd': 'Design Files',
    '.ai': 'Design Files',
    '.indd': 'Design Files',
    '.fig': 'Design Files',
    '.sketch': 'Design Files',
    '.svg': 'Design Files',
    '.eps': 'Design Files',

    # Fonts
    '.ttf': 'Fonts',
    '.otf': 'Fonts',
    '.woff': 'Fonts',
    '.woff2': 'Fonts',
    '.eot': 'Fonts',

    # Logs / Temporary / Backup
    '.log': 'Logs',
    '.bak': 'Backups',
    '.old': 'Backups',
    '.tmp': 'Temporary',
    '.temp': 'Temporary',

    # Disk Images
    '.iso': 'Disk Images',
    '.dmg': 'Disk Images',
    '.img': 'Disk Images',
    '.vhd': 'Disk Images',
    '.vmdk': 'Disk Images',

    # System Files
    '.dll': 'System Files',
    '.sys': 'System Files',
    '.ini': 'System Files',
    '.cfg': 'System Files',
}

#path = input("Enter path: ")
path = r"E:\hariprasath\My work 2026\LEARN ROADMAP\PYTHON\Projects\sample"

files= os.listdir(path)

for file in files:
    if not os.path.isfile(os.path.join(path,file)):
        continue
    
    name,ext = os.path.splitext(file)
    ext = ext.lower()
    if ext in data:
        nfolder = data[ext] 
    else:
        nfolder = 'others'
    if not os.path.exists(os.path.join(path,nfolder)):
        os.mkdir(os.path.join(path,nfolder))
    shutil.move(os.path.join(path,file), os.path.join(path,nfolder,file))
        