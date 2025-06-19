.. meta::
  :description: ROCm-LS toolkit is a collection of open-source software for high-performance data science applications built on the core ROCm platform.
  :keywords: Contributing to ROCm-LS, Contributing to life sciences, ROCm-LS contribution, life sciences contribution

.. _rocm-ls-contribution:

*************************
Contributing to ROCm-LS
*************************

AMD welcomes community contribution to ROCm-LS and its components. Whether those contributions are bug reports, bug fixes, documentation additions, performance notes, or other improvements, we value collaboration with our users. This topic provides guidelines that must be followed to ensure that your contributions are accepted.

Our code contribution guidelines closely follow the GitHub pull requests model. Ensure to create pull requests (PR) against the default branch (develop) in the ROCm-LS components.

Issue discussion
=================

Use the GitHub Issues tab for issue creation.

- Use your best judgment for issue creation. If your issue is already listed, upvote the issue and comment or post to provide additional details, such as how you reproduced this issue.

- If you’re not sure whether your issue is same as the existing one, err on the side of caution and file your issue. You can add a comment to include the issue number (and link) for the similar issue. If we evaluate your issue to be the same as the existing one, we’ll close the duplicate.

- If your issue doesn’t exist, use the issue template to file a new issue.

  - When filing an issue, provide as much information as possible, including script output so we can collect information about your configuration. This helps reduce the time required to reproduce your issue.

  - Check your issue regularly, as we might require additional information to successfully reproduce the issue.

- You can also open an issue to ask the maintainers whether a proposed change meets the acceptance criteria or to discuss an idea about the library.

Acceptance criteria
====================

Any contribution of the following nature is most likely to get accepted:

- Fix bugs, improve documentation, enhance testing, and reduce complexity.

- Improve the performance of existing routines.

- Add missing functionality.

- Add additional formats or allow an existing format to be used with an existing routine.

The contributors have an opportunity to add optimization algorithms to suit important user requirements and performance considerations. We encourage contributors to leverage the GitHub Issues tab to discuss possible additions.

Exceptions
-----------

ROCm-LS places a heavy emphasis on performance. Hence, contributions that add new routines or modify existing routines must offer high performance with respect to the hardware they run on.

Additionally, when adding new routines, ensure that these routines offer enough value to enough users to be deemed worth including. Based on compile times, binary sizes, and general library complexity, we reserve the right to decide whether a proposed routine is too niche or specialized to be worth including.

Code structure
===============

Here is the ROCm-LS library structure as available in the GitHub repository:

- ``library/include/``: Contains the header files, which include headers defining the public API. Also contains headers for all public types.

- ``library/src/``: Contains the implementations of routines. These implementations are divided into directories based on the category the routine belongs to. These directories contain both C++ and HIP kernel code.

- ``clients/directory/``: Contains the testing and benchmarking code along with the samples demonstrating the usage.

- ``docs/``: Contains the documentation files.

- ``scripts/``: Contains potentially useful Python and shell scripts for downloading test matrices (see ``scripts/performance/matrices/``) as well as plotting tools.

Coding style
=============

In general, follow the surrounding code style. C and C++ code is formatted using clang-format. Use the clang-format version installed with ROCm, which is present in the ``/opt/rocm/llvm/bin`` directory. Don't use your system’s built-in clang-format, as a difference in the version might lead to incorrect results.

To format a file, use:

.. code-block:: shell

    /opt/rocm/hcc/bin/clang-format -style=file -i <path-to-source-file>

To format the code per-commit, install githooks:

.. code-block:: shell

    ./.githooks/install

Pull request guidelines
========================

Ensure to create the PR on the default branch. Our default branch is the develop branch, which serves as our integration branch.

Deliverables
-------------

When raising a PR in ROCm-LS, follow these guidelines:

1. For each new file in the repository, include the following licensing header and adjust the date to the current year. When simply modifying a file, the date should automatically be updated when using the pre-commit script.

.. code-block:: shell

    /* ************************************************************************
    * Copyright (C) 20xx Advanced Micro Devices, Inc. All rights Reserved.
    *
    * Permission is hereby granted, free of charge, to any person obtaining a copy
    * of this software and associated documentation files (the "Software"), to deal
    * in the Software without restriction, including without limitation the rights
    * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    * copies of the Software, and to permit persons to whom the Software is
    * furnished to do so, subject to the following conditions:
    *
    * The above copyright notice and this permission notice shall be included in
    * all copies or substantial portions of the Software.
    *
    * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    * THE SOFTWARE.
    *
    * ************************************************************************ */

2. When adding a new routine, ensure to add the appropriate testing code. These new unit tests should integrate within the existing googletest framework. This typically involves adding the following files:

   - testing_<routine_name>.cpp file in the ``clients/testing/`` directory

   - test_<routine_name>.cpp file in the ``clients/tests/`` directory

   - test_<routine_name>.yaml file in the ``clients/tests/`` directory

   When adding new tests, refer to the existing tests for guidelines.

3. When modifying an existing routine, add appropriate tests to test_<routine_name>.yaml file in the ``clients/tests/`` directory.

4. The tests must have good code coverage.

5. Ensure that the code builds successfully. This includes ensuring that the code can compile, is properly formatted, and all tests pass.

6. Don’t break existing tests.

Process
--------

When a PR is raised targeting the develop branch in ROCm-LS, CI will be automatically triggered to:

- Test that the PR passes static analysis, which ensures that the clang formatting rules are followed.

- Test that the documentation can be built properly.

- Ensure that the PR compiles on different OS and GPU device architecture combinations.

- Ensure that all tests pass on different OS and GPU device architecture combinations.

For assistance on any CI failure encountered on your PR, reach out to us.

The code reviewers are listed in the CODEOWNERS file.
