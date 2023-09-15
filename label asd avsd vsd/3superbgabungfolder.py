import os
import shutil

def merge_folders_by_prefix(source_dir, dest_dir):
    # Membuat direktori tujuan jika belum ada
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # gabung folder dengan tiga karakter pertama yang sama
    for root, dirs, files in os.walk(source_dir):
        for folder in dirs:
            source_folder = os.path.join(root, folder)
            prefix = folder[:3]
            dest_folder = os.path.join(dest_dir, prefix)

            # Membuat direktori tujuan jika belum ada
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # Memindahkan file dari folder sumber ke folder tujuan
            for file in os.listdir(source_folder):
                source_file = os.path.join(source_folder, file)
                dest_file = os.path.join(dest_folder, file)
                shutil.move(source_file, dest_file)

if __name__ == "__main__":
    source_directory = "gabungan"  
    dest_directory = "gabungtot"   # gabungan super

    merge_folders_by_prefix(source_directory, dest_directory)
    print("Folder telah digabungkan!")
