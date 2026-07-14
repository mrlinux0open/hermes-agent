import subprocess
import sys

subprocess.run([
    sys.executable,
    "-m",
    "pip",
    "install",
    "git+https://github.com/NousResearch/hermes-agent.git"
], check=True)

subprocess.run(["hermes setup"])
