import sys
import colorama
from colorama import Fore, Style
from pathlib import Path

colorama.init(autoreset=True)

def print_dir_structure(path: Path, indent: str = ""):
    for item in path.iterdir():
        if item.name.startswith('.'):
            continue
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            print_dir_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
    sys.exit(2)

path = Path(sys.argv[1]).resolve()

if not path.is_dir():
    print("Вказаний шлях не існує або не є директорією.")
    sys.exit(2)

print(f"{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
print_dir_structure(path, indent="    ")