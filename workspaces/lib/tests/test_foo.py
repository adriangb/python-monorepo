import json
from namespace.lib import Foo


def test_foo() -> None:
    got = json.loads(Foo(name="adrian").json())
    expected = {"name": "adrian"}
    assert got == expected
