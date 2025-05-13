import os
import shutil

dataset = "caltech101"

path = 'aug/caltech101/sd2.1/gs2.0_nis50/shot1_seed{i}_template1_lr0.0001_ep200/train'

path_1 = path.format(i=1)
class_names = ['Faces', 'Faces_easy', 'Leopards', 'Motorbikes', 'accordion', 'airplanes', 'anchor', 'ant', 'barrel', 'bass', 'beaver', 'binocular', 'bonsai', 'brain', 'brontosaurus', 'buddha', 'butterfly', 'camera', 'cannon', 'car_side', 'ceiling_fan', 'cellphone', 'chair', 'chandelier', 'cougar_body', 'cougar_face', 'crab', 'crayfish', 'crocodile', 'crocodile_head', 'cup', 'dalmatian', 'dollar_bill', 'dolphin', 'dragonfly', 'electric_guitar', 'elephant', 'emu', 'euphonium', 'ewer', 'ferry', 'flamingo', 'flamingo_head', 'garfield', 'gerenuk', 'gramophone', 'grand_piano', 'hawksbill', 'headphone', 'hedgehog', 'helicopter', 'ibis', 'inline_skate', 'joshua_tree', 'kangaroo', 'ketch', 'lamp', 'laptop', 'llama', 'lobster', 'lotus', 'mandolin', 'mayfly', 'menorah', 'metronome', 'minaret', 'nautilus', 'octopus', 'okapi', 'pagoda', 'panda', 'pigeon', 'pizza', 'platypus', 'pyramid', 'revolver', 'rhino', 'rooster', 'saxophone', 'schooner', 'scissors', 'scorpion', 'sea_horse', 'snoopy', 'soccer_ball', 'stapler', 'starfish', 'stegosaurus', 'stop_sign', 'strawberry', 'sunflower', 'tick', 'trilobite', 'umbrella', 'watch', 'water_lilly', 'wheelchair', 'wild_cat', 'windsor_chair', 'wrench', 'yin_yang']

for i in range(3):
    path = path.format(i=i)
    
    for idx, class_name in enumerate(class_names):
        image_files = os.listdir(os.path.join(path, class_name))
        new_image_files = [f'aug-{idx}-{os.path.basename(image_file)}' for image_file in image_files if image_file.endswith('.png')]
        
        new_image_paths = [os.path.join('aa-datadream',f'caltech101-{i}-1', new_image_file) for new_image_file in new_image_files]
        image_paths = [os.path.join(path, class_name, image_file) for image_file in image_files]
        
        for image_path, new_image_path in zip(image_paths, new_image_paths):
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            shutil.copy(image_path, new_image_path)
            print(f"Copied {image_path} to {new_image_path}")