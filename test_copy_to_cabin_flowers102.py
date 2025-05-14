import os
import shutil

dataset = "flowers102"

path = 'aug/flowers102/sd2.1/gs2.0_nis50/shot1_seed{i}_template1_lr0.0001_ep200/train'

path_1 = path.format(i=1)
class_names = ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold',
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
                   'trumpet creeper', 'blackberry lily']

for i in range(3):
    _path = path.format(i=i)
    
    for idx, class_name in enumerate(class_names):
        image_files = os.listdir(os.path.join(_path, class_name))
        new_image_files = [f'aug-{idx}-{os.path.basename(image_file)}' for image_file in image_files if image_file.endswith('.png')]
        
        new_image_paths = [os.path.join('aa-datadream',f'flowers-{i}-1', new_image_file) for new_image_file in new_image_files]
        image_paths = [os.path.join(_path, class_name, image_file) for image_file in image_files]
        
        for image_path, new_image_path in zip(image_paths, new_image_paths):
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            shutil.copy(image_path, new_image_path)
            print(f"Copied {image_path} to {new_image_path}")