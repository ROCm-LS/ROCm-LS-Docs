## Compatibility matrix

Use this matrix to view the ROCm-LS compatibility and system requirements across the releases:

<div class="pst-scrollable-table-container">
    <table id="compatibility-matrix" class="table">
        <thead>
            <style>
                table {
                    border-collapse: collapse;
                    border-spacing: 0;
                    }
                td, th {
                    border: 1px solid black;
                    }
                tbody [rowspan] ~ td {
                    border: 1px solid black;
                    }
            </style>
            <tr>
                <th>ROCm-LS version</th>
                <th>Supported components</th>
                <th>AMD Instinct GPU</th>
                <th>ROCm version</th>
                <th>Ubuntu version</th>
                <th>Python version</th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-ls-components">
            <tr>
                <th rowspan="3">25.11</th>
                <td rowspan="2"><a href ="https://rocm.docs.amd.com/projects/hipCIM/en/docs-25.11/">hipCIM 25.10.00</a></td>
                <td>MI300A</td>
                <td>7.0.2</td>
                <td>24.04</td>
                <td>3.12</td>
            </tr>
            <tr>
                <td>MI325X</td>
                <td>6.4.3</td>
                <td>22.04</td>
                <td>3.10</td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-25.11/">MONAI 1.0.0 for AMD ROCm (EA)</a></td>
                <td>MI300X</td>
                <td>6.4.3</td>
                <td>22.04</td>
                <td>3.10</td>
            </tr>
            <tr>
                <th rowspan="2">25.09</th>
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/docs-25.09/">hipCIM 25.04.00</a></td>
                <td>MI325X</td>
                <td rowspan="2">6.4.3</td>
                <td rowspan="2">22.04</td>
                <td rowspan="2">3.10</td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-25.09/">MONAI 1.0.0 for AMD ROCm (EA)</a></td>
                <td>MI300X</td>
            </tr>
            <tr>
                <th>25.06</th>
                <td><a href = "https://rocm.docs.amd.com/projects/hipCIM/en/docs-25.06/">hipCIM 25.04.00</a></td>
                <td>MI325X</td>
                <td>6.4.3</td>
                <td>22.04</td>
                <td>3.10</td>
            </tr>
        </tbody>
    </table>
</div>
