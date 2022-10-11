from time import sleep

import orjson

from namespace.lib import Foo


def main() -> None:
    while True:
        print(orjson.dump(Foo(name="app").dict()).decode())
        sleep(1)


if __name__ == "__main__":
    main()
