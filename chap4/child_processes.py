"""
Forking Child Process
"""

import os
from multiprocessing import Process


def run_child() -> None:
    print("===== Children Process =====")

    print(f"> Child PID : {os.getpid()}")
    print(f"> Parent PID : {os.getppid()}") # 'p'arent 'p'rocess 'id'

    print("============================")


def start_parent(children_num: int) -> None:
    print("===== Parent Process =====")

    print(f"> PID : {os.getpid()}")  # 'p'arent 'p'rocess 'id'
    # Spawning/Forking New Process
    for i in range(children_num):
        print(f"> Start Child Process ({i})")
        Process(target=run_child).start()

    print("==========================")
    pass


if __name__ == '__main__':
    children_num = 3
    start_parent(children_num)


"""
===== Parent Process =====
> PID : 56313
> Start Child Process (0)
> Start Child Process (1)
> Start Child Process (2)
==========================
===== Children Process =====
> Child PID : 56315
> Parent PID : 56313
============================
===== Children Process =====
> Child PID : 56316
> Parent PID : 56313
============================
===== Children Process =====
> Child PID : 56317
> Parent PID : 56313
============================
"""