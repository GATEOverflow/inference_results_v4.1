# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
sys.path.insert(0, os.getcwd())

from code.common.constants import Benchmark, Scenario
from code.common.systems.system_list import KnownSystem
from configs.configuration import *
from configs.gptj import GPUBaseConfig


class ServerGPUBaseConfig(GPUBaseConfig):
    scenario = Scenario.Server
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    tensor_parallelism = 1
    precision = "fp16"
    enable_sort = False
    num_sort_segments = 2


class H200_SXM_141GBx1(ServerGPUBaseConfig):
    gpu_batch_size = {'gptj': 396}
    use_fp8 = True
    server_target_qps = 34.92


class H200_SXM_141GBx1_HighAccuracy(H200_SXM_141GBx1):
    pass


class H200_SXM_141GBx8(H200_SXM_141GBx1):
    server_target_qps = 34.92 * 8


class H200_SXM_141GBx8_HighAccuracy(H200_SXM_141GBx8):
    pass


class GH200_96GB_aarch64x1(ServerGPUBaseConfig):
    gpu_batch_size = {'gptj': 196}
    use_fp8 = True
    server_target_qps = 31.3


class GH200_96GB_aarch64x1_HighAccuracy(GH200_96GB_aarch64x1):
    pass


class H100_SXM_80GBx1(ServerGPUBaseConfig):
    gpu_batch_size = {'gptj': 256}
    use_fp8 = True
    server_target_qps = 34.92


class H100_SXM_80GBx8(H100_SXM_80GBx1):
    server_target_qps = 34.92 * 8


class H100_SXM_80GBx8_MaxQ(H100_SXM_80GBx8):
    server_target_qps = 150
    power_limit = 350


class H100_SXM_80GBx1_HighAccuracy(H100_SXM_80GBx1):
    pass


class H100_SXM_80GBx8_HighAccuracy(H100_SXM_80GBx8):
    pass


class H100_SXM_80GBx8_HighAccuracy_MaxQ(H100_SXM_80GBx8_HighAccuracy):
    server_target_qps = 150
    power_limit = 350


class H100_PCIe_80GBx1(ServerGPUBaseConfig):
    gpu_batch_size = {'gptj': 128}
    use_fp8 = True
    server_target_qps = 15.1


class H100_PCIe_80GBx8(H100_PCIe_80GBx1):
    gpu_batch_size = {'gptj': 128}
    server_target_qps = 116


class H100_PCIe_80GBx8_MaxQ(H100_PCIe_80GBx8):
    server_target_qps = 40
    power_limit = 200


class H100_PCIe_80GBx1_HighAccuracy(H100_PCIe_80GBx1):
    precision = "fp16"


class H100_PCIe_80GBx8_HighAccuracy(H100_PCIe_80GBx8):
    precision = "fp16"


class H100_PCIe_80GBx8_HighAccuracy_MaxQ(H100_PCIe_80GBx8_HighAccuracy):
    server_target_qps = 40
    power_limit = 200


class L4x1(ServerGPUBaseConfig):
    gpu_batch_size = {'gptj': 7}
    use_fp8 = True
    server_target_qps = 0.88


class L4x1_HighAccuracy(L4x1):
    pass


class L40Sx1(ServerGPUBaseConfig):
    gpu_batch_size = {'gptj': 128}
    use_fp8 = True
    server_target_qps = 12


class L40Sx1_HighAccuracy(L40Sx1):
    pass


class L40Sx8(L40Sx1):
    server_target_qps = 96


class L40Sx8_HighAccuracy(L40Sx8):
    pass