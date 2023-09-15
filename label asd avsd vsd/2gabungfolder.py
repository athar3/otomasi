import os
import shutil

# Direktori folder utama
folder_utama = r"direktori yg nk di gawein"

# Direktori folder gabungan henshin
folder_gabungan = r"direktori hasil gawean"

# Membuat folder gabungan jika belum ada
if not os.path.exists(folder_gabungan):
    os.makedirs(folder_gabungan)
    print(f"Folder 'gabungan' berhasil dibuat di '{folder_gabungan}'")

# Daftar folder di folder utama
folders = [f.path for f in os.scandir(folder_utama) if f.is_dir()]

# Memindahkan subsubfolder dari folder utama ke folder gabung dengan menggunakan nama subfolder
for folder in folders:
    subsubfolders = [f.name for f in os.scandir(folder) if f.is_dir()]
    subfolder_name = os.path.basename(folder)  # Nama subfolder
    for subsubfolder in subsubfolders:
        source_path = os.path.join(folder, subsubfolder)
        destination_path = os.path.join(folder_gabungan, f"{subsubfolder}_{subfolder_name}")
        
        # Memindahkan isi subsubfolder ke dalam folder "gabungan"
        shutil.move(source_path, destination_path)
        print(f"Subsubfolder '{subsubfolder}' berhasil dipindahkan ke '{destination_path}'")

print("Proses selesai. Subsubfolder telah dipindahkan dan digabungkan ke dalam folder 'gabungan'.")
