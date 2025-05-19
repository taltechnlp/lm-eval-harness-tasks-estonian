# Tasks
This repository contains lm-evaluation-harness task configurations for a set of Estonian language benchmarks.
## Using lm-evaluation-harness
### Installation
Install instruction for lm-evaluation-harness can be found [here](https://github.com/EleutherAI/lm-evaluation-harness).  
I would suggest using Python virtual environments so the modified install commands would be
```
python3 -m venv venv
source venv/bin/activate
git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
python -m pip install -e .
```
This will install the `lm_eval` package, that can be used as described in the following subsection.
### Usage
A basic version of a command that runs `tartuNLP/Llammas` on all instruction tuned tasks would be the following. This assumes that the current repo is in a folder called 'lm-eval-tasks' in your home directory. 
```
lm_eval --model hf --model_args pretrained=tartuNLP/Llammas,device=cuda:0 --tasks instr_tag_est --include_path ~/lm-eval-tasks
```
There is an analogous tag called `base_tag_est` that will run a model on all datasets using the configurations meant for base models.
### SLURM
Assuming that one wants to use some job scheduler, then the above command will have to be integrated into that job schedulers configuration file. Below is an example of a slurm configuration file that runs the above command.
```
#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --job-name=all_instr
#SBATCH --time=50:00:00
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=256G
#SBATCH --constraint=A100-40

source /home/username/nlp_project/venv/bin/activate
lm_eval --model hf --model_args pretrained=tartuNLP/Llammas,device=cuda:0 --tasks instr_tag_est --include_path ~/lm-eval-tasks
```
### Example command with extra options
A more complete command with some additional options is shown below
```
lm_eval --model hf --model_args pretrained=tartuNLP/Llammas-base,device=cuda:0 --tasks base_tag_est --include_path ~/lm-eval-tasks --batch_size 1 --log_samples --output_path results --verbosity DEBUG --trust_remote_code --limit 10
```
### GPUs required for various models
In the file called `models.txt` there names for various models along with extra parameters required by those models (for example for Gemma it is necessary to specify that it should use 16 bit floats) as well as suggested number and type of GPUs (V refers to A100-40GB and S refers to A100-80GB, so 2S would mean that it is suggested to use two A100-80GB GPUs). 
