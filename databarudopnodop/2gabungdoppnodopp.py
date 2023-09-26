import os
import shutil

# Fungsi untuk mengelompokkan file berdasarkan 4 huruf pertama
def organize_files(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            folder_name = file[:4]  # Mengambil 4 huruf pertama dari nama file
            file_name, file_extension = os.path.splitext(file)
            folder_path = os.path.join(dest_folder, root, folder_name)

            # Membuat folder jika belum ada
            os.makedirs(folder_path, exist_ok=True)

            source_path = os.path.join(root, file)
            dest_path = os.path.join(folder_path, file_name + file_extension)

            # Memindahkan file ke folder yang sesuai
            shutil.move(source_path, dest_path)

if __name__ == "__main__":
    src_folder = r"D:\3 projekTA\TA koding\Dataset\jantung\data isys doppler\percobin"
    dest_folder = r"D:\3 projekTA\TA koding\Dataset\jantung\data isys doppler\percob_output"

    organize_files(src_folder, dest_folder)
