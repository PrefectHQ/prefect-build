"""This is an example flows module"""
from prefect import flow

from prefect_build.blocks import BuildBlock
from prefect_build.tasks import (
    goodbye_prefect_build,
    hello_prefect_build,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    BuildBlock.seed_value_for_example()
    block = BuildBlock.load("sample-block")

    print(hello_prefect_build())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_build())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
