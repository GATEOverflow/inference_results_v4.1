
See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/GATEOverflow/inference_results_v4.1/blob/main/closed/HPE/results/HPE_ProLiant_DL380a_L40S_PCIe_48GBx4_TRT/summary.html)



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
    <p>HPE     </p>
    <p>HPE ProLiant DL380a Gen11 (4x L40S-PCIe-48GB, TensorRT)    </p>
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
    <td id="tester_val">HPE</td>
    <th id="sw_avail"><a href="">Availability:</a></th>
    <td id="sw_avail_val">Available  as of August 2024</td>
   </tr>
  </tbody>
 </table>
  
<table>
            <tr><td><h3>Accelerator Details</h3><table><tr><td>accelerator_frequency</td><td></td></tr><tr><td>accelerator_host_interconnect</td><td>PCIe Gen5 Switch</td></tr><tr><td>accelerator_interconnect</td><td>N/A</td></tr><tr><td>accelerator_interconnect_topology</td><td></td></tr><tr><td>accelerator_memory_capacity</td><td>48 GB</td></tr><tr><td>accelerator_memory_configuration</td><td>HBM2e</td></tr><tr><td>accelerator_model_name</td><td>NVIDIA L40S</td></tr><tr><td>accelerator_on-chip_memories</td><td></td></tr><tr><td>accelerators_per_node</td><td>4</td></tr></table></td> <td><h3>Processor and Memory Details</h3><table><tr><td>host_memory_capacity</td><td>1024GB</td></tr><tr><td>host_memory_configuration</td><td>16x 64GB 36ASF8G72PZ-3G2E1</td></tr><tr><td>host_processor_caches</td><td></td></tr><tr><td>host_processor_core_count</td><td>60</td></tr><tr><td>host_processor_frequency</td><td></td></tr><tr><td>host_processor_interconnect</td><td></td></tr><tr><td>host_processor_model_name</td><td>Intel(R) Xeon(R) Platinum 8580</td></tr><tr><td>host_processors_per_node</td><td>2</td></tr></table></td> </tr>
            <tr><td ><h3>Other Hardware Details</h3><table><tr><td>cooling</td><td>Air-cooled</td></tr><tr><td>disk_controllers</td><td></td></tr><tr><td>disk_drives</td><td></td></tr><tr><td>hw_notes</td><td></td></tr><tr><td>other_hardware</td><td></td></tr><tr><td>power_management</td><td></td></tr><tr><td>power_supply_details</td><td></td></tr><tr><td>power_supply_quantity_and_rating_watts</td><td></td></tr></table></td> <td><h3>Network and Interconnect Details</h3><table><tr><td>host_network_card_count</td><td>7-slots of 2-port 200G Infiniband (Max 2800GB HDR) or 2-port 100G Ethernet (Max 1400GbE)</td></tr><tr><td>host_networking</td><td>1Gbe</td></tr><tr><td>host_networking_topology</td><td>N/A</td></tr><tr><td>network_speed_mbit</td><td></td></tr><tr><td>nics_enabled_connected</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>nics_enabled_os</td><td></td></tr><tr><td>number_of_type_nics_installed</td><td></td></tr></table></td> </tr>
            <tr><td colspan="2"><h3>Software Details</h3><table><tr><td>boot_firmware_version</td><td></td></tr><tr><td>framework</td><td>TensorRT 9.0.0, CUDA 12.4</td></tr><tr><td>management_firmware_version</td><td></td></tr><tr><td>nics_enabled_firmware</td><td></td></tr><tr><td>operating_system</td><td>Ubuntu 22.04.3</td></tr><tr><td>other_software_stack</td><td>TensorRT 9.3.0, CUDA 12.4, Driver 535.183.01</td></tr><tr><td>sw_notes</td><td></td></tr></table></td> </tr>
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
    </tr><tr><td>resnet</td><td>acc: 75.6954</td><td>Queries/s</td> <td>176025.0</td><td>Samples/s</td> <td>172857.0</td><tr><td>retinanet</td><td>mAP: 37.1745</td><td>Queries/s</td> <td>3102.23</td><td>Samples/s</td> <td>3273.27</td><tr><td>bert-99</td><td>F1: 89.9653</td><td>Queries/s</td> <td>12904.6</td><td>Samples/s</td> <td>12981.8</td><tr><td>3d-unet-99</td><td>DICE: 0.8531</td><td colspan="2"> N/A </td><td>Samples/s</td> <td>15.4388</td></table>

