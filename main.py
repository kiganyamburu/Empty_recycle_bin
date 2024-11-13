import ctypes
import os

def empty_recycle_bin():
    try:
        recycle_bin_flags = 0x00000001 | 0x00000002 | 0x00000004
        
        # Call Windows Shell API to empty the Recycle Bin
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, recycle_bin_flags)
        
        if result == 0:
            print("Recycle Bin emptied successfully.")
        else:
            print(f"Failed to empty Recycle Bin. Error code: {result}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    empty_recycle_bin()
