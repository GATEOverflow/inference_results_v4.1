
See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/GATEOverflow/inference_results_v4.1/blob/main/closed/Supermicro/results/1-node-2S-EMR-PyTorch/summary.html)



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
    <p>supermicro     </p>
    <p>1-node-2S-EMR-PyTorch    </p>
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
    <td id="tester_val">supermicro</td>
    <th id="sw_avail"><a href="">Availability:</a></th>
    <td id="sw_avail_val">Available  as of August 2024</td>
   </tr>
  </tbody>
 </table>
  
<table>
            <tr><td><h3>Accelerator Details</h3><table><tr><td>accelerators_per_node</td><td>0</td></tr><tr><td>accelerator_model_name</td><td>N/A</td></tr><tr><td>accelerator_frequency</td><td>N/A</td></tr><tr><td>accelerator_host_interconnect</td><td>N/A</td></tr><tr><td>accelerator_interconnect</td><td>N/A</td></tr><tr><td>accelerator_interconnect_topology</td><td>N/A</td></tr><tr><td>accelerator_memory_capacity</td><td>N/A</td></tr><tr><td>accelerator_memory_configuration</td><td>N/A</td></tr><tr><td>accelerator_on-chip_memories</td><td>N/A</td></tr></table></td> <td><h3>Processor and Memory Details</h3><table><tr><td>host_processor_model_name</td><td>INTEL(R) XEON(R) PLATINUM 8592+</td></tr><tr><td>host_processors_per_node</td><td>2</td></tr><tr><td>host_processor_core_count</td><td>64</td></tr><tr><td>host_processor_frequency</td><td>N/A</td></tr><tr><td>host_processor_caches</td><td>N/A</td></tr><tr><td>host_memory_configuration</td><td>8 slots / 64GB each / per socket</td></tr><tr><td>host_memory_capacity</td><td>1024GB</td></tr><tr><td>host_processor_interconnect</td><td>N/A</td></tr></table></td> </tr>
            <tr><td ><h3>Other Hardware Details</h3><table><tr><td>cooling</td><td>Air</td></tr><tr><td>hw_notes</td><td>QuantaGrid D54Q-2U</td></tr></table></td> <td><h3>Network and Interconnect Details</h3><table><tr><td>host_networking</td><td>Ethernet Controller / 10GBASE-T</td></tr><tr><td>host_networking_topology</td><td>N/A</td></tr><tr><td>host_network_card_count</td><td>2</td></tr></table></td> </tr>
            <tr><td colspan="2"><h3>Software Details</h3><table><tr><td>framework</td><td>PyTorch</td></tr><tr><td>operating_system</td><td>Rocky Linux 8.10</td></tr><tr><td>other_software_stack</td><td>5.14.0-427.24.1.el9_4.x86_64</td></tr><tr><td>sw_notes</td><td>N/A</td></tr></table></td> </tr>
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
    </tr><tr><td>resnet</td><td>acc: 75.6954</td><td>Queries/s</td> <td>21001.6</td><td>Samples/s</td> <td>23674.2</td><tr><td>bert-99</td><td>F1: 89.9653</td><td>Queries/s</td> <td>1256.61</td><td>Samples/s</td> <td>1595.13</td></table>

