
import os
from glob import glob

paths_38 = sorted(glob('aa-datadream/caltech-*-1/aug-*-0.png'))
paths_39 = sorted(glob('aa-datadream/caltech-*-1/aug-*-1.png'))
print(paths_38)

for path_38, path_39 in zip(paths_38, paths_39):
    print(path_38)
    print(path_39)
    # path_39를 path_38로 복사
    os.system(f'cp {path_39} {path_38}')