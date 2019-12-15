t2t-decoder \
 --problem=schill_subwords_mp \
 --data_dir=/mnt/data/schillbot_pt \
 --t2t_usr_dir=/home/lab/jonny/schillbot \
 --tmp_dir=/mnt/data/schillbot_mp \
 --train_dir=/mnt/data/schillbot_mp/checkpoints \
 --output_dir=/mnt/data/schillbot_mp/checkpoints \
 --model=transformer \
 --hparams_set=transformer_schill_mp \
 --hparams="sampling_method=random,sampling_temp=0.95" \
 --decode_hparams="beam_size=1,alpha=0.6,num_decodes=10,multiproblem_task_id=31983" \
 --decode_from_file=/mnt/data/schillbot_pt/decode_full.txt \
 --decode_to_file=/mnt/data/schillbot_mp/decode_200000_95_1_full_x10.txt
