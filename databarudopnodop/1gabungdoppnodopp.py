import os
import shutil

# Definisikan path ke folder awal dan folder tujuan
folder_awal = r'perc'
folder_tujuan = r'percob'

# Buat folder tujuan jika belum ada
if not os.path.exists(folder_tujuan):
    os.makedirs(folder_tujuan)

# Iterasi melalui folder pasien di dalam folder awal
for pasien_folder in os.listdir(folder_awal):
    pasien_path = os.path.join(folder_awal, pasien_folder)

    # Pastikan yang diiterasi adalah folder, bukan file
    if os.path.isdir(pasien_path):
        # Iterasi melalui folder "doppler" dan "tanpa doppler"
        for jenis_pemeriksaan in os.listdir(pasien_path):
            jenis_pemeriksaan_path = os.path.join(pasien_path, jenis_pemeriksaan)

            # Pastikan yang diiterasi adalah folder, bukan file
            if os.path.isdir(jenis_pemeriksaan_path):
                # Ambil 4 karakter pertama dari nama folder jenis pemeriksaan (misalnya "5ch" atau "4ch")
                jenis_pemeriksaan = jenis_pemeriksaan[:15]

                # Iterasi melalui file di dalam folder jenis pemeriksaan
                for subfolder in os.listdir(jenis_pemeriksaan_path):
                    subfolder_path = os.path.join(jenis_pemeriksaan_path, subfolder)
                    
                    # Pastikan yang diiterasi adalah folder, bukan file
                    if os.path.isdir(subfolder_path):
                        # Iterasi melalui file di dalam subfolder
                        for file in os.listdir(subfolder_path):
                            file_path = os.path.join(subfolder_path, file)

                            # Tentukan nama folder tujuan berdasarkan jenis_pemeriksaan
                            folder_tujuan_jenis = os.path.join(folder_tujuan, jenis_pemeriksaan)

                            # Buat folder tujuan jika belum ada
                            if not os.path.exists(folder_tujuan_jenis):
                                os.makedirs(folder_tujuan_jenis)

                            # Tentukan path file tujuan
                            file_tujuan = os.path.join(folder_tujuan_jenis, file)

                            # Copy-paste file dari folder awal ke folder tujuan
                            shutil.copy2(file_path, file_tujuan)

# Hapus folder pasien kosong di dalam folder awal
for pasien_folder in os.listdir(folder_awal):
    pasien_path = os.path.join(folder_awal, pasien_folder)
    if os.path.isdir(pasien_path) and not os.listdir(pasien_path):
        os.rmdir(pasien_path)
