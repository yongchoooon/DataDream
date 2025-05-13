
GPU=0
N_SET_SPLIT=1
SPLIT_IDX=0


BS=10
NIPC=110
SD="sd2.1"
GS=2.0

N_SHOT=1
N_TEMPLATE=1

MODE="datadream"
DD_LR=1e-4
DD_EP=200

DATASET="$1"
IS_DATASETWISE=False
FEWSHOT_SEED="seed1"



# for DATASET in "${DATASETS[@]}"; do

CUDA_VISIBLE_DEVICES=$GPU python generate.py \
--bs=$BS \
--n_img_per_class=$NIPC \
--sd_version=$SD \
--mode=$MODE \
--guidance_scale=$GS \
--n_shot=$N_SHOT \
--n_template=$N_TEMPLATE \
--dataset=$DATASET \
--n_set_split=$N_SET_SPLIT \
--split_idx=$SPLIT_IDX \
--fewshot_seed=$FEWSHOT_SEED \
--datadream_lr=$DD_LR \
--datadream_epoch=$DD_EP \
--is_dataset_wise_model=$IS_DATASETWISE \

# done

