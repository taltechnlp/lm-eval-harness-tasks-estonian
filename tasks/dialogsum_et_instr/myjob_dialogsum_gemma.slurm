#!/bin/bash
#SBATCH --partition=gpu    ### Partition
#SBATCH --job-name=dialogsum   ### Job Name           -J
#SBATCH --time=50:00:00       ### WallTime           -t
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=4     ### Number of threads per task (OMP threads)
#SBATCH --mem=32G
#SBATCH --constraint=A100-40    ### Options: L40, A100-40, A100-80

source /gpfs/mariana/home/helenl/lm-evaluation-harness/venv4/bin/activate

lm_eval --model hf --model_args pretrained=google/gemma-2-27b-it,dtype=bfloat16,parallelize=True --tasks dialogsum_et_instr --batch_size auto --log_samples --output_path results --verbosity DEBUG --trust_remote_code --fewshot_as_multiturn --apply_chat_template --num_fewshot 5
