import os

def delete_jpg_without_json(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.jpg'):
                jpg_path = os.path.join(foldername, filename)
                json_path = os.path.join(foldername, filename.replace('.jpg', '.json'))
                if not os.path.exists(json_path):
                    print(f"hapus {jpg_path} karna ga ada versi json {json_path}")
                    os.remove(jpg_path)

if __name__ == "__main__":
    root_folder = r'perc' 
    delete_jpg_without_json(root_folder)
