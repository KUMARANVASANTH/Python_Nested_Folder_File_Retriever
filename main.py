import os
import shutil
import pydicom
def extract_dicom_images(source_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.dcm'):
                dicom_file_path = os.path.join(root, file)
                shutil.copy(dicom_file_path, output_folder)
                print(f"Extracted: {dicom_file_path} -> {output_folder}/{file}")
def extract_from_nested_folders(source_folder, output_folder):
    for dir_name in os.listdir(source_folder):
        current_folder = os.path.join(source_folder, dir_name)
        if os.path.isdir(current_folder):
            try:
                extract_dicom_images(current_folder, output_folder)
                extract_from_nested_folders(current_folder, output_folder)
            except PermissionError:
                print(f"Warning: Permission denied for {current_folder}. Skipping.")
def main():
    source_folder = os.path.abspath('/input_file_path')  
    output_folder = '/output_file_path'  
    extract_from_nested_folders(source_folder, output_folder)

if __name__ == "__main__":
    main()


