
See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/mlcommons/mlperf_inference_test_submissions_v5.0/blob/main/closed/ASUSTeK/results/ESC_N8_E11_H100x8_TRT/summary.html)



<div class="resultpage">
 <div class="titlebarcontainer">
  <div class="logo">
   <a href="/" style="border: none"><img src="" alt="" /></a>
  </div>
  <div class="titlebar">
   <h1 class="title">MLPerf Inference v5.0</h1>
   <p style="font-size: smaller">Copyright 2019-2025 MLCommons</p>
  </div>
 </div>
 <table class="titlebarcontainer">
  <tr>
   <td class="headerbar" rowspan="2">
    <p>ASUSTeK     </p>
    <p>ESC-N8-E11 (8x H100-SXM-80GB, TensorRT)    </p>
   </td>
  </tr>
 </table>
 <table class="datebar">
  <tbody>
   <tr>
    <th id="license_num"><a href="">MLPerf Inference Category:</a></th>
    <td id="license_num_val">Datacenter</td>
    <th id="test_date"><a href="">MLPerf Inference Division:</a></th>
    <td id="test_date_val">Closed</td>
   </tr>
   <tr>
    <th id="tester"><a href="">Submitted by:</a></th>
    <td id="tester_val">ASUSTeK</td>
    <th id="sw_avail"><a href="">Availability:</a></th>
    <td id="sw_avail_val">Available as of Feb 2025</td>
   </tr>
  </tbody>
 </table>
  
<table>
            <tr><td><h3>Accelerator Details</h3><table><tr><td>accelerator_frequency</td><td></td></tr><tr><td>accelerator_host_interconnect</td><td>PCIe Gen5 x16</td></tr><tr><td>accelerator_interconnect</td><td>18x 4th Gen NVLink, 900GB/s</td></tr><tr><td>accelerator_interconnect_topology</td><td></td></tr><tr><td>accelerator_memory_capacity</td><td>80 GB</td></tr><tr><td>accelerator_memory_configuration</td><td>HBM3</td></tr><tr><td>accelerator_model_name</td><td>NVIDIA H100-SXM-80GB</td></tr><tr><td>accelerator_on-chip_memories</td><td></td></tr><tr><td>accelerators_per_node</td><td>8</td></tr></table></td> <td><h3>Processor and Memory Details</h3><table><tr><td>host_memory_capacity</td><td>1.5 TB</td></tr><tr><td>host_memory_configuration</td><td>16x 96GB M321RYGA0PB2-CCPPC</td></tr><tr><td>host_processor_caches</td><td></td></tr><tr><td>host_processor_core_count</td><td>64</td></tr><tr><td>host_processor_frequency</td><td></td></tr><tr><td>host_processor_interconnect</td><td></td></tr><tr><td>host_processor_model_name</td><td>INTEL(R) XEON(R) PLATINUM 8592+</td></tr><tr><td>host_processors_per_node</td><td>2</td></tr></table></td> </tr>
            <tr><td ><h3>Other Hardware Details</h3><table><tr><td>cooling</td><td>Air-cooled</td></tr><tr><td>disk_controllers</td><td>NVMe</td></tr><tr><td>disk_drives</td><td>NVMe SSD</td></tr><tr><td>hw_notes</td><td></td></tr><tr><td>other_hardware</td><td></td></tr><tr><td>power_management</td><td></td></tr><tr><td>power_supply_details</td><td></td></tr><tr><td>power_supply_quantity_and_rating_watts</td><td></td></tr></table></td> <td><h3>Network and Interconnect Details</h3><table><tr><td>host_network_card_count</td><td>10x MT2910 Family [ConnectX-7]</td></tr><tr><td>host_networking</td><td>Infiniband</td></tr><tr><td>host_networking_topology</td><td>N/A</td></tr><tr><td>network_speed_mbit</td><td></td></tr><tr><td>nics_enabled_connected</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>nics_enabled_os</td><td></td></tr><tr><td>number_of_type_nics_installed</td><td></td></tr></table></td> </tr>
            <tr><td colspan="2"><h3>Software Details</h3><table><tr><td>boot_firmware_version</td><td></td></tr><tr><td>framework</td><td>TensorRT 10.2.0, CUDA 12.4</td></tr><tr><td>management_firmware_version</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>operating_system</td><td>Ubuntu 22.04.3</td></tr><tr><td>other_software_stack</td><td>TensorRT 10.2.0, CUDA 12.4, cuDNN 8.9.7, Driver 550.90.07</td></tr><tr><td>sw_notes</td><td></td></tr></table></td> </tr>
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
    </tr>
    <tr><td>llama2-70b-99</td><td>ROUGE1: 43.9869, ROUGE2: 21.8148, ROUGEL: 28.33, TOKENS_PER_SAMPLE: 265.005</td><td>Tokens/s</td> <td>20605.3</td><td>Tokens/s</td> <td>24323.6</td><tr><td>llama2-70b-99.9</td><td>ROUGE1: 44.3868, ROUGE2: 22.0132, ROUGEL: 28.5876, TOKENS_PER_SAMPLE: 265.005</td><td>Tokens/s</td> <td>20605.3</td><td>Tokens/s</td> <td>24323.6</td><tr><td>gptj-99</td><td>ROUGE1: 42.5566, ROUGE2: 19.9223, ROUGEL: 29.6882, GEN_LEN: 3615190.2</td><td>Tokens/s</td> <td>19226.9</td><td>Tokens/s</td> <td>19877.6</td><tr><td>gptj-99.9</td><td>ROUGE1: 42.9435, ROUGE2: 20.1034, ROUGEL: 29.9581, GEN_LEN: 3615190.2</td><td>Tokens/s</td> <td>19226.9</td><td>Tokens/s</td> <td>19877.6</td><tr><td>bert-99</td><td>F1: 89.9653</td><td>Queries/s</td> <td>57005.2</td><td>Samples/s</td> <td>70661.2</td><tr><td>bert-99.9</td><td>F1: 90.7831</td><td>Queries/s</td> <td>51213.8</td><td>Samples/s</td> <td>62371.4</td><tr><td>stable-diffusion-xl</td><td>CLIP_SCORE: 31.6863, FID_SCORE: 23.0109</td><td>Queries/s</td> <td>15.7041</td><td>Samples/s</td> <td>16.4176</td><tr><td>dlrm-v2-99</td><td>AUC: 79.5069</td><td>Queries/s</td> <td>516159.0</td><td>Samples/s</td> <td>591476.0</td><tr><td>dlrm-v2-99.9</td><td>AUC: 80.2297</td><td>Queries/s</td> <td>330066.0</td><td>Samples/s</td> <td>363048.0</td><tr><td>retinanet</td><td>mAP: 37.1745</td><td>Queries/s</td> <td>13763.0</td><td>Samples/s</td> <td>14432.8</td><tr><td>resnet</td><td>acc: 75.6954</td><td>Queries/s</td> <td>630229.0</td><td>Samples/s</td> <td>709920.0</td><tr><td>3d-unet-99</td><td>DICE: 0.8531</td><td></td><td></td><td>Samples/s</td> <td>51.6944</td><tr><td>3d-unet-99.9</td><td>DICE: 0.8608</td><td></td><td></td><td>Samples/s</td> <td>51.6944</td></table>
