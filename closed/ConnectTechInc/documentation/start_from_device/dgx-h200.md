# DGX-H200 System Architecture

![Architecture Diagram](dgx_h200_diagram.png)

NVIDIA's [DGX-H200](https://www.nvidia.com/en-us/data-center/dgx-h200/) system supports the [GPUDirect](https://developer.nvidia.com/gpudirect) RDMA™ technology, which allows for direct I/O from PCIe devices (e.g. a Host Channel Adapter) to GPU device memory.  Each H200 GPU in the system is connected to an NVIDIA CX-7 Infiniband 400 NDR NIC through a PCIe Gen5x16 connection

Resnet50-Offline running on single DGX-H200, with INT8 input, requires to support 13GB/s for example. NVIDIA has
measured approximately 49 GB/s per GPU in our internal measurement of P2P transfers between the NIC and the GPUs.
