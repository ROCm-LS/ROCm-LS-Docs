# ROCm-LS 26.03 release notes

The release notes provide a summary of notable changes since the previous ROCm-LS release.

## Release highlights

The following are notable new features and improvements in ROCm-LS 26.03 since the release of 25.11. For detailed changes to individual components, see [detailed component changes](#detailed-component-changes).

- **MONAI 1.5.2 for AMD ROCm** exits Early Access (EA) and is now production ready for life sciences imaging workloads on AMD GPUs. It is based on the upstream project [MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/releases/tag/1.5.2)

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
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/docs-25.11/">hipCIM</a></td>
                <td>25.10.00</td>
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-25.09/">MONAI for AMD ROCm</a></td>
                <td>1.5.0&nbsp;&Rightarrow;&nbsp;<a href="#monai-1-5-2">1.5.2</a></td>
                <td><a href="https://github.com/ROCm-LS/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

:::{note}
The hipCIM version remains unchanged in this release, with only added support for ROCm 7.2.0.
:::

## Detailed component changes

The following sections describe key changes to the ROCm-LS components:

### hipCIM (25.10.00)

#### Added

- Support for ROCm 7.2.0 with continued support for ROCm 7.0.2.

### MONAI (1.5.2)

This release is based on the upstream [MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/releases/tag/1.5.2) release and includes the following enhancements:

#### Added

- Support for ROCm 7.2.0 with continued support for ROCm 7.0.2.

- Support for PyTorch 2.7 and 2.8 for AMD ROCm.

- Input validation for the `ImageStats` class.

- Support for optional conditioning in `PatchInferer`, `SliceInferer`, and `SlidingWindowInferer`.

- A `cfg_fill_value` parameter to classifier-free guidance sampling to help users control the value used for the unconditioned tensor instead of the previously hard-coded value `-1`.

- Provision to pass custom timeout to the CI job to save resources.

#### Changed

- Updated the supported version of Hugging Face transformers.

#### Optimized

- Improved `DiffusionModelEncoder` to support output linear layers of different dimensions.

- Improved documentation on the `datalist` format.

- Refactored and cleaned up the tests.

- Improved the orientation transform to use the "space" (LPS vs. RAS) of a metatensor by default.

- Ensured that additional keyword arguments `**kwargs` are correctly propagated through `ResizeWithPadOrCrop` and related zoom, pad, and crop operations, preventing extra parameters from being silently ignored in certain workflows.

#### Resolved issues

- Fixed the insecure zip file extraction to address `GHSA-x6ww-pf9m-m73m`.

- Fixed the insecure use of `torch.load` and pickle to address `GHSA-6vm5-6jv9-rjpj` and `GHSA-p8cm-mm2v-gwjm`.

- Fixed Torchvision for loading pretrained weights using the current syntax.

- Fixed bug in MAISI `vae`.

- Ensured that invalid images in the RetinaNet detector throw an exception.

- Fixed the `HistogramNormalized` document.

- Fixed a build failure by pinning `pyamg` to versions earlier than 5.3.0.

- Fixed hardcoded input `dim` in `DiffusionModelEncoder`.

- Fixed `gdown` download failure.

#### Known issues

- GMM layer failure on Multi-GPU.

- MIOpen 3D backward pass errors on Multi‑GPU.

- 3D grad‑based visualization not functional on Multi‑GPU.

### MONAI (1.5.0)

#### Added

- Support for ROCm 7.0.2.

- Support for PyTorch 2.7 and 2.8 for AMD ROCm.

#### Removed

- Support for ROCm 6.4.3.

#### Known issues

- GMM layer failure on Multi-GPU.

- MIOpen issue on Multi‑GPU.
