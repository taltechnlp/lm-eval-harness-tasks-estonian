#!/bin/bash
#SBATCH --partition=gpu    ### Partition
#SBATCH --job-name=grammar2_instr   ### Job Name           -J
#SBATCH --time=50:00:00       ### WallTime           -t
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=4     ### Number of threads per task (OMP threads)
#SBATCH --mem=32G
#SBATCH --constraint=A100-80    ### Options: L40, A100-40, A100-80

source /gpfs/mariana/home/helenl/lm-evaluation-harness/venv4/bin/activate

lm_eval --model hf --model_args pretrained=meta-llama/Llama-3.1-70B-Instruct,parallelize=True --tasks grammar_et_instr --batch_size auto --log_samples --output_path results --verbosity DEBUG --trust_remote_code --system_instruction "Sa oled eesti keele ekspert. Sulle antakse ette eestikeelsed laused, kus võivad esineda grammatikavead. Tagasta korrektne lause, kus vead on parandatud. Juhul kui etteantud lause on juba õige, siis tagastagi see sama lause. Vasta ainult lausega" --fewshot_as_multiturn --apply_chat_template --num_fewshot 5
