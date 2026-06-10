#!/usr/bin/env python3
"""ClaudeOS entry point."""

from .kernel import Kernel
from .shell import Shell


def main() -> None:
    kernel = Kernel()
    kernel.boot()
    shell = Shell(kernel)
    shell.run()


if __name__ == "__main__":
    main()
