from time import sleep

import orjson

from namespace.lib import Foo


def main(max_iters: float | None) -> None:
    iter = 0
    if max_iters is None:
        max_iters = float("inf")
    while iter < max_iters:
        iter +=1
        print(orjson.dumps(Foo(name="app").dict()).decode())
        sleep(1)


if __name__ == "__main__":
    main()
