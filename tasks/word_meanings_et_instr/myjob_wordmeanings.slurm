#!/bin/bash
#SBATCH --partition=gpu    ### Partition
#SBATCH --job-name=word_meanings_instr   ### Job Name           -J
#SBATCH --time=50:00:00       ### WallTime           -t
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4     ### Number of threads per task (OMP threads)
#SBATCH --mem=32G
#SBATCH --constraint=A100-40    ### Options: L40, A100-40, A100-80

source /gpfs/mariana/home/helenl/lm-evaluation-harness/venv4/bin/activate

lm_eval --model hf --model_args pretrained=tartuNLP/Llammas --tasks word_meanings_et_instr --batch_size auto --log_samples --output_path results --verbosity DEBUG --trust_remote_code --system_instruction "Sa oled eesti sõnatähenduste ekspert. Sulle antakse ette sõna tähendus(ed) ja sinu ülesandeks on öelda, mis sõnale/sõnadele need kõige paremini vastavad. Õige vastus on enamasti üks sõna, kuid võib olla ka mitmesõnaline (näiteks Aafrika punane tee). Vasta ainult seletusele sobiva vastusega." --fewshot_as_multiturn --apply_chat_template --num_fewshot 5
