
See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/GATEOverflow/inference_results_v4.1/blob/main/closed/Dell/results/XR8620_L4x1_TRT/summary.html)



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
    <p>Dell PowerEdge XR8620t (1x L4, TensorRT)    </p>
   </td>
  </tr>
 </table>
 <table class="datebar">
  <tbody>
   <tr>
    <th id="license_num"><a href="">MLPerf Inference Category:</a></th>
    <td id="license_num_val">edge</td>
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
            <tr><td><h3>Accelerator Details</h3><table><tr><td>accelerator_frequency</td><td></td></tr><tr><td>accelerator_host_interconnect</td><td>PCIe Gen5 x16</td></tr><tr><td>accelerator_interconnect</td><td>PCIe Gen5 x16</td></tr><tr><td>accelerator_interconnect_topology</td><td></td></tr><tr><td>accelerator_memory_capacity</td><td>24 GB</td></tr><tr><td>accelerator_memory_configuration</td><td>GDDR6</td></tr><tr><td>accelerator_model_name</td><td>NVIDIA L4</td></tr><tr><td>accelerator_on-chip_memories</td><td></td></tr><tr><td>accelerators_per_node</td><td>1</td></tr></table></td> <td><h3>Processor and Memory Details</h3><table><tr><td>host_memory_capacity</td><td>251GB</td></tr><tr><td>host_memory_configuration</td><td>8x 32GB DDR5</td></tr><tr><td>host_processor_caches</td><td></td></tr><tr><td>host_processor_core_count</td><td>32</td></tr><tr><td>host_processor_frequency</td><td></td></tr><tr><td>host_processor_interconnect</td><td></td></tr><tr><td>host_processor_model_name</td><td>Intel(R) Xeon(R) Gold 6433N</td></tr><tr><td>host_processors_per_node</td><td>1</td></tr></table></td> </tr>
            <tr><td ><h3>Other Hardware Details</h3><table><tr><td>cooling</td><td>air-cooled</td></tr><tr><td>disk_controllers</td><td></td></tr><tr><td>disk_drives</td><td></td></tr><tr><td>hw_notes</td><td></td></tr><tr><td>other_hardware</td><td></td></tr><tr><td>power_management</td><td></td></tr><tr><td>power_supply_details</td><td></td></tr><tr><td>power_supply_quantity_and_rating_watts</td><td></td></tr></table></td> <td><h3>Network and Interconnect Details</h3><table><tr><td>host_networking</td><td>Ethernet</td></tr><tr><td>host_networking_topology</td><td>N/A</td></tr><tr><td>host_network_card_count</td><td>4x 25GbE</td></tr><tr><td>network_speed_mbit</td><td></td></tr><tr><td>nics_enabled_connected</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>nics_enabled_os</td><td></td></tr><tr><td>number_of_type_nics_installed</td><td></td></tr></table></td> </tr>
            <tr><td colspan="2"><h3>Software Details</h3><table><tr><td>boot_firmware_version</td><td></td></tr><tr><td>framework</td><td>TensorRT 10.2.0, CUDA 12.4</td></tr><tr><td>management_firmware_version</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>operating_system</td><td>Ubuntu 22.04.3</td></tr><tr><td>other_software_stack</td><td>TensorRT 10.2.0, CUDA 12.4, cuDNN 8.9.7, Driver 550.54</td></tr><tr><td>sw_notes</td><td></td></tr></table></td> </tr>
            </table>

<h3>Results Table</h3>
<table>
    <tr>
        <th rowspan="2">Model</th>
        <th rowspan="2">Accuracy Target</th>
        <th colspan="2">Offline</th>
        <th colspan="2">SingleStream</th>
        <th colspan="2">MultiStream</th>
    </tr>
    <tr>
    <td>Metric</td>
    <td>Performance</td>
    <td>Metric</td>
    <td>Performance</td>
    <td>Metric</td>
    <td>Performance</td>
    </tr><tr><td>retinanet</td><td>mAP: 37.1745</td><td>Samples/s</td> <td>222.619</td><td>Latency (ms)</td> <td>4.830777</td><td>Latency (ms)</td> <td>42.019927</td></table>

