# ROCm-LS 25.11 release notes

The release notes provide a summary of notable changes since the previous ROCm-LS release.

## ROCm-LS release highlights

The following are notable new features and improvements in ROCm-LS 25.11 since the release of 25.09. For detailed changes to individual components, see [detailed component changes](#detailed-component-changes).

- **hipCIM General Availability (GA) 25.10.00:**

    - GA status: hipCIM 25.10.00 exits Early Access (EA) and is now production-ready for life sciences imaging workloads on AMD GPUs.

    - Upstream parity: hipCIM 25.10.00 is based on upstream [RAPIDS™ cuCIM v25.10.00](https://github.com/rapidsai/cucim/releases/tag/v25.10.00) for feature and API parity, as well as easier migration from CUDA-based pipelines.

    - Region property computations and utility functions: This release delivers significant performance and feature improvements for GPU-accelerated imaging on AMD ROCm, with a focus on region property computations and utility functions for common image workflows.

- **ROCm 7.0 support:** ROCm-LS 25.11 adds support for ROCm 7.0 platforms and toolchains while continuing support for ROCm 6.4.

- MONAI 1.0.0 is based on ROCm 6.4 and continues to be in EA.

## ROCm-LS components

The following table lists the versions of ROCm-LS components for ROCm-LS 25.11, including any version changes from 25.09 to 25.11. Click the GitHub icon to go to the component's source code.

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
                <td><a href="https://advanced-micro-devices-hipcim-internal--102.com.readthedocs.build/en/102/">hipCIM</a></td>
                <td>25.10.00</td>
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-25.09/">MONAI for AMD ROCm</a></td>
                <td>1.0.0</td>
                <td><a href="https://github.com/ROCm-LS/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

:::{note}
The MONAI version remains unchanged in this release.
:::

## Detailed component changes

The following sections describe key changes to the ROCm-LS components:

### hipCIM (25.10.00)

This release is based on the upstream [cuCIM v25.10.00 release](https://github.com/rapidsai/cucim/releases/tag/v25.10.00) and includes the following enhancements:

#### Added

- **ROCm versions:** Support for ROCm 7.0 with continued support for ROCm 6.4.

- **Utility functions:** Montage and `compare_images` utility functions for quickly visualizing and validating image outputs in analysis workflows.

- **Geometry and morphology:** GPU-accelerated implementations of `convex_hull_image` and `convex_hull_object` functions.

- **API extensions:** Region properties API extended with `regionprops_table` and accelerated implementations across basic, intensity, moment-based, convexity, perimeter, and Euler characteristic properties.

#### Optimized

- End-to-end acceleration of `regionprops` and `regionprops_table`, reducing computation time and memory overhead on common segmentation and labeling tasks.

- Improved performance for `label2rgb`, offering faster visualization of labeled images in typical post-processing pipelines.

#### Resolved issues

- **Imaging integration:** Improved compatibility with Pillow’s `Image.fromarray` when using deprecated mode parameters, preventing runtime issues in visualization workflows.

- **Morphology and binary operations:** Refreshed binary morphology and `binary_fill_holes` components for correctness and stability.

:::{note}

hipCIM targets functional parity with the most commonly used upstream APIs in the life sciences imaging. Minor behavioral differences might exist due to ROCm backend variations. Validate critical pipelines accordingly.

:::
