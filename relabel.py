import os
import shutil
import numpy as np

# [Rhonchi, Stridor, Wheeze]

# Expecting a txt file
def convert_label(file_path):
    label = np.zeros(3)
    with open(file_path, 'r') as file:
        for line in file.readlines():
            first_word = line.split()[0]
            if first_word == "Rhonchi":
                label[0] = 1
            elif first_word == "Stridor":
                label[1] = 1
            elif first_word == "Wheeze":
                label[2] = 1
    return label 

def get_label(file):
    filename = file.replace(".wav", "")
    label_path = "train/" + filename + "_label.txt"
    label = convert_label(label_path)
    return label

def process_data(src_folder, dest_folder):
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
        print(f"Removed existing directory")
    os.makedirs(dest_folder)

    counter = 1
    for file in os.listdir(src_folder):
        if file.endswith(".wav"):
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, f"{counter}.wav")
            label_path = os.path.join(dest_folder, f"{counter}")
            shutil.copy(src_path, dest_path)

            label = get_label(file)
            np.save(label_path, label)

            counter += 1

source = "train"
process_data(source, "train2")

# label_file = "train/trunc_2019-07-31-10-20-16-L6_13_label.txt"
# print(convert_label(label_file))