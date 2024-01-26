# INTEL CONFIDENTIAL
# Copyright 2023 Intel Corporation.
#
# This software and the related documents are Intel copyrighted materials, and your use of them is governed
# by the express license under which they were provided to you ("License"). Unless the License provides otherwise,
# you may not use, modify, copy, publish, distribute, disclose or transmit this software or the related documents
# without Intel's prior written permission.
#
# This software and the related documents are provided as is, with no express or implied warranties,
# other than those that are expressly stated in the License.
"""Generate sphinx docs."""

import os
import shutil
import logging

from sphinx.ext import apidoc
from sphinx.cmd import build


apidoc.main(["-e", "-o", "mfd_testing", os.path.join("..", "mfd_testing")])

build.main(["-b", "html", ".", "build/html"])

logging.info("Cleaning folders from build process...")
shutil.rmtree("mfd_testing")
