# ROCm-LS 25.09 release notes

The release notes provide a summary of notable changes since the previous ROCm-LS release.

This early access release serves as a preview and is not intended for production workloads.

## ROCm-LS release highlights

The following are notable new features and improvements in ROCm-LS 25.09 since the release of 25.06.

### Introducing MONAI for AMD ROCm

MONAI (Medical Open Network for AI) is a PyTorch-based, open-source framework designed for deep learning in healthcare imaging. AMD now provides ROCm-enabled MONAI builds optimized for AMD GPUs as a ROCm-LS component, which enables scalable medical AI workflows on AMD hardware.

MONAI for AMD ROCm offers the following advantages:

- GPU acceleration on AMD Instinct MI300 Series accelerators (gfx942)

- API compatibility with upstream MONAI without requiring any code changes

- Validation with hipCIM image processing workflows

For more information, see [MONAI for AMD ROCm documentation](https://rocm.docs.amd.com/projects/monai-internal/en/swraw-doc-creation/index.html)

## ROCm-LS components

The following table lists the versions of ROCm-LS components for ROCm-LS 25.09, including any version changes from 25.06 to 25.09. Click the GitHub icon to go to the component's source code.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Category</th>
                <th>Component name</th>
                <th>Version</th>
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
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai-internal/en/swraw-doc-creation/index.html">MONAI for AMD ROCm</a></td>
                <td>1.0.0</td>
                <td><a href="https://github.com/AMD-AIOSS/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

:::{note}
The hipCIM version remains unchanged in this release.
:::
