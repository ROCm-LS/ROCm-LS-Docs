# ROCm-LS 26.03 release notes

The release notes provide a summary of notable changes since the previous ROCm-LS release.

## Release highlights

The following are notable new features and improvements in ROCm-LS 26.03 since the 25.11 release. For detailed changes to individual components, see [detailed component changelogs](#detailed-component-changelogs).

- **MONAI 1.5.2 on ROCm** exits Early Access (EA) state and is now production-ready for life sciences imaging workloads on AMD GPUs. It's based on the upstream project [MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/releases/tag/1.5.2)

- **ROCm 7.2.0 support:** ROCm-LS 26.03 adds support for ROCm 7.2.0 while continuing support for ROCm 7.0.2.

## ROCm-LS components

The following table lists the versions of ROCm-LS components for ROCm-LS 26.03, including any version changes from 25.11 to 26.03. Click the GitHub icon to go to the component's source code.

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
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/docs-26.03/">hipCIM</a></td>
                <td>25.10.00</td>
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-26.03/">MONAI on ROCm</a></td>
                <td>1.5.0&nbsp;&Rightarrow;&nbsp;<a href="#monai-on-rocm-1-5-2">1.5.2</a></td>
                <td><a href="https://github.com/ROCm-LS/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

:::{note}
The hipCIM version remains unchanged in this release.
:::

## Detailed component changelogs

The following sections describe key changes to the ROCm-LS components:

### hipCIM (25.10.00)

#### Added

- Support for ROCm 7.2.0 (support for ROCm 7.0.2 is maintained).

- Support for AMD Instinct™ GPUs MI355X and MI300X.

#### Removed

- Support for ROCm 6.4.3.

- Support for Ubuntu 22.04 and Python 3.10.

- Support for AMD Instinct GPU MI300A.

### MONAI on ROCm (1.5.2)

This release is based on the upstream [MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/releases/tag/1.5.2) release. Apart from the changes introduced in the [upstream MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/compare/releasing/1.5.0...1.5.2), MONAI on ROCm 1.5.2 includes the following changes:

#### Added

- Support for ROCm 7.2.0.

- Support for [PyTorch for AMD ROCm](https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/) 2.8 and later.

- Support for AMD Instinct GPUs MI355X and MI325X.

- Support for Ubuntu 24.04 and Python 3.12.

#### Known issues

- Issues with GMM kernel on Multi-GPU.

- MIOpen runtime issue with 3D data on Multi‑GPU for 3D convolutions.
