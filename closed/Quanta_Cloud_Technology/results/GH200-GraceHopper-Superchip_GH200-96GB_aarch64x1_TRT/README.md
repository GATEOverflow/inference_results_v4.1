
See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/GATEOverflow/inference_results_v4.1/blob/main/closed/Quanta_Cloud_Technology/results/GH200-GraceHopper-Superchip_GH200-96GB_aarch64x1_TRT/summary.html)



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
    <p>Quanta_Cloud_Technology     </p>
    <p>GH200-GraceHopper-Superchip_GH200-96GB_aarch64x1_TRT    </p>
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
    <td id="tester_val">Quanta_Cloud_Technology</td>
    <th id="sw_avail"><a href="">Availability:</a></th>
    <td id="sw_avail_val">Available  as of August 2024</td>
   </tr>
  </tbody>
 </table>
  
<table>
            <tr><td><h3>Accelerator Details</h3><table><tr><td>accelerator_frequency</td><td></td></tr><tr><td>accelerator_host_interconnect</td><td>NVLink-C2C</td></tr><tr><td>accelerator_interconnect</td><td>1x 400Gbe Infiniband</td></tr><tr><td>accelerator_interconnect_topology</td><td></td></tr><tr><td>accelerator_memory_capacity</td><td>96 GB</td></tr><tr><td>accelerator_memory_configuration</td><td>HBM3</td></tr><tr><td>accelerator_model_name</td><td>NVIDIA GH200 Grace Hopper Superchip 96GB</td></tr><tr><td>accelerator_on-chip_memories</td><td></td></tr><tr><td>accelerators_per_node</td><td>1</td></tr></table></td> <td><h3>Processor and Memory Details</h3><table><tr><td>host_memory_capacity</td><td>512 GB</td></tr><tr><td>host_memory_configuration</td><td>16x 16DP (32GB) LPDDR5x</td></tr><tr><td>host_processor_caches</td><td></td></tr><tr><td>host_processor_core_count</td><td>72</td></tr><tr><td>host_processor_frequency</td><td></td></tr><tr><td>host_processor_interconnect</td><td></td></tr><tr><td>host_processor_model_name</td><td>NVIDIA Grace CPU</td></tr><tr><td>host_processors_per_node</td><td>1</td></tr></table></td> </tr>
            <tr><td ><h3>Other Hardware Details</h3><table><tr><td>cooling</td><td>Air-cooled</td></tr><tr><td>disk_controllers</td><td>NVMe</td></tr><tr><td>disk_drives</td><td>SSD</td></tr><tr><td>hw_notes</td><td>QuantaGrid S74G-2U</td></tr><tr><td>other_hardware</td><td></td></tr><tr><td>power_management</td><td></td></tr><tr><td>power_supply_details</td><td></td></tr><tr><td>power_supply_quantity_and_rating_watts</td><td></td></tr></table></td> <td><h3>Network and Interconnect Details</h3><table><tr><td>host_network_card_count</td><td>1x 10Gbe Intel Ethernet X550T</td></tr><tr><td>host_networking</td><td>Ethernet; Data bandwidth for GPU-NIC is 252.06 GB/s</td></tr><tr><td>host_networking_topology</td><td>Ethernet/Infiniband on switching network</td></tr><tr><td>network_speed_mbit</td><td></td></tr><tr><td>nics_enabled_connected</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>nics_enabled_os</td><td></td></tr><tr><td>number_of_type_nics_installed</td><td></td></tr></table></td> </tr>
            <tr><td colspan="2"><h3>Software Details</h3><table><tr><td>boot_firmware_version</td><td></td></tr><tr><td>framework</td><td>TensorRT 10.2.0.19, CUDA 12.4</td></tr><tr><td>management_firmware_version</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>operating_system</td><td>Rocky Linux 9.3</td></tr><tr><td>other_software_stack</td><td>CUDA 12.4, cuDNN 8.9.7.29, Driver 550.54.14</td></tr><tr><td>sw_notes</td><td></td></tr></table></td> </tr>
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
    </tr><tr><td>resnet</td><td>acc: 75.6954</td><td>Queries/s</td> <td>73014.9</td><td>Samples/s</td> <td>94990.9</td><tr><td>retinanet</td><td>mAP: 37.1745</td><td>Queries/s</td> <td>1731.14</td><td>Samples/s</td> <td>1923.2</td><tr><td>bert-99</td><td>F1: 89.9653</td><td>Queries/s</td> <td>7103.12</td><td>Samples/s</td> <td>9196.01</td><tr><td>bert-99.9</td><td>F1: 90.7831</td><td>Queries/s</td> <td>6600.99</td><td>Samples/s</td> <td>8092.46</td><tr><td>dlrm-v2-99</td><td>AUC: 79.5069</td><td>Queries/s</td> <td>77511.7</td><td>Samples/s</td> <td>80878.4</td><tr><td>dlrm-v2-99.9</td><td>AUC: 80.2297</td><td>Queries/s</td> <td>46207.5</td><td>Samples/s</td> <td>48197.0</td><tr><td>3d-unet-99</td><td>DICE: 0.8531</td><td colspan="2"> N/A </td><td>Samples/s</td> <td>6.77957</td><tr><td>3d-unet-99.9</td><td>DICE: 0.8608</td><td colspan="2"> N/A </td><td>Samples/s</td> <td>6.77957</td><tr><td>gptj-99</td><td>ROUGE1: 42.5566, ROUGE2: 19.9223, ROUGEL: 29.6882, GEN_LEN: 3615190.2</td><td>Tokens/s</td> <td>2160.12</td><td>Tokens/s</td> <td>2803.72</td><tr><td>gptj-99.9</td><td>ROUGE1: 42.9435, ROUGE2: 20.1034, ROUGEL: 29.9581, GEN_LEN: 3615190.2</td><td>Tokens/s</td> <td>2160.12</td><td>Tokens/s</td> <td>2803.72</td><tr><td>llama2-70b-99.9</td><td>ROUGE1: 44.3868, ROUGE2: 22.0132, ROUGEL: 28.5876, TOKENS_PER_SAMPLE: 265.005</td><td>Tokens/s</td> <td>2619.09</td><td>Tokens/s</td> <td>3114.03</td><tr><td>stable-diffusion-xl</td><td>CLIP_SCORE: 31.6863, FID_SCORE: 23.0109</td><td>Queries/s</td> <td>1.84443</td><td>Samples/s</td> <td>2.08805</td></table>

