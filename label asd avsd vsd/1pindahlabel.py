import os
import shutil

# direktori folder utama
folder_utama = r"inidirektori"

# daftar folder di folder utama
folders = [f.path for f in os.scandir(folder_utama) if f.is_dir()]

# buat folder "image" di setiap subfolder jika belum ada
for folder in folders:
    subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
    for subfolder in subfolders:
        image_folder = os.path.join(subfolder, "image")

        # pindah seluruh isi folder "label" ke folder "image"
        label_folder = os.path.join(subfolder, "label")
        if os.path.exists(label_folder):
            for root, _, files in os.walk(label_folder):
                for file in files:
                    label_file_path = os.path.join(root, file)
                    new_path = os.path.join(image_folder, file)
                    shutil.move(label_file_path, new_path)
                    print(f"File '{label_file_path}' berhasil dipindahkan ke '{new_path}'")
            shutil.rmtree(label_folder)
            print(f"Folder 'label' '{label_folder}' berhasil dihapus")
        else:
            print(f"Folder 'label' tidak ditemukan di '{subfolder}'")
        # pindah isi folder "image" ke utama
        if os.path.exists(image_folder):
            image_files = [f.path for f in os.scandir(image_folder) if f.is_file()]
            for file in image_files:
                new_path = os.path.join(subfolder, os.path.basename(file))
                shutil.move(file, new_path)
                print(f"File '{file}' berhasil dipindahkan ke '{new_path}'")
              # apus image
            shutil.rmtree(image_folder)
            print(f"Folder 'label' '{image_folder}' berhasil dihapus")
        else:
            print(f"Folder 'image' tidak ditemukan di '{subfolder}'")
