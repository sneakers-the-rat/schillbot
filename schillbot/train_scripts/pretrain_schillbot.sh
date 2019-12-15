t2t-trainer \
 --generate_data \
 --problem=languagemodel_en_wiki32k \
 --t2t_usr_dir=/home/lab/jonny/schillbot \
 --data_dir=/mnt/data/schillbot_pt \
 --tmp_dir=/mnt/data/jonny/schillbot_pt \
 --train_dir=/mnt/data/schillbot_pt/checkpoints \
 --output_dir=/mnt/data/schillbot_pt/checkpoints \
 --checkpoint_dir=/mnt/data/schillbot_pt/checkpoints \
 --model=transformer \
 --hparams_set=transformer_schill \
 --train_steps=20000000


