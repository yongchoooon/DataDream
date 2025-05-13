import os
from glob import glob
from PIL import Image

path_ = '/home/jinwon/workspace/DataDream/aug/pets/sd2.1/gs2.0_nis50/shot1_seed0_template1_lr0.0001_ep200/train'

success_count = 0
error_count = 0

for i, class_dir in enumerate(os.listdir(path_)):
    class_path = os.path.join(path_, class_dir)
    image_paths = glob(os.path.join(class_path, '*.png'))
    print(len(image_paths))
    for image_path in image_paths:
        try:
            with Image.open(image_path) as img:
                img.verify()   # 파일이 손상되었는지 검사
            success_count += 1
        except Exception as e:
            print(f"[ERROR] {image_path}: {e}")
            error_count += 1

print(f"Checked {success_count + error_count} images → Success: {success_count}, Errors: {error_count}")