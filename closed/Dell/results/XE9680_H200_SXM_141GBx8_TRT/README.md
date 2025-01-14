
See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/GATEOverflow/inference_results_v4.1/blob/main/closed/Dell/results/XE9680_H200_SXM_141GBx8_TRT/summary.html)



<div class="resultpage">
 <div class="titlebarcontainer">
  <div class="logo">
   <a href="/" style="border: none"><img src="" alt="" /></a>
  </div>
  <div class="titlebar">
   <h1 class="title">MLPerf Inference v4.1</h1>
   <p style="font-size: smaller">Copyright 2019-2025 MLCommons</p>
  </div>
 </div>
 <table class="titlebarcontainer">
  <tr>
   <td class="headerbar" rowspan="2">
    <p>Dell     </p>
    <p>Dell PowerEdge XE9680 (8x H200-SXM-141GB, TensorRT)    </p>
   </td>
  </tr>
 </table>
 <table class="datebar">
  <tbody>
   <tr>
    <th id="license_num"><a href="">MLPerf Inference Category:</a></th>
    <td id="license_num_val">datacenter</td>
    <th id="test_date"><a href="">MLPerf Inference Division:</a></th>
    <td id="test_date_val">closed</td>
   </tr>
   <tr>
    <th id="tester"><a href="">Submitted by:</a></th>
    <td id="tester_val">Dell</td>
    <th id="sw_avail"><a href="">Availability:</a></th>
    <td id="sw_avail_val">Available  as of August 2024</td>
   </tr>
  </tbody>
 </table>
  
<table>
            <tr><td><h3>Accelerator Details</h3><table><tr><td>accelerator_frequency</td><td></td></tr><tr><td>accelerator_host_interconnect</td><td>PCIe Gen5 x16</td></tr><tr><td>accelerator_interconnect</td><td>NVLINK</td></tr><tr><td>accelerator_interconnect_topology</td><td>NVLINK Switch</td></tr><tr><td>accelerator_memory_capacity</td><td>141 GB</td></tr><tr><td>accelerator_memory_configuration</td><td>HBM3e</td></tr><tr><td>accelerator_model_name</td><td>NVIDIA H200-SXM-141GB</td></tr><tr><td>accelerator_on-chip_memories</td><td></td></tr><tr><td>accelerators_per_node</td><td>8</td></tr></table></td> <td><h3>Processor and Memory Details</h3><table><tr><td>host_memory_capacity</td><td>2 TB</td></tr><tr><td>host_memory_configuration</td><td>32x 64GB DDR5</td></tr><tr><td>host_processor_caches</td><td></td></tr><tr><td>host_processor_core_count</td><td>52</td></tr><tr><td>host_processor_frequency</td><td></td></tr><tr><td>host_processor_interconnect</td><td></td></tr><tr><td>host_processor_model_name</td><td>Intel(R) Xeon(R) Platinum 8470</td></tr><tr><td>host_processors_per_node</td><td>2</td></tr></table></td> </tr>
            <tr><td ><h3>Other Hardware Details</h3><table><tr><td>cooling</td><td>air-cooled</td></tr><tr><td>disk_controllers</td><td>NVMe</td></tr><tr><td>disk_drives</td><td></td></tr><tr><td>hw_notes</td><td>H200 TGP 700W</td></tr><tr><td>other_hardware</td><td></td></tr><tr><td>power_management</td><td></td></tr><tr><td>power_supply_details</td><td></td></tr><tr><td>power_supply_quantity_and_rating_watts</td><td></td></tr></table></td> <td><h3>Network and Interconnect Details</h3><table><tr><td>host_networking</td><td>Infiniband:Data bandwidth for GPU-PCIe: 504GB/s; PCIe-NIC: 500GB/s</td></tr><tr><td>host_networking_topology</td><td>Ethernet/Infiniband on switching network</td></tr><tr><td>host_network_card_count</td><td>10x 400Gb Infiniband</td></tr><tr><td>network_speed_mbit</td><td></td></tr><tr><td>nics_enabled_connected</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>nics_enabled_os</td><td></td></tr><tr><td>number_of_type_nics_installed</td><td></td></tr></table></td> </tr>
            <tr><td colspan="2"><h3>Software Details</h3><table><tr><td>boot_firmware_version</td><td></td></tr><tr><td>framework</td><td>TensorRT 10.2.0, CUDA 12.4</td></tr><tr><td>management_firmware_version</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>operating_system</td><td>Ubuntu 22.04.3</td></tr><tr><td>other_software_stack</td><td>TensorRT 10.2.0, CUDA 12.5, cuDNN 8.9.7, Driver 555.42.06</td></tr><tr><td>sw_notes</td><td></td></tr></table></td> </tr>
            </table>

<h3>Results Table</h3>
<table>
    <tr>
        <th rowspan="2">Model</th>
        <th rowspan="2">Accuracy Target</th>
        <th colspan="2">Server</th>
        <th colspan="2">Offline</th>
    </tr>
    <tr>
    <td>Metric</td>
    <td>Performance</td>
    <td>Metric</td>
    <td>Performance</td>
    </tr><tr><td>resnet</td><td>acc: 75.6954</td><td>Queries/s</td> <td>630226.0</td><td>Samples/s</td> <td>768235.0</td><tr><td>retinanet</td><td>mAP: 37.1745</td><td>Queries/s</td> <td>13603.8</td><td>Samples/s</td> <td>14760.1</td><tr><td>bert-99</td><td>F1: 89.9653</td><td>Queries/s</td> <td>58091.3</td><td>Samples/s</td> <td>73791.0</td><tr><td>bert-99.9</td><td>F1: 90.7831</td><td>Queries/s</td> <td>51213.5</td><td>Samples/s</td> <td>65322.6</td><tr><td>3d-unet-99</td><td>DICE: 0.8531</td><td colspan="2"> N/A </td><td>Samples/s</td> <td>54.6196</td><tr><td>3d-unet-99.9</td><td>DICE: 0.8608</td><td colspan="2"> N/A </td><td>Samples/s</td> <td>54.6196</td><tr><td>gptj-99</td><td>ROUGE1: 42.5566, ROUGE2: 19.9223, ROUGEL: 29.6882, GEN_LEN: 3615190.2</td><td>Tokens/s</td> <td>20139.0</td><td>Tokens/s</td> <td>20238.4</td><tr><td>gptj-99.9</td><td>ROUGE1: 42.9435, ROUGE2: 20.1034, ROUGEL: 29.9581, GEN_LEN: 3615190.2</td><td>Tokens/s</td> <td>20139.0</td><td>Tokens/s</td> <td>20238.4</td><tr><td>llama2-70b-99</td><td>ROUGE1: 43.9869, ROUGE2: 21.8148, ROUGEL: 28.33, TOKENS_PER_SAMPLE: 265.005</td><td>Tokens/s</td> <td>29739.9</td><td>Tokens/s</td> <td>32124.3</td><tr><td>llama2-70b-99.9</td><td>ROUGE1: 44.3868, ROUGE2: 22.0132, ROUGEL: 28.5876, TOKENS_PER_SAMPLE: 265.005</td><td>Tokens/s</td> <td>29739.9</td><td>Tokens/s</td> <td>32124.3</td><tr><td>stable-diffusion-xl</td><td>CLIP_SCORE: 31.6863, FID_SCORE: 23.0109</td><td>Queries/s</td> <td>16.6945</td><td>Samples/s</td> <td>17.6742</td></table>

