
GPU=0
SET_SPLIT=1 # GPU당 클래스를 몇개로 나눌 것인가
SPLIT_IDX=0

### ------------------
### Parameters
### ------------------
DATASET="$1"
N_CLS="$2"
FEWSHOT_SEED="seed1"
N_SHOT=1
NUM_TRAIN_EPOCH=200


### ------------------
### Calculate CLASS_IDXS 
### ------------------
START_RANGE=$(( (N_CLS / SET_SPLIT) * SPLIT_IDX))
END_RANGE=$(( (N_CLS / SET_SPLIT) * (SPLIT_IDX + 1) - 1 ))

# Check if SPLIT_IDX is equal to SET_SPLIT - 1
if [ $SPLIT_IDX -eq $((SET_SPLIT - 1)) ]; then
    FINAL_END_RANGE=$((N_CLS - 1))
else
    FINAL_END_RANGE=$END_RANGE
fi

CLASS_IDXS=($(seq $START_RANGE $FINAL_END_RANGE))


### ------------------
### Run
### ------------------
for CLASS_IDX in "${CLASS_IDXS[@]}"; do

CUDA_VISIBLE_DEVICES=$GPU, accelerate launch datadream.py \
--dataset=$DATASET \
--n_template=1 \
--fewshot_seed=$FEWSHOT_SEED \
--train_batch_size=8 \
--gradient_accumulation_steps=1 \
--learning_rate=1e-4 \
--lr_scheduler="cosine" \
--lr_warmup_steps=100 \
--num_train_epochs=$NUM_TRAIN_EPOCH \
--train_text_encoder=True \
--is_tqdm=True \
--output_dir=outputs \
--n_shot=$N_SHOT \
--target_class_idx=$CLASS_IDX \
--resume_from_checkpoint=None \
$PARAM

done
