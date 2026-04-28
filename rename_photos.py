import os

path = r'public/assets/core/'
if not os.path.exists(path):
    print(f"Path {path} does not exist")
else:
    for filename in os.listdir(path):
        # Only process files that aren't already clean
        if filename.endswith('.jpg') and '-' in filename:
            continue
            
        new_name = filename.strip()
        # Remove extra extensions and patterns
        new_name = new_name.replace('.jpg.jpeg', '.jpg')
        new_name = new_name.replace('.jpeg', '.jpg')
        new_name = new_name.replace(' (2)', '')
        new_name = new_name.replace(' ', '-').lower()
        
        # Avoid duplicate extensions
        if new_name.count('.jpg') > 1:
            new_name = new_name.replace('.jpg.jpg', '.jpg')
            
        old_path = os.path.join(path, filename)
        new_path = os.path.join(path, new_name)
        
        if old_path != new_path:
            print(f"Renaming: {filename} -> {new_name}")
            if os.path.exists(new_path):
                os.remove(new_path)
            os.rename(old_path, new_path)
