#!/bin/bash
#SBATCH --partition=gpu    ### Partition
#SBATCH --job-name=inflection_instr   ### Job Name           -J
#SBATCH --time=50:00:00       ### WallTime           -t
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=4     ### Number of threads per task (OMP threads)
#SBATCH --mem=32G
#SBATCH --constraint=A100-80    ### Options: L40, A100-40, A100-80

source /gpfs/mariana/home/helenl/lm-evaluation-harness/venv4/bin/activate

lm_eval --model hf --model_args pretrained=mistralai/Mixtral-8x7B-Instruct-v0.1,parallelize=True --tasks inflection_et_instr --batch_size auto --log_samples --output_path results --verbosity DEBUG --trust_remote_code --system_instruction "Sa oled eesti keele ekspert. Sulle antakse sõnapaar ainsuse nimetamas käändes ja sinu ülesandeks on käänata see etteantud käändesse. Jälgi, kas küsitud on käänet ainsuses või mitmuses ning vasta ainult käänatud sõnapaariga." --fewshot_as_multiturn --apply_chat_template --num_fewshot 5
