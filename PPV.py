import subprocess

def main():
    # Get the list of wireless profiles
    command = "netsh wlan show profiles"
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        print(f"Command '{command}' failed with error code {exc.returncode}: {exc.stderr}")
        return
    profiles = [line.split(":")[1].strip() for line in result.stdout.splitlines() if "All User Profile" in line]

    # Get the Wi-Fi passwords for each profile
    for profile in profiles:
        command = f"netsh wlan show profile \"{profile}\" key=clear"
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as exc:
            print(f"Command '{command}' failed with error code {exc.returncode}: {exc.stderr}")
            continue
        print(result.stdout)

    input("Press Any Key to Exit\n")

if __name__ == "__main__":
    main()
