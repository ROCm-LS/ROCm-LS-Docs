# ROCm-LS 25.06 release notes

We are excited to announce the early access release of ROCm-LS, a new software toolkit designed to accelerate life science workloads on selected AMD Instinct GPUs. This release serves as a preview of the capabilities enabled by the future ROCm-LS releases and is not intended for production workloads.

## ROCm-LS release highlights

ROCm-LS is a GPU-accelerated life science library. The early access release features a single library, hipCIM.

hipCIM is an open-source, accelerated computer vision and image processing software library for multidimensional images used in biomedical, geospatial, material and life science, and remote sensing use cases.

:::{note}
ROCm-LS is in an early access state. Running production workloads is not recommended.
:::

## ROCm-LS components

The following table lists the ROCm-LS components available in the current release. Click the GitHub icon to go to the component's source code.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Component</th>
                <th>Version</th>
                <th></th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-components-libs rocm-components-ml">
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/release-1.0.x/">hipCIM</a></td>
                <td>1.0.00</td>
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
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

## Compatibility matrix

| Operating system | ROCm version | Python version | Hardware | Support status |
|------------------|--------------|----------------|----------|----------------|
| Ubuntu 22.04 | 6.4.0 | 3.10.12 | Instinct MI300 series (gfx942) | hipCIM 1.0.00 |

For hipCIM supported features and limitations, see [Supported hipCIM functionality](https://rocm.docs.amd.com/projects/hipCIM/en/release-1.0.x/reference/supported-functionality.html)
