import os
import subprocess
import time

def display_message(message, color=None):
    if color:
        print(f"\033[{color}m{message}\033[0m")
    else:
        print(message)

def install_kali_purple_tools_and_theme():
    # 프로그램 명 표시
    display_message("Kali Purple Tools and Theme Installer", "95")

    # 개발자 정보 표시
    display_message("Developer: 201580ag\nGitHub: https://github.com/201580ag", "93")

    # sudo 권한 확인
    if os.geteuid() != 0:
        display_message("Please run with sudo (administrative) privileges.", "91")
        return

    # Kali Purple 도구 및 테마 설치 여부 확인
    response = input("Would you like to install Kali Linux Purple tools and theme? (Y/N): ")
    if response.upper() != 'Y':
        display_message("Installation aborted.", "91")
        return

    # 패키지 목록 업데이트 및 불필요한 패키지 정리
    display_message("Updating package lists and cleaning up unnecessary packages...", "94")
    time.sleep(1)
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "full-upgrade", "-y"])
    subprocess.run(["apt", "autoremove"])

    display_message("Package list updated and cleaned.", "92")

    # Kali Purple 도구 설치
    display_message("Installing Kali Linux Purple tools...", "94")
    time.sleep(1)
    subprocess.run(["apt", "install", "kali-tools-identify", "-y"])
    subprocess.run(["apt", "install", "kali-tools-protect", "-y"])
    subprocess.run(["apt", "install", "kali-tools-detect", "-y"])
    subprocess.run(["apt", "install", "kali-tools-respond", "-y"])
    subprocess.run(["sudo", "apt", "install", "kali-tools-recover", "-y"])

    display_message("Kali Linux Purple tools installed.", "92")

    # Kali Purple 테마 설치 및 도구 메뉴에 추가
    display_message("Installing Kali Purple theme and adding tools to menu...", "94")
    time.sleep(1)
    subprocess.run(["apt", "install", "kali-themes-purple", "-y"])
    subprocess.run(["apt", "install", "--reinstall", "kali-menu"])

    display_message("Theme installed and tools added to menu.", "92")

    # 새로운 배경화면 설치
    display_message("Installing new wallpapers...", "94")
    subprocess.run(["apt", "update"])
    subprocess.run(["sudo", "apt", "-y", "install", "kali-wallpapers-legacy"])

    display_message("New wallpapers installed.", "92")

    display_message("All installations completed.", "92")

    # 터미널 초기화
    time.sleep(3)
    subprocess.run(["clear"])
    display_message("Installation completed.", "92")
    display_message('Change the appearance to Kali Purple Theme (Optional)\nSearch for "Appearance" in the Kali Linux menu and change it', "94")

if __name__ == "__main__":
    install_kali_purple_tools_and_theme()
