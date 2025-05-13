import os
import shutil
import pandas as pd

# datasets = ['cub', 'caltech', 'flowers', 'pets', 'food', 'eurosat']
# dd_datasets = ['cub200', 'caltech101', 'flowers102', 'pets', 'food101', 'eurosat']
datasets = ['flowers']
dd_datasets = ['flowers102']

util_pets = [
        'Abyssinian', 'American Bulldog', 'American Pit Bull Terrier', 'Basset Hound', 'Beagle',
        'Bengal', 'Birman', 'Bombay', 'Boxer', 'British Shorthair',
        'Chihuahua', 'Egyptian Mau', 'English Cocker Spaniel', 'English Setter', 'German Shorthaired',
        'Great Pyrenees', 'Havanese', 'Japanese Chin', 'Keeshond', 'Leonberger',
        'Maine Coon', 'Miniature Pinscher', 'Newfoundland', 'Persian', 'Pomeranian',
        'Pug', 'Ragdoll', 'Russian Blue', 'Saint Bernard', 'Samoyed',
        'Scottish Terrier', 'Shiba Inu', 'Siamese', 'Sphynx', 'Staffordshire Bull Terrier',
        'Wheaten Terrier', 'Yorkshire Terrier'
    ]
util_pets_class_names = [cls_name.lower().replace(' ', '_') for cls_name in util_pets]

util_flowers = [
        'pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold',
        'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle',
        'snapdragon', "colt's foot", 'king protea', 'spear thistle', 'yellow iris',
        'globe-flower', 'purple coneflower', 'peruvian lily', 'balloon flower', 'giant white arum lily',
        'fire lily', 'pincushion flower', 'fritillary', 'red ginger', 'grape hyacinth',
        'corn poppy', 'prince of wales feathers', 'stemless gentian', 'artichoke', 'sweet william',
        'carnation', 'garden phlox', 'love in the mist', 'mexican aster', 'alpine sea holly',
        'ruby-lipped cattleya', 'cape flower', 'great masterwort', 'siam tulip', 'lenten rose',
        'barbeton daisy', 'daffodil', 'sword lily', 'poinsettia', 'bolero deep blue',
        'wallflower', 'marigold', 'buttercup', 'oxeye daisy', 'common dandelion',
        'petunia', 'wild pansy', 'primula', 'sunflower', 'pelargonium',
        'bishop of llandaff', 'gaura', 'geranium', 'orange dahlia', 'pink-yellow dahlia',
        'cautleya spicata', 'japanese anemone', 'black-eyed susan', 'silverbush', 'californian poppy',
        'osteospermum', 'spring crocus', 'bearded iris', 'windflower', 'tree poppy',
        'gazania', 'azalea', 'water lily', 'rose', 'thorn apple',
        'morning glory', 'passion flower', 'lotus', 'toad lily', 'anthurium',
        'frangipani', 'clematis', 'hibiscus', 'columbine', 'desert-rose',
        'tree mallow', 'magnolia', 'cyclamen', 'watercress', 'canna lily',
        'hippeastrum', 'bee balm', 'ball moss', 'foxglove', 'bougainvillea',
        'camellia', 'mallow', 'mexican petunia', 'bromelia', 'blanket flower',
        'trumpet creeper', 'blackberry lily'
    ]

aug_dir = "/home/jinwon/workspace/temp-dalda2/aug/aa-cabin-all-lambda-rn50"

for idx, dataset in enumerate(datasets):
    for i in range(3):
        csv_path = os.path.join(aug_dir, f"{dataset}-{i}-1", f"source_image_prompt.csv")
        df = pd.read_csv(csv_path)
        unique_image_files = list(df['source_image_path'].unique())
        # if dataset == 'cub':
        #     class_names = [image.split('/')[2].split('.')[-1].replace('_', ' ') for image in unique_image_files]
        #     for class_idx, class_name in enumerate(class_names):
        #         class_dir = os.path.join('data', dd_datasets[idx], 'real_train_fewshot', f"seed{i}", class_name)
        #         os.makedirs(class_dir, exist_ok=True)
        #         shutil.copy('/home/jinwon/workspace/temp-dalda2/' + unique_image_files[class_idx], class_dir)
        
        # if dataset == 'caltech':
        #     class_names = [image.split('/')[2] for image in unique_image_files]
        #     for class_idx, class_name in enumerate(class_names):
        #         class_dir = os.path.join('data', dd_datasets[idx], 'real_train_fewshot', f"seed{i}", class_name)
        #         os.makedirs(class_dir, exist_ok=True)
        #         shutil.copy('/home/jinwon/workspace/temp-dalda2/' + unique_image_files[class_idx], class_dir)

        # if dataset == 'pets':
        #     class_names = util_pets_class_names
        #     print(class_names)
        #     for class_idx, class_name in enumerate(class_names):
        #         class_dir = os.path.join('data', dd_datasets[idx], 'real_train_fewshot', f"seed{i}", util_pets[class_idx])
        #         os.makedirs(class_dir, exist_ok=True)
        #         shutil.copy('/home/jinwon/workspace/temp-dalda2/' + unique_image_files[class_idx], class_dir)

        # if dataset == 'food':
        #     class_names = [image.split('/')[2] for image in unique_image_files]
        #     for class_idx, class_name in enumerate(class_names):
        #         class_dir = os.path.join('data', dd_datasets[idx], 'real_train_fewshot', f"seed{i}", class_name)
        #         os.makedirs(class_dir, exist_ok=True)
        #         shutil.copy('/home/jinwon/workspace/temp-dalda2/' + unique_image_files[class_idx], class_dir)

        if dataset == 'flowers':
            class_names = util_flowers
            print(class_names)
            for class_idx, class_name in enumerate(class_names):
                class_dir = os.path.join('data', dd_datasets[idx], 'real_train_fewshot', f"seed{i}", util_flowers[class_idx])
                os.makedirs(class_dir, exist_ok=True)
                shutil.copy('/home/jinwon/workspace/temp-dalda2/' + unique_image_files[class_idx], class_dir)
