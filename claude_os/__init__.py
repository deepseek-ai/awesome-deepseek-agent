"""ClaudeOS — AI-native operating system."""

from .kernel import Kernel
from .shell import Shell
from .secrets import SecretVault
from .coworker import Coworker, CoworkerRegistry

__version__ = "0.3.0"
__all__ = ["Kernel", "Shell", "SecretVault", "Coworker", "CoworkerRegistry"]
