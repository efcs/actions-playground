import argparse
import os
from pathlib import Path
import re
import subprocess
import argparse

# Path: classify-paths.py
ROOT = Path(__file__).parent

def get_diff():
  output = subprocess.check_output(['git', 'diff', '--name-only', 'origin/main', 'origin/{GITHUB_HEAD_REF}'.format(os.environ['GITHUB_HEAD_REF'])])
  output = output.decode('utf-8')
  return [ln.strip() for ln in output.splitlines() if ln.strip()]


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--paths', nargs='+', required=True)
  args = parser.parse_args()


if __name__ == '__main__':
  main()
