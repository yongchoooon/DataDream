import os
import shutil

dataset = "pets"

path = 'aug/pets/sd2.1/gs2.0_nis50/shot1_seed{i}_template1_lr0.0001_ep200/train'

path_1 = path.format(i=1)
class_names = ['Abyssinian', 'American Bulldog', 'American Pit Bull Terrier', 'Basset Hound', 'Beagle',
             'Bengal', 'Birman', 'Bombay', 'Boxer', 'British Shorthair',
             'Chihuahua', 'Egyptian Mau', 'English Cocker Spaniel', 'English Setter', 'German Shorthaired',
             'Great Pyrenees', 'Havanese', 'Japanese Chin', 'Keeshond', 'Leonberger',
             'Maine Coon', 'Miniature Pinscher', 'Newfoundland', 'Persian', 'Pomeranian',
             'Pug', 'Ragdoll', 'Russian Blue', 'Saint Bernard', 'Samoyed',
             'Scottish Terrier', 'Shiba Inu', 'Siamese', 'Sphynx', 'Staffordshire Bull Terrier',
             'Wheaten Terrier', 'Yorkshire Terrier']

for i in range(3):
    _path = path.format(i=i)
    
    for idx, class_name in enumerate(class_names):
        image_files = os.listdir(os.path.join(_path, class_name))
        image_files = [image_file for image_file in image_files if image_file.endswith('.png')]
        new_image_files = [f'aug-{idx}-{os.path.basename(image_file)}' for image_file in image_files if image_file.endswith('.png')]
        
        new_image_paths = [os.path.join('aa-datadream',f'pets-{i}-1', new_image_file) for new_image_file in new_image_files]
        image_paths = [os.path.join(_path, class_name, image_file) for image_file in image_files]
        
        for image_path, new_image_path in zip(image_paths, new_image_paths):
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            shutil.copy(image_path, new_image_path)
            print(f"Copied {image_path} to {new_image_path}")