.. meta::
  :description: ROCm-LS toolkit is a collection of open-source software for high-performance data science applications built on the core ROCm platform.
  :keywords: ROCm-LS, life sciences

**************************
ROCm-LS documentation
**************************

The AMD ROCm™ Life Science toolkit (ROCm-LS) is an open-source, GPU-accelerated library suite for life science and healthcare applications optimized for use on AMD GPUs. 

ROCm-LS can be used to accelerate new and existing life science workloads on AMD devices. The suite targets compute-intensive applications that process larger datasets so that you can build pre-processing and post-processing applications for AI models and accelerate existing life science pipelines.

The ROCm-LS libraries provide the following tools for life science acceleration on AMD GPUs:

- **hipCIM**: A GPU imaging library that accelerates and scales image processing on AMD Instinct™ GPUs.
- **MONAI on ROCm**: An open-source framework that brings deep learning for medical imaging to AMD GPU platforms.
- **MONAI Model Zoo**: A collection of MONAI Bundle models with AMD ROCm inference overlays for validated segmentation workloads on AMD Instinct™ GPUs.
- **MONAILabel**: An interactive medical image labeling framework with Early Access AMD GPU support on ROCm.

These tools are integrated into a comprehensive workflow for scientific imaging pipelines that accelerates image I/O and transformation operations for supported whole slide images on AMD GPUs.

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Components

    - `hipCIM <https://advanced-micro-devices-demo--137.com.readthedocs.build/projects/hipcim-internal/en/137/>`_
    - `MONAI on ROCm <https://advanced-micro-devices-demo--115.com.readthedocs.build/projects/monai-internal/en/115/>`_
    - `MONAI Model Zoo <https://advanced-micro-devices-demo--3.com.readthedocs.build/projects/model-zoo-internal/en/3/>`_
    - MONAILabel

  ..
    * `hipCIM <https://rocm.docs.amd.com/projects/hipCIM/en/docs-26.03/>`_
    * `MONAI on ROCm <https://rocm.docs.amd.com/projects/monai/en/docs-26.03/>`_
    * `MONAI Model Zoo <https://rocm.docs.amd.com/projects/model-zoo/en/docs-26.08/>`_
    * `MONAILabel <https://rocm.docs.amd.com/projects/monailabel/en/docs-26.08/>`_

  .. grid-item-card:: Related content

    - `ROCm-LS blogs <https://instinct.docs.amd.com/latest/life-science/ROCmLS-Blogs.html>`_
    - :ref:`rocm-ls-contribution`

For ready-to-run code samples that demonstrate ROCm-LS capabilities on the AMD ROCm platform, see the `ROCm-LS examples <https://github.com/ROCm-LS/examples>`_.
