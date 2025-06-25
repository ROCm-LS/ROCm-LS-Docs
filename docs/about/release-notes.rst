.. meta::
  :description: ROCm-LS toolkit is a collection of open-source software for high-performance data science applications built on the core ROCm platform.
  :keywords: ROCm-LS release, life sciences release

.. _rocm-ls-release:

**********************
ROCm-LS release notes
**********************

We are excited to announce the early access release of ROCm-LS, a new software toolkit designed to accelerate life science workloads on selected AMD Instinct GPUs. This release serves as a preview of the capabilities enabled by the future ROCm-LS releases and is not intended for production workloads.

ROCm-LS release highlights
===========================

ROCm-LS is a GPU-accelerated life science library, similar to the NVIDIA CLARA software collection. The early access release features a single library, hipCIM.

hipCIM is an open-source, accelerated computer vision and image processing software library for multidimensional images used in biomedical, geospatial, material and life science, and remote sensing use cases.

.. note::

    The 25.06 release is a technology preview and is NOT intended for production workloads.

ROCm-LS components
===================

The following table lists the ROCm-LS components available in the current release. To access the component’s source code on GitHub, click the component name.

.. list-table::

    * - **Component**
      - **Version**

    * - `hipCIM <https://github.com/AMD-AIOSS/hipCIM>`_
      - 1.0.00

hipCIM
-------

hipCIM enables accelerated computer vision and image processing for multidimensional images used in biomedical, geospatial, material and life science, and remote sensing use cases. hipCIM offers both a Python and C++ API, allowing for a wide range of use cases. Despite being named hipCIM, this library is API compatible with the NVIDIA cuCIM library, allowing for workloads to be transitioned to AMD devices without the need for hipification.

hipCIM supports the following image formats:

- Single level Aperio ScanScope Virtual Slide (SVS) with JPEG compression

- Single level Philips TIFF with JPEG compression

Note that the image support is limited by `rocJPEG chroma subsampling and hardware capabilities <https://rocm.docs.amd.com/projects/rocJPEG/en/latest/reference/rocjpeg-formats-and-architectures.html>`_.

hipCIM API mirrors `scikit-image <https://scikit-image.org/>`_ for image manipulation and `OpenSlide <https://openslide.org/>`_ for image loading.

hipCIM is fully open source under the Apache-2.0 license and available for contribution.

Compatibility matrix
=====================

.. list-table::

    * - **Operating system**
      - **ROCm version**
      - **Python version**
      - **Hardware**
      - **Support status**

    * - Ubuntu 22.04
      - 6.4
      - 3.10.12
      - MI300 / gfx942
      - hipCIM 1.0.00

For hipCIM supported features and limitations, see :ref:`supported-features`.
