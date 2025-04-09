import time
from multiprocessing import Process


class Worker(Process):
    def run(self) -> None:
        print("> Worker started...")
        time.sleep(2)
        print("> Worker exited...")


def main() -> None:
    print("> Request to Worker")
    worker = Worker()

    print("> Start Worker")
    worker.start()
    print(f"\tis Worker alive?: {worker.is_alive()}")

    print("> Make Worker rest")
    time.sleep(2)
    print(f"\tis Worker alive?: {worker.is_alive()}")

    print("> Wait for Worker until the Worker finish the job and join")
    worker.join() # 실질적으로 작업 수행
    print(f"\tis Worker alive?: {worker.is_alive()}")

    print("> Finish Worker")


if __name__ == '__main__':
    main()