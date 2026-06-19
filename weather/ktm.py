
import os


def run_cmd(value:str) -> None:
    res = os.system(command=value)
    return res

while True:

    print(run_cmd(input("👉")))