#!/usr/bin/env python3
import os
import subprocess

subprocess = subprocess.Popen("gh pr list", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
list = subprocess_return.splitlines()

pairs = {}
for i, pr in enumerate(list):
    name = pr.decode()
    num = name.split("\t")
    pairs[i+1] = num[0]
    print(f"number[{i+1}] -> {num[1]}")

print("select checkout PR number")
inp = input()
os.system(f"gh pr checkout {pairs[int(inp)]}")
