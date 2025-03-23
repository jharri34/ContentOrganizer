import os
import time
import getopt, sys
from initialize import ensure_nltk_data, initialize_models

from image_data_processing import (
    process_image_files
)

from file_utils import (collect_file_paths,
                        display_directory_tree,
                        simulate_directory_tree,
                          display_simulated_tree,
                            separate_files_by_type) 

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
    initialize_models()
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
    file_paths = collect_file_paths(DATA_PATH)
    end_time = time.time()
    print(f"Time taken to load file paths: {end_time - start_time:.2f} seconds")
    print("-" * 50)

    print("Directory tree before organizing:")
    #display_directory_tree(DATA_PATH)

    # Prepare to collect link type statistics
    link_type_counts = {'hardlink': 0, 'symlink': 0}
    
    # Separate files by type
    image_files = separate_files_by_type(file_paths)
    
   
    

    print("*" * 50)
    print("The file upload was successful. Processing may take a few minutes.")
    print("*" * 50)

  
    
    
if __name__=="__main__":
    main()