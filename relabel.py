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
    # determine the number of each symptom
    return label 

def get_label(file):
    filename = file.replace(".wav", "")
    label_path = source + "/" + filename + "_label.txt"
    label = convert_label(label_path)
    return label

def process_data(src_folder, dest_folder):
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
        print(f"Removed existing directory")
    os.makedirs(dest_folder)

    total = 0
    rhonchi = 0
    stridor = 0
    wheeze = 0

    counter = 1
    for file in os.listdir(src_folder):
        if file.endswith(".wav"):
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, f"{counter}.wav")
            label_path = os.path.join(dest_folder, f"{counter}")
            shutil.copy(src_path, dest_path)

            label = get_label(file)
            np.save(label_path, label)

            total += 1
            if label[0] == 1:
                rhonchi += 1
            if label[1] == 1:
                stridor += 1
            if label[2] == 1:
                wheeze += 1

            counter += 1
    
    return total, rhonchi, stridor, wheeze

source = "test"
total, rhonchi, stridor, wheeze = process_data(source, "test2")

print(f"Total: {total}")
print(f"Rhonchi: {rhonchi}")
print(f"Stridor: {stridor}")
print(f"Wheeze: {wheeze}")


label_file = "train/steth_20190128_09_29_27_label.txt"
print(convert_label(label_file))