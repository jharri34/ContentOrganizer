import os
import time
import getopt, sys
from initialize import ensure_nltk_data, initialize_models
from sortphoto import file_utils
from image_data_processing import process_image_files
from data_processing import compute_operations


DATA_PATH = "/mnt/d/Pictures"
OUTPUT_PATH = "/mnt/d/Organize_Pictures"
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hdt"
# Long options
long_options = ["Help", "date", "type"]

def main():
    # Ensure NLTK data is downloaded efficiently and quietly
    ensure_nltk_data()
    
    # Initialize models once
    print("Checking if the model is already downloaded. If not, downloading it now.")
    image_inference, text_inference= initialize_models()
    print("*" * 50)
    print("The file upload was successful. Processing may take a few minutes.")
    print("*" * 50)

    # Start with dry run set to True
    dry_run = True

    # Confirm successful output path
    output_path = os.path.join(os.path.dirname(DATA_PATH), 'organized_folder')
    print(f"Output path successfully set to: {output_path}")
    print("-" * 50)

    # Start processing files
    start_time = time.time()
    file_paths = file_utils.collect_file_paths(DATA_PATH)
    end_time = time.time()
    print(f"Time taken to load file paths: {end_time - start_time:.2f} seconds")
    print("-" * 50)

    print("Directory tree before organizing:")
    # display_directory_tree(DATA_PATH)
    print("*" * 50)
    print("The file upload was successful. Processing may take a few minutes.")
    print("*" * 50)

    # Prepare to collect link type statistics
    link_type_counts = {'hardlink': 0, 'symlink': 0}
    
    # Separate files by type
    image_files = file_utils.separate_files_by_type(file_paths)

    # Process files sequentially
    data_images = process_image_files(image_files, image_inference, text_inference)
    
    # Prepare for copying and renaming
    renamed_files = set()
    processed_files = set()
    
    operations = compute_operations(
                    data_images,
                    output_path,
                    renamed_files,
                    processed_files
                )
    # Simulate and display the proposed directory tree
    print("-" * 50)
    message = "Proposed directory structure:"

    print(message)
    print(os.path.abspath(output_path))
    simulated_tree = file_utils.simulate_directory_tree(operations, output_path)
    file_utils.display_simulated_tree(simulated_tree)
    print("-" * 50)
   

  
    
    
if __name__=="__main__":
    main()