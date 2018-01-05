flow \
  --model cfg/binary-tiny-yolo-voc.cfg \
  --load  -1 \
  --annotation cvlab_dataset/Dog/ann/ \
  --dataset cvlab_dataset/Dog/img/ \
  --imgdir cvlab_dataset/Dog/img/ \
  --gpu 0.85 \
  --threshold 0.6 \
  --batch 20 \
  #--train \
  #--trainer adam \
