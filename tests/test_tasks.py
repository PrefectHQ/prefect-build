from prefect import flow

from prefect_build.tasks import (
    goodbye_prefect_build,
    hello_prefect_build,
)


def test_hello_prefect_build():
    @flow
    def test_flow():
        return hello_prefect_build()

    result = test_flow()
    assert result == "Hello, prefect-build!"


def goodbye_hello_prefect_build():
    @flow
    def test_flow():
        return goodbye_prefect_build()

    result = test_flow()
    assert result == "Goodbye, prefect-build!"
