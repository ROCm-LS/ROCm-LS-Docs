
.. meta::
  :description: ROCm-LS toolkit is a collection of open-source software for high-performance data science applications built on the core ROCm platform.
  :keywords: ROCm-LS, life sciences

.. _rocm-ls-compat-matrix:

=============================
ROCm-LS compatibility matrix
=============================

Use the following matrix to view the ROCm-LS compatibility and system requirements across releases:

.. role:: version-start

.. table::
   :width: 65%
   :widths: 20 20 20 12 12 12
   :align: left
   :class: compat-matrix format-big-table

   +------------------------+--------------------------------------+-------------------+--------------+----------------+----------------+
   |  ROCm-LS version       |  Supported component                 | AMD Instinct™ GPU | ROCm version | Ubuntu version | Python version |
   +========================+======================================+===================+==============+================+================+
   | :version-start:`26.03` | `hipCIM 25.10.00                     | MI355X,           | 7.2.0,       | 24.04          | 3.12           |
   |                        | <https://rocm.docs.amd.com/projects  | MI325X,           | 7.0.2        |                |                |
   |                        | /hipCIM/en/docs-26.03/>`_            | MI300X            |              |                |                |
   +                        +--------------------------------------+-------------------+--------------+----------------+----------------+
   |                        | `MONAI 1.5.2 on ROCm                 | MI355X,           | 7.2.0,       | 24.04          | 3.12           |
   |                        | <https://rocm.docs.amd.com/projects/ | MI325X,           | 7.0.2        |                |                |
   |                        | monai/en/docs-26.03/>`_              | MI300X            |              |                |                |
   +------------------------+--------------------------------------+-------------------+--------------+----------------+----------------+
   | :version-start:`25.11` | `hipCIM 25.10.00                     | MI300A            | 7.0.2        | 24.04          | 3.12           |
   +                        + <https://rocm.docs.amd.com/projects  +-------------------+--------------+----------------+----------------+
   |                        | /hipCIM/en/docs-25.11/>`_            | MI325X            | 6.4.3        | 22.04          | 3.10           |
   +                        +--------------------------------------+-------------------+--------------+----------------+----------------+
   |                        | `MONAI 1.5.0 on ROCm (EA)            | MI300X            | 6.4.3        | 22.04          | 3.10           |
   |                        | <https://advanced-micro-devices-demo |                   |              |                |                |
   |                        | --22.com.readthedocs.build/projects/ |                   |              |                |                |
   |                        | monai/en/22/>`_                      |                   |              |                |                |
   +------------------------+--------------------------------------+-------------------+--------------+----------------+----------------+
   | :version-start:`25.09` | `hipCIM 25.04.00                     | MI325X            | 6.4.3        | 22.04          | 3.10           |
   |                        | <https://rocm.docs.amd.com/projects  |                   |              |                |                |
   |                        | /hipCIM/en/docs-25.09/>`_            |                   |              |                |                |
   +                        +--------------------------------------+-------------------+--------------+----------------+----------------+
   |                        | `MONAI 1.5.0 on ROCm (EA)            | MI300X            | 6.4.3        | 22.04          | 3.10           |
   |                        | <https://advanced-micro-devices-demo |                   |              |                |                |
   |                        | --22.com.readthedocs.build/projects/ |                   |              |                |                |
   |                        | monai/en/22/>`_                      |                   |              |                |                |
   +------------------------+--------------------------------------+-------------------+--------------+----------------+----------------+
   | :version-start:`25.06` | `hipCIM 25.04.00                     | MI325X            | 6.4.3        | 22.04          | 3.10           |
   |                        | <https://rocm.docs.amd.com/projects  |                   |              |                |                |
   |                        | /hipCIM/en/docs-25.06/>`_            |                   |              |                |                |
   +------------------------+--------------------------------------+-------------------+--------------+----------------+----------------+
