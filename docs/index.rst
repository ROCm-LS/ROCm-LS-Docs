.. meta::
  :description: ROCm-LS toolkit is a collection of open-source software for high-performance data science applications built on the core ROCm platform.
  :keywords: ROCm-LS, life sciences

**********************
ROCm-LS documentation
**********************

.. note::

  ROCm-LS is in an early access state. Running production workloads is not recommended.

The ROCm Life Science (ROCm-LS) toolkit is a GPU-accelerated library suite developed for life science and healthcare applications, offering a robust set of tools optimized for AMD hardware. It is an open-source software collection for high-performance life science applications built on the core ROCm platform, which helps you accelerate life science processing and analyze workloads on AMD accelerators and GPUs.

You can leverage ROCm-LS to accelerate both new and existing life science workloads, which helps you execute intensive applications with larger datasets relatively fast. ROCm-LS creates scalable solutions to address the needs of today's data-driven landscape. With ROCm-LS, you can build pre- and post-processing applications for your AI models and accelerate your existing life science pipelines with minimal effort.

The ROCm-LS libraries provide tools to build a complete workflow for life science acceleration on AMD GPUs:

- **hipCIM:** A high-performance GPU imaging library that accelerates and scales image processing workflows on AMD Instinct GPUs.

- **MONAI for AMD ROCm:** An open-source framework that brings advanced deep learning capabilities for medical imaging to AMD GPU platforms.

MONAI for AMD ROCm provides out-of-the-box integration with hipCIM, delivering accelerated image I/O and transformation operations for supported whole slide images (WSI). Together, hipCIM and MONAI enable researchers and healthcare professionals to streamline scientific imaging pipelines, boost computational performance, and speed up innovation across a wide array of life science use cases.

The documentation is structured as follows:

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Components

    * `hipCIM <https://rocm.docs.amd.com/projects/hipCIM/en/latest/>`_
    * `MONAI for AMD ROCm <https://rocm.docs.amd.com/projects/monai/en/latest/>`_

  .. grid-item-card:: Related content

    * `ROCm-LS blogs <https://rocm.blogs.amd.com/software-tools-optimization/rocm-ls-intro/README.html>`_
    * :ref:`rocm-ls-contribution`
