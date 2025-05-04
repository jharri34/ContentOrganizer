import os
import re
import datetime  # Import datetime for date operations
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn

def sanitize_filename(name, max_length=50, max_words=5):
    """Sanitize the filename by removing unwanted words and characters."""
    # Remove file extension if present
    name = os.path.splitext(name)[0]
    # Remove unwanted words and data type words
    name = re.sub(
        r'\b(jpg|jpeg|png|gif|bmp|txt|md|pdf|docx|xls|xlsx|csv|ppt|pptx|image|picture|photo|this|that|these|those|here|there|'
        r'please|note|additional|notes|folder|name|sure|heres|a|an|the|and|of|in|'
        r'to|for|on|with|your|answer|should|be|only|summary|summarize|text|category)\b',
        '',
        name,
        flags=re.IGNORECASE
    )
    # Remove non-word characters except underscores
    sanitized = re.sub(r'[^\w\s]', '', name).strip()
    # Replace multiple underscores or spaces with a single underscore
    sanitized = re.sub(r'[\s_]+', '_', sanitized)
    # Convert to lowercase
    sanitized = sanitized.lower()
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    # Split into words and limit the number of words
    words = sanitized.split('_')
    limited_words = [word for word in words if word]  # Remove empty strings
    limited_words = limited_words[:max_words]
    limited_name = '_'.join(limited_words)
    # Limit length
    return limited_name[:max_length] if limited_name else 'untitled'
def compute_operations(data_list, new_path, renamed_files, processed_files):
    """Compute the file operations based on generated metadata."""
    operations = []
    for data in data_list:
        file_path = data['file_path']
        if file_path in processed_files:
            continue
        processed_files.add(file_path)

        # Prepare folder name and file name
        folder_name = data['foldername']
        new_file_name = data['filename'] + os.path.splitext(file_path)[1]

        # Prepare new file path
        dir_path = os.path.join(new_path, folder_name)
        new_file_path = os.path.join(dir_path, new_file_name)

        # Handle duplicates
        counter = 1
        original_new_file_name = new_file_name
        while new_file_path in renamed_files:
            new_file_name = f"{data['filename']}_{counter}" + os.path.splitext(file_path)[1]
            new_file_path = os.path.join(dir_path, new_file_name)
            counter += 1

        # Decide whether to use hardlink or symlink
        link_type = 'hardlink'  # Assume hardlink for now

        # Record the operation
        operation = {
            'source': file_path,
            'destination': new_file_path,
            'link_type': link_type,
            'folder_name': folder_name,
            'new_file_name': new_file_name
        }
        operations.append(operation)
        renamed_files.add(new_file_path)

    return operations  # Return the list of operations for display or further processing
def execute_operations(operations, dry_run=False, silent=False, log_file=None):
    """Execute the file operations."""
    total_operations = len(operations)

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True
    ) as progress:
        task = progress.add_task("Organizing Files...", total=total_operations)
        for operation in operations:
            source = operation['source']
            destination = operation['destination']
            link_type = operation['link_type']
            dir_path = os.path.dirname(destination)

            if dry_run:
                message = f"Dry run: would create {link_type} from '{source}' to '{destination}'"
            else:
                # Ensure the directory exists before performing the operation
                os.makedirs(dir_path, exist_ok=True)

                try:
                    if link_type == 'hardlink':
                        os.link(source, destination)
                    else:
                        os.symlink(source, destination)
                    message = f"Created {link_type} from '{source}' to '{destination}'"
                except Exception as e:
                    message = f"Error creating {link_type} from '{source}' to '{destination}': {e}"

            progress.advance(task)

            # Silent mode handling
            if silent:
                if log_file:
                    with open(log_file, 'a') as f:
                        f.write(message + '\n')
            else:
                print(message)