import os, sys, signal, time

if len(sys.argv) != 3:
    print("USAGE: python sender.py <number> <pid>")

try:
    pid = int(sys.argv[2])
    num = int(sys.argv[1])
except:
    print("Ensure that both parameters are integers.\n")
    exit(-1)

try:
    os.kill(pid, 0)
except:
    print("Process", pid, "does not exist");
    exit(-1)

for i in range(7,-1,-1):
    if num >> i & 1:
        os.kill(pid, signal.SIGUSR2)
    else:
        os.kill(pid, signal.SIGUSR1)
    time.sleep(0.2)

