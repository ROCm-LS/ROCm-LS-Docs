# ROCm-LS 25.11 release notes

The release notes provide a summary of notable changes since the previous ROCm-LS release.

## ROCm-LS release highlights

The following are notable new features and improvements in ROCm-LS 25.11 since the release of 25.09:

- hipCIM General Availability (GA) 25.10.00:

    - GA status: hipCIM 25.10.00 exits Early Access (EA) and is now production-ready for life sciences imaging workloads on AMD GPUs.

    - Version alignment: hipCIM 25.10.00 is based on upstream cuCIM 25.10 for API parity and easier migration from CUDA-based pipelines.

- ROCm 7.0 support: ROCm-LS 25.11 adds support for ROCm 7.0 platforms and toolchains.

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
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/latest/">hipCIM</a></td>
                <td>25.10.00</td>
                <td><a href="https://github.com/ROCm-LS/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/latest/">MONAI for AMD ROCm</a></td>
                <td>1.0.0</td>
                <td><a href="https://github.com/ROCm-LS/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

:::{note}
The MONAI version remains unchanged in this release.
:::
