import os
import shutil

dataset = "eurosat"

path = 'aug/eurosat/sd2.1/gs2.0_nis50/shot1_seed{i}_template1_lr0.0001_ep200/train'

path_1 = path.format(i=1)
class_names = [
        'AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
        'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake'
    ]

for i in range(3):
    _path = path.format(i=i)
    
    for idx, class_name in enumerate(class_names):
        image_files = os.listdir(os.path.join(_path, class_name))
        new_image_files = [f'aug-{idx}-{os.path.basename(image_file)}' for image_file in image_files if image_file.endswith('.png')]
        
        new_image_paths = [os.path.join('aa-datadream',f'eurosat-{i}-1', new_image_file) for new_image_file in new_image_files]
        image_paths = [os.path.join(_path, class_name, image_file) for image_file in image_files]
        
        for image_path, new_image_path in zip(image_paths, new_image_paths):
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            shutil.copy(image_path, new_image_path)
            print(f"Copied {image_path} to {new_image_path}")