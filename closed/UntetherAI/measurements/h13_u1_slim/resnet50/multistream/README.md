
# MLPerf Inference v4.0 - closed - Untether

To run experiments individually, use the following commands.

## h13_u1_slim - resnet50 - multistream

### Accuracy  

```
axs byquery loadgen_output,framework=kilt,task=image_classification,sut_name=h13_u1_slim,device=uai,loadgen_mode=AccuracyOnly,loadgen_scenario=MultiStream,collection=results_h13_u1_slim
```

### Performance 

```
axs byquery loadgen_output,framework=kilt,task=image_classification,sut_name=h13_u1_slim,device=uai,loadgen_mode=PerformanceOnly,loadgen_compliance_test-,loadgen_scenario=MultiStream,collection=results_h13_u1_slim,loadgen_target_latency=0.3
```

### Compliance TEST01

```
axs byquery loadgen_output,framework=kilt,task=image_classification,sut_name=h13_u1_slim,device=uai,loadgen_mode=PerformanceOnly,loadgen_compliance_test=TEST01,loadgen_scenario=MultiStream,collection=results_h13_u1_slim,loadgen_target_latency=0.3
```

### Compliance TEST04

```
axs byquery loadgen_output,framework=kilt,task=image_classification,sut_name=h13_u1_slim,device=uai,loadgen_mode=PerformanceOnly,loadgen_compliance_test=TEST04,loadgen_scenario=MultiStream,collection=results_h13_u1_slim,loadgen_target_latency=0.3
```

### Compliance TEST05

```
axs byquery loadgen_output,framework=kilt,task=image_classification,sut_name=h13_u1_slim,device=uai,loadgen_mode=PerformanceOnly,loadgen_compliance_test=TEST05,loadgen_scenario=MultiStream,collection=results_h13_u1_slim,loadgen_target_latency=0.3
```
