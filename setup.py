"""Module for package distribution setup."""

# INTEL CONFIDENTIAL
# Copyright 2023-2023 Intel Corporation.
#
# This software and the related documents are Intel copyrighted materials, and your use of them is governed
# by the express license under which they were provided to you ("License"). Unless the License provides otherwise,
# you may not use, modify, copy, publish, distribute, disclose or transmit this software or the related documents
# without Intel's prior written permission.
#
# This software and the related documents are provided as is, with no express or implied warranties,
# other than those that are expressly stated in the License.

import argparse
import sys
import os
from codecs import open
from setuptools import setup, find_packages

assert sys.version_info >= (3, 7, 0), "mfd requires Python 3.7+"

pwd = os.path.abspath(os.path.dirname(__file__))
version_file_path = os.path.join(pwd, "mfd_testing", "__version__.py")

info = {}
if os.path.exists(version_file_path):
    with codec_open(version_file_path, "r", "utf-8") as f:
        exec(f.read(), info)
else:
    info["__title__"] = "mfd-testing"
    info["__description__"] = "Modular Framework Design (MFD) module for Infrastructure Processing Unit"
    info["__version__"] = "0.0.0"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


def _get_suffix() -> str:
    """
    Define development suffix according to args.

    Removes defined additional argument from sys.argv for compatibility with setuptools
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", type=int, help="Define development build")
    args, left = parser.parse_known_args()
    sys.argv = sys.argv[:1] + left
    if args.dev:
        return f".dev{args.dev}"
    else:
        return ""


def yellow_print(message: str) -> None:
    """Print message with yellow color."""
    yellow_start_string = "\033[93m"
    yellow_end_string = "\033[00m"
    print(yellow_start_string)
    print("*" * 30)
    print(message)
    print("*" * 30)
    print(yellow_end_string)


required = []
dependency_links = []

EGG_MARK = "#egg="
for line in requirements:
    if line.startswith("-e git:") or line.startswith("-e git+") or line.startswith("git:") or line.startswith("git+"):
        if EGG_MARK in line:
            package_name = line[line.find(EGG_MARK) + len(EGG_MARK) :]  # noqa E203
            required.append(package_name)
            dependency_links.append(line)
        else:
            yellow_print(
                "Dependency to a git repository should have the format: "
                "\ngit+ssh://repo/xxxxx/xxxxxx#egg=package_name"
            )
    elif line.startswith("--extra-index-url"):
        yellow_print(
            "Found extra-index-url in requirements. "
            "Make sure, that you passed --extra-index-url value for module installation"
        )
    else:
        required.append(line)

# add development suffix if required
info["__version__"] += _get_suffix()

setup(
    name=info["__title__"],
    description=info["__description__"],
    version=info["__version__"],
    packages=find_packages(exclude=["examples", "tests*"]),
    install_requires=required,
    dependency_links=dependency_links,
    python_requires="~=3.7",
)
