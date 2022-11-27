import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("test_binary")
args = parser.parse_args()

message = "Hello Nowide Nowide"
test_binary = args.test_binary

completed_process = subprocess.run(
    [test_binary, "passthrough"],
    input=message,
    capture_output=True,
    encoding='utf-8'
)

result = completed_process.returncode
stdout_lines = set(completed_process.stdout.split("\n"))

if completed_process.returncode != 0:
    print(f"Command {test_binary} failed ({result}) with {stdout}")
    exit(1)

if message not in stdout_lines:
    print(f"Command {test_binary} did not output {message!r} but {completed_process.stdout!r}")
    exit(1)

print("Test OK")
