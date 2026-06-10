#!/usr/bin/env python3
"""Launch ClaudeOS from the repository root: python run_os.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from claude_os.kernel import Kernel
from claude_os.shell import Shell


def main() -> None:
    kernel = Kernel()
    kernel.boot()
    shell = Shell(kernel)
    shell.run()


if __name__ == "__main__":
    main()
