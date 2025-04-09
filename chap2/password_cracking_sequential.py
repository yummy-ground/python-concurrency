import time
import math
import hashlib
import typing as T


def get_combinations(*, pass_length: int, min_number: int = 0,
                     max_num: T.Optional[int] = None) -> T.List[str]:
    combinations = []
    if not max_num:
        max_num = int(math.pow(10, pass_length) - 1)

    for i in range(min_number, max_num + 1):
        str_num = str(i)
        zeros = "0" * (pass_length - len(str_num))
        combi = "".join((zeros, str_num))
        print(combi)
        combinations.append(combi)

    return combinations


def get_crypto_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(expected_crypto_hash: str, possible_password: str) -> bool:
    return expected_crypto_hash == get_crypto_hash(possible_password)


def crack_password(crypt_hash: str, password_length: int) -> None:
    print("=== Processing number combinations sequentially ===")
    start_time = time.perf_counter()

    combinations = get_combinations(pass_length=password_length)
    for combination in combinations:
        if check_password(crypt_hash, combination):
            print(f"** PASSWORD CRACKED : {combination} **")
            break

    process_time = time.perf_counter() - start_time
    print(f"=== Process Time: {process_time} ===")
    pass


if __name__ == '__main__':
    crypto_hash = \
        "e24df920078c3dd4e7e8d2442f00e5c9ab2a231bb3918d65cc50906e49ecaef4"
    length = 8

    crack_password(crypto_hash, length)
