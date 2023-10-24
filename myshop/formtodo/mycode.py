import subprocess


def run_server():
    try:
        subprocess.run(["py", "manage.py", "runserver"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: 'py' or 'manage.py' not found. Make sure Python and Django are installed and you're in the correct directory.")


if __name__ == "__main__":
    run_server()
