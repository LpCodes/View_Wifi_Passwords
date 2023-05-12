import subprocess


def main():
    # Get the list of wireless profiles
    command = "netsh wlan show profiles"
    try:
        result = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as exc:
        print(f"Command '{command}' failed with error code {exc.returncode}: {exc.stderr}")
        return
    profiles = [line.split(":")[1].strip() for line in result.splitlines() if "All User Profile" in line]

    # Get the Wi-Fi passwords for each profile
    for profile in profiles:
        command = f"netsh wlan show profile \"{profile}\" key=clear"
        try:
            result = subprocess.check_output(command, shell=True, text=True)
        except subprocess.CalledProcessError as exc:
            print(f"Command '{command}' failed with error code {exc.returncode}: {exc.stderr}")
            continue
        for line in result.splitlines():
            if "SSID" in line:
                username = line.split(":")[1].strip()
            elif "Key Content" in line:
                password = line.split(":")[1].strip()
        print(f"UserName - {username} | PassWord -  {password}")

    input("Press Any Key to Exit\n")


if __name__ == "__main__":
    main()
