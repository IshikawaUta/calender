from colorama import Fore # Mengimpor modul warna pada teks
import calendar # Mengimpor modul calendar untuk mengelola dan menampilkan kalender
from datetime import datetime # Mengimpor datetime untuk mendapatkan tanggal dan waktu saat ini

print(Fore.CYAN + " ██████╗ █████╗ ██╗     ███████╗███╗   ██╗██████╗ ███████╗██████╗")
print(Fore.CYAN + "██╔════╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗")
print(Fore.CYAN + "██║     ███████║██║     █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝")
print(Fore.CYAN + "██║     ██╔══██║██║     ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗")
print(Fore.CYAN + "╚██████╗██║  ██║███████╗███████╗██║ ╚████║██████╔╝███████╗██║  ██║")
print(Fore.CYAN + " ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
print(Fore.LIGHTMAGENTA_EX + "Program untuk menunjukan tanggal dari input tahun dan bulan ini\n" + Fore.RESET)

# Mendapatkan tanggal hari ini
today = datetime.today() # Mengambil tanggal dan waktu saat ini

year = int(input("Input tahun : ")) # Meminta pengguna memasukkan tahun
month = int(input("Input Bulan (1-12): ")) # Meminta pengguna memasukkan bulan

# Mengganti hari ini dengan versi yang berwarna biru dalam kalender
print("\n", calendar.month(year, month).replace(str(today.day), f"{Fore.BLUE}{today.day}{Fore.RESET}"))

# Menampilkan informasi tanggal dan bulan saat ini
print(f"Sekarang adalah: {Fore.BLUE}{today.day}{Fore.RESET} {calendar.month_name [today.month]} {today.year}")
