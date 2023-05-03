import pygame
import os
from colorama import Fore, Style

# Inisialisasi pygame mixer
pygame.mixer.init()

# Inisialisasi pygame
pygame.init()

# Fungsi untuk memutar musik
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Fungsi untuk menghentikan pemutaran musik
def stop_music():
    pygame.mixer.music.stop()

# Fungsi untuk mengatur volume musik (0.0 - 1.0)
def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Fungsi untuk mendapatkan status pemutaran musik
def is_playing():
    return pygame.mixer.music.get_busy()

# Main program
if __name__ == "__main__":
    # Path folder musik
    music_folder = "./music"

    # Daftar musik dalam folder
    music_files = os.listdir(music_folder)

    # Looping untuk memilih musik
    while True:
        # Menampilkan daftar musik yang tersedia
        print(Fore.YELLOW + "Daftar musik yang tersedia:" + Style.RESET_ALL)
        for i, file in enumerate(music_files):
            print(Fore.GREEN + f"{i + 1}. {file}" + Style.RESET_ALL)

        # Memilih nomor musik
        choice = input("Masukkan nomor musik yang ingin diputar (0 untuk keluar): ")
        choice = int(choice) - 1

        # Keluar jika pilihan 0 atau diluar rentang daftar musik
        if choice == -1 or choice >= len(music_files):
            break

        # Mengambil path file musik yang dipilih
        music_file = os.path.join(music_folder, music_files[choice])

        # Memutar musik yang dipilih
        play_music(music_file)

        # Looping untuk kontrol pemutaran musik
        while True:
            print(Fore.YELLOW + "Pilihan kontrol:" + Style.RESET_ALL)
            print(Fore.GREEN + "1. Stop")
            print("2. Ubah Volume")
            print("0. Kembali ke daftar musik" + Style.RESET_ALL)

            # Memilih kontrol
            control_choice = input(Fore.BLUE + "Masukkan nomor kontrol: " + Style.RESET_ALL)

            # Stop pemutaran musik
            if control_choice == "1":
                stop_music()
                break

            # Ubah volume
            elif control_choice == "2":
                volume = float(input(Fore.BLUE + "Masukkan volume (0.0 - 1.0): " + Style.RESET_ALL))
                set_volume(volume)

            # Kembali ke daftar musik
            elif control_choice == "0":
                stop_music()
                break

        print()

    print("Terima kasih telah menggunakan pemutar musik.")
