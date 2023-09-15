import os
import shutil

# Fungsi untuk mengelompokkan file berdasarkan 4 huruf pertama
def organize_files(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            file_name = os.path.splitext(file)[0]
            folder_name = file_name[:4]  # Mengambil 4 huruf pertama dari nama file
            file_extension = os.path.splitext(file)[1]
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, folder_name, file_name + file_extension)

            # Membuat folder jika belum ada
            os.makedirs(os.path.join(dest_folder, folder_name), exist_ok=True)

            # Memindahkan file ke folder yang sesuai
            shutil.move(source_path, dest_path)

if __name__ == "__main__":
    src_folder = "percob"
    dest_folder = "percob_output"

    organize_files(src_folder, dest_folder)
