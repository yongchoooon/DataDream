import os
import shutil

dataset = "food101"

path = 'aug/food101/sd2.1/gs2.0_nis50/shot1_seed{i}_template1_lr0.0001_ep200/train'

path_1 = path.format(i=1)
class_names = ['apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare',
                'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito',
                'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake',
                'ceviche', 'cheese_plate', 'cheesecake', 'chicken_curry', 'chicken_quesadilla',
                'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder',
                'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes',
                'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict',
                'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras',
                'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice',
                'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich',
                'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup',
                'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna',
                'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup',
                'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters',
                'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck',
                'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib',
                'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto',
                'samosa', 'sashimi', 'scallops', 'seaweed_salad', 'shrimp_and_grits',
                'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake',
                'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare',
                'waffles']

for i in range(3):
    path = path.format(i=i)
    
    for idx, class_name in enumerate(class_names):
        image_files = os.listdir(os.path.join(path, class_name))
        new_image_files = [f'aug-{idx}-{os.path.basename(image_file)}' for image_file in image_files if image_file.endswith('.png')]
        
        new_image_paths = [os.path.join('aa-datadream',f'food101-{i}-1', new_image_file) for new_image_file in new_image_files]
        image_paths = [os.path.join(path, class_name, image_file) for image_file in image_files]
        
        for image_path, new_image_path in zip(image_paths, new_image_paths):
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            shutil.copy(image_path, new_image_path)
            print(f"Copied {image_path} to {new_image_path}")