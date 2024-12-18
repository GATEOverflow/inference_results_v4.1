# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    gpu_batch_size = {'mixtral-8x7b': 512}
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 10 * 4
    enable_sort = False
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    tensor_parallelism = 2 #NVIDIA README says TP=2 for 40GB and lower  GPU memory
    pipeline_parallelism = 1
    kvcache_free_gpu_mem_frac = 0.90
    #min_duration = 2400000

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    gpu_batch_size = {'mixtral-8x7b': 896}
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 15 * 4
    enable_sort = False
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    tensor_parallelism = 1  #NVIDIA README says TP=1 for 80GB and higher GPU memory
    pipeline_parallelism = 1
    kvcache_free_gpu_mem_frac = 0.90
    #min_duration = 2400000

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP) #
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    gpu_batch_size = {'mixtral-8x7b': 896}
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 15 * 4
    enable_sort = False
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    tensor_parallelism = 1 #NVIDIA README says TP=1 for 80GB and higher GPU memory
    pipeline_parallelism = 1
    kvcache_free_gpu_mem_frac = 0.90
    #min_duration = 2400000

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GBx8):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    gpu_batch_size = {'mixtral-8x7b': 1024}
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 48 * 8    
    enable_sort = False
    max_num_tokens = 8192
    vboost_slider = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    tensor_parallelism = 1  #NVIDIA README says TP=1 for 80GB and higher GPU memory
    pipeline_parallelism = 1
    kvcache_free_gpu_mem_frac = 0.90
    min_duration = 2400000
