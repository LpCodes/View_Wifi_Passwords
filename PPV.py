import subprocess

root = subprocess.check_output(
    "netsh wlan show profiles", shell=True, stderr=subprocess.STDOUT
).decode()
# print(resp)

uname = []
for x in root.splitlines():
    if "User" in x:

        uname.append(x.split(":", 1)[-1])

print(uname)

for y in uname:
    yy = "netsh wlan show profile %s key=Clear" % y
    try:
        op = subprocess.check_output(yy, shell=True, stderr=subprocess.STDOUT).decode()
        print(op)
    except subprocess.CalledProcessError:
        print("oops", y)

input("Press Any Key to Exit\n")
