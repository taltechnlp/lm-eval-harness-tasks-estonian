#!/bin/bash
#SBATCH --partition=gpu    ### Partition
#SBATCH --job-name=speaker_paevakaja   ### Job Name           -J
#SBATCH --time=50:00:00       ### WallTime           -t
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4     ### Number of threads per task (OMP threads)
#SBATCH --mem=32G
#SBATCH --constraint=A100-80    ### Options: L40, A100-40, A100-80

source /gpfs/mariana/home/helenl/lm-evaluation-harness/venv4/bin/activate

lm_eval --model hf --model_args pretrained=tartuNLP/Llammas --tasks paevakaja_et_instr --batch_size 1 --log_samples --output_path results --verbosity DEBUG --trust_remote_code --system_instruction "Sa oled ekspert Eesti avaliku elu tegelaste alal. Sulle antakse uudiste- või vestlussaate automaatne transkriptsioon, koos kõneleja koodidega. Proovi arvata, millised isikud saates kõnelevad, nii reporterid kui ka intervjueeritavad. Väljasta tulemus JSONi abil. JSON formaadi näide: ["nimi1", "nimi2"].  Ära liialt riski, meile on täpsus olulisem kui saagis. Nimed võivad olla valesti transkribeeritud, kasuta oma taustateadmisi, et neid vajadusel korrigeerida. KINDLASTI ANNA VASTUSEKS AINULT ÜKS JSON LIST JA MITTE MIDAGI MUUD." --apply_chat_template 