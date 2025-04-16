import subprocess
from helper import get_staged_diff
from generator import generate_commit_message

def main():
    diff = get_staged_diff()
    if not diff:
        print("No staged changes to commit.")
        return
    message = generate_commit_message(diff)
    print(f"Commit message: {message}")
    confirm = input("\nContinue to commit? (y/n): ").strip().lower()
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", message])
    elif confirm == "n":
        print("Commit cancelled.")
    else:
        print("Not a valid option. Commit cancelled.")

if __name__ == "__main__":
    main()
