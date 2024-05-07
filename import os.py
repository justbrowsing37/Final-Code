import sys
import getpass
import os

# Function to disable input
def disable_input():
    # Disable input by redirecting sys.stdin or using getpass.getpass()
    # Save the original sys.stdin if needed

    # For example, redirecting sys.stdin
    global original_stdin
    original_stdin = sys.stdin
    sys.stdin = open(os.devnull)

# Function to re-enable input
def enable_input():
    # Re-enable input by restoring the original sys.stdin or switching back from getpass.getpass()

    # For example, restoring the original sys.stdin
    sys.stdin = original_stdin

# Test the functions
def main():
    # Disable input
    disable_input()

    # Test disabled input
    user_input_disabled = getpass.getpass("Input is disabled. Press Enter to continue...")
    print("Disabled input:", user_input_disabled)

    # Re-enable input
    enable_input()

    # Test re-enabled input
    user_input_enabled = input("Now input is enabled. Enter something: ")
    print("Enabled input:", user_input_enabled)

if __name__ == "__main__":
    main()
