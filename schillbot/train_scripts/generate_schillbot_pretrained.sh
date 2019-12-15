t2t-decoder \
 --problem=languagemodel_en_wiki32k \
 --data_dir=/mnt/data/schillbot_pt \
 --t2t_usr_dir=/home/lab/jonny/schillbot \
 --tmp_dir=/mnt/data/schillbot_pt \
 --train_dir=/mnt/data/schillbot_pt/checkpoints \
 --output_dir=/mnt/data/schillbot_pt/checkpoints \
 --model=transformer \
 --hparams_set=transformer_schill \
 --hparams="sampling_method=random,sampling_temp=0.7" \
 --decode_hparams="beam_size=1,alpha=0.6,num_decodes=1" \
 --decode_from_file=/mnt/data/schillbot_pt/decode.txt \
 --decode_to_file=/mnt/data/schillbot_pt/decode_out.txt

