"""Configuration file for the Sphinx documentation builder."""
import os
import shutil
import re

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "rocm.docs.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "ROCm for Life Science"

version = "25.06"
release = version
html_title = "ROCm-LS 25.06 documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2025 Advanced Micro Devices, Inc. All rights reserved."
setting_all_article_info = True
all_article_info_os = ["linux"]
all_article_info_author = ""

# Required settings
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm-docs-home",
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']