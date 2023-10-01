import subprocess


def get_wifi_profiles():
    try:
        command = "netsh wlan show profiles"
        result = subprocess.check_output(command, shell=True, text=True)
        return [line.split(":")[1].strip() for line in result.splitlines() if "All User Profile" in line]
    except subprocess.CalledProcessError as exc:
        print(f"Command '{command}' failed with error code {exc.returncode}: {exc.stderr}")
        return []


def get_wifi_password(profile):
    try:
        command = f"netsh wlan show profile \"{profile}\" key=clear"
        result = subprocess.check_output(command, shell=True, text=True)
        username, password = None, None
        for line in result.splitlines():
            if "SSID" in line:
                username = line.split(":")[1].strip()
            elif "Key Content" in line:
                password = line.split(":")[1].strip()
        return username, password
    except subprocess.CalledProcessError as exc:
        print(f"Command '{command}' failed with error code {exc.returncode}: {exc.stderr}")
        return None, None


def main():
    wifi_profiles = get_wifi_profiles()
    if not wifi_profiles:
        print("No wireless profiles found.")
        return

    for profile in wifi_profiles:
        username, password = get_wifi_password(profile)
        if username is not None and password is not None:
            print(f"UserName - {username} | PassWord - {password}")

    input("Press Enter to exit\n")


if __name__ == "__main__":
    main()
