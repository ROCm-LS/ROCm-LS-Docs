# ROCm-LS 25.09 release notes

We are excited to announce the early access release of ROCm-LS, a new software toolkit designed to accelerate life science workloads on selected AMD Instinct GPUs. This release serves as a preview of the capabilities enabled by the future ROCm-LS releases and is not intended for production workloads.

This early access release features hipCIM, a high-performance GPU imaging library that accelerates and scales image processing workflows on AMD Instinct GPUs. MONAI for AMD ROCm is introduced as an open-source framework that brings advanced deep learning capabilities for medical imaging to AMD’s GPU platforms. Notably, MONAI for AMD ROCm now provides out-of-the-box integration with hipCIM, delivering accelerated image I/O and transformation operations for supported whole slide images (WSI). Together, hipCIM and MONAI enable researchers and healthcare professionals to streamline scientific imaging pipelines, boost computational performance, and speed up innovation across a wide array of life science use cases.

## ROCm-LS release highlights

ROCm-LS is a collection of GPU-accelerated life science libraries. The early access release features:

- **hipCIM 1.0.0:** An open-source, accelerated computer vision and image processing software library for multidimensional images used in biomedical, geospatial, material and life science, and remote sensing use cases.

- **MONAI 1.0.0 for AMD ROCm:** A deep learning framework for healthcare imaging.

:::{note}
ROCm-LS is in an early access state. Running production workloads is not recommended.
:::

## ROCm-LS components

The following table lists the ROCm-LS components available in the current release. Click the GitHub icon to go to the component's source code.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Category</th>
                <th>Component name</th>
                <th>Version</th>
                <th>Description</th>
                <th>Source code</th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-components-libs rocm-components-ml">
            <tr>
                <td>Imaging</td>
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/latest/">hipCIM</a></td>
                <td>1.0.00</td>
                <td>GPU-accelerated image I/O and processing</td>
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/latest/">MONAI for AMD ROCm</a></td>
                <td>1.0.0</td>
                <td>Deep learning framework for medical imaging</td>
                <td><a href="https://github.com/ROCm-LS/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

### hipCIM

hipCIM enables accelerated computer vision and image processing for multidimensional images used in biomedical, geospatial, material and life science, and remote sensing use cases. hipCIM offers both a Python and C++ API, allowing for a wide range of use cases. Despite being named hipCIM, this library is API compatible with the NVIDIA cuCIM library, allowing for workloads to be transitioned to AMD devices without the need for hipification.

hipCIM supports the following image formats:

- Single level Aperio ScanScope Virtual Slide (SVS) with JPEG compression

- Single level Philips TIFF with JPEG compression

Note that the image support is limited by [rocJPEG chroma subsampling and hardware capabilities](https://rocm.docs.amd.com/projects/rocJPEG/en/latest/reference/rocjpeg-formats-and-architectures.html).

hipCIM API mirrors [scikit-image](https://scikit-image.org/) for image manipulation and [OpenSlide](https://openslide.org/) for image loading.

hipCIM is fully open source under the Apache-2.0 license and available for contribution.

### MONAI for AMD ROCm

MONAI (Medical Open Network for AI) is a PyTorch-based, open-source framework designed for healthcare imaging deep learning. AMD now provides ROCm-enabled MONAI builds optimized for AMD GPUs as a ROCm-LS component, which enables scalable medical AI workflows on AMD hardware.

**Key features:**

- Optimized for 3D medical imaging: Supports CT, MRI, Ultrasound, and other volumetric modalities with domain-specific optimizations.

- Prebuilt training pipelines: Supports segmentation, classification, and detection tasks, reducing setup overhead.

- Model Zoo with pretrained models: Provides access to a wide collection of pretrained models from the MONAI Model Zoo, ready for fine-tuning on custom datasets. Examples include UNet, SegResNet, SwinUNETR, and various organ-specific models.

- Seamless integration with hipCIM - Enables accelerated image I/O and transformations for supported whole slide images (WSI).

**Benefits of ROCm-LS MONAI for AMD ROCm integration:**

- GPU acceleration on AMD Instinct MI300 series accelerators (gfx942)

- API compatibility with upstream MONAI without requiring any code changes

- Validation with hipCIM image processing workflows

## Compatibility matrix

| Operating system | ROCm version | Python version | Hardware | Support status |
|------------------|--------------|----------------|----------|----------------|
| Ubuntu 22.04 | 6.4.0 | 3.10.12 | Instinct MI300 series (gfx942) | <ul><li>hipCIM 1.0.00</li><li>MONAI 1.0.0 for AMD ROCm</li></ul> |

## Supported functionalities

- hipCIM 1.0.00 is based on [cuCIM 25.04.00](https://github.com/rapidsai/cucim/tree/branch-25.04) and offers GPU acceleration for the following features:

  - Core image interface

  - Whole slide imaging

  - Image processing (skimage)

  - Segmentation

  - Color operations

  - Measurement functions

  For hipCIM supported features and limitations, see [Supported hipCIM functionality](https://rocm.docs.amd.com/projects/hipCIM/en/latest/reference/supported-functionality.html)

- MONAI 1.0.0 for AMD ROCm is based on [MONAI upstream version 1.5.0](https://github.com/Project-MONAI/MONAI/commit/d388d1c6fec8cb3a0eebee5b5a0b9776ca59ca83) and offers the following features:

  - Common MONAI model architectures for segmentation, classification, registration, generative models, federated learning, and AutoML

  - Integration with PyTorch for AMD ROCm

  - Training pipelines optimized for AMD Instinct GPUs.
