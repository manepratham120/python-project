import tkinter as tk
import os
import gzip
def get_file_size(file_path):
    """
    Returns the size of a file in bytes
    """
    return os.path.getsize(file_path)

def compress_file(file_path):
    """
    Compresses a file using gzip and returns the compressed file path
    """
    compressed_file_path = file_path + ".gz"
    with open(file_path, "rb") as f_in:
        with gzip.open(compressed_file_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    return compressed_file_path

def show_compression_stats():
    """
    Displays the space before and after compression in the GUI
    """
    original_file_size = get_file_size("my_file.txt")
    compressed_file_path = compress_file("my_file.txt")
    compressed_file_size = get_file_size(compressed_file_path)
    os.remove(compressed_file_path)
    label_before.config(text="Original file size: {} bytes".format(original_file_size))
    label_after.config(text="Compressed file size: {} bytes".format(compressed_file_size))

# Create the GUI window
root = tk.Tk()

# Create the labels for the space before and after compression
label_before = tk.Label(root, text="Original file size:")
label_before.pack()
label_after = tk.Label(root, text="Compressed file size:")
label_after.pack()

# Create the button to trigger the compression
compress_button = tk.Button(root, text="Compress", command=show_compression_stats)
compress_button.pack()

# Start the main loop of the GUI
root.mainloop()