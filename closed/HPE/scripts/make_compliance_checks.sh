########## Run compliance on all models #############
cd /work #container's home dir
SUBMITTER="HPE"
export SUBMITTER=$SUBMITTER

#Setup for audit
make stage_results SUBMITTER=$SUBMITTER 

##Run audit checks
make run_audit_harness SUBMITTER=$SUBMITTER 
## Legacy NVIDIA container
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=resnet50 --scenarios=offline,server"
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=retinanet --scenarios=offline,server" 
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=rnnt --scenarios=offline,server"
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=3d-unet --scenarios=offline --config_ver=default,high_accuracy" 
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=bert --scenarios=offline,server --config_ver=default,high_accuracy"
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=dlrm-v2 --scenarios=offline,server --config_ver=default,high_accuracy"

## New NVIDIA container
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=gptj --scenarios=offline,server --config_ver=default,high_accuracy"
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=stable-diffusion-xl --scenarios=offline,server"
#make run_audit_harness SUBMITTER=$SUBMITTER RUN_ARGS="--benchmarks=llama2-70b --scenarios=offline,server --config_ver=default,high_accuracy"

#once all above pass, run this:
make stage_compliance SUBMITTER=$SUBMITTER
