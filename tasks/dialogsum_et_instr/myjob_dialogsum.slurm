#!/bin/bash
#SBATCH --partition=gpu    ### Partition
#SBATCH --job-name=dialogsum   ### Job Name           -J
#SBATCH --time=50:00:00       ### WallTime           -t
#SBATCH --gres=gpu:3
#SBATCH --cpus-per-task=4     ### Number of threads per task (OMP threads)
#SBATCH --mem=32G
#SBATCH --constraint=A100-80    ### Options: L40, A100-40, A100-80

source /gpfs/mariana/home/helenl/lm-evaluation-harness/venv4/bin/activate

lm_eval --model hf --model_args pretrained=Qwen/Qwen2-72B-Instruct,parallelize=True --tasks dialogsum_et_instr --batch_size 4 --log_samples --output_path results --verbosity DEBUG --trust_remote_code --system_instruction "Sa oled tehisintellekti ekspert eesti keele alal. Su ülesanne on analüüsida dialooge ja genereerida ühe või kahe lausega lühike kokkuvõte, mis kirjeldab dialoogi sisu. Ära unusta alati vastata eesti keeles. Vasta ainult kokkuvõttega!" --fewshot_as_multiturn --apply_chat_template --num_fewshot 5