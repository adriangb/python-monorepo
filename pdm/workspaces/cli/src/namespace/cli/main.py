from rich import print

from namespace.lib import Foo


def main() -> None:
    print(Foo(name="cli"))


if __name__ == "__main__":
    main()
