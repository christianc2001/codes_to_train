import glob
from pathlib import Path
import os

# Define paths to image folders
image_path = '/content/images/all'
train_path = '/content/images/train'
val_path = '/content/images/validation'
test_path = '/content/images/test'

# Get list of all images
jpg_file_list = [path for path in Path(image_path).rglob('*.jpg')]
jpeg_file_list = [path for path in Path(image_path).rglob('*.jpeg')]
JPG_file_list = [path for path in Path(image_path).rglob('*.JPG')]
png_file_list = [path for path in Path(image_path).rglob('*.png')]
bmp_file_list = [path for path in Path(image_path).rglob('*.bmp')]

file_list = jpg_file_list + jpeg_file_list + JPG_file_list + png_file_list + bmp_file_list
file_num = len(file_list)
print('Total images: %d' % file_num)

# Determine number of files to move to each folder
train_percent = 0.8  # 80% of the files go to train
val_percent = 0.1 # 10% go to validation
test_percent = 0.1 # 10% go to test
train_num = int(file_num*train_percent)
val_num = int(file_num*val_percent)
test_num = file_num - train_num - val_num
print('Images moving to train: %d' % train_num)
print('Images moving to validation: %d' % val_num)
print('Images moving to test: %d' % test_num)

# Select files for train folder
for i, file_path in enumerate(file_list[:train_num]):
    fn = file_path.name
    base_fn = file_path.stem
    parent_path = file_path.parent
    xml_fn = base_fn + '.xml'
    os.rename(file_path, train_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(train_path,xml_fn))
    

# Select files for validation folder
for i, file_path in enumerate(file_list[train_num:train_num+val_num]):
    fn = file_path.name
    base_fn = file_path.stem
    parent_path = file_path.parent
    xml_fn = base_fn + '.xml'
    os.rename(file_path, val_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(val_path,xml_fn))

# Select files for test folder
for i, file_path in enumerate(file_list[train_num+val_num:]):
    fn = file_path.name
    base_fn = file_path.stem
    parent_path = file_path.parent
    xml_fn = base_fn + '.xml'
    os.rename(file_path, test_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(test_path,xml_fn))