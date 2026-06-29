import subprocess
import sys

def run_cmd(cmd):
    try:
        # Run command and capture output
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        # Ignore "remote origin already exists" error, fail on others
        if "remote origin already exists" in e.stderr or "already exists" in e.stderr:
            return
        print(f"\n[Error executing]: {cmd}")
        print(e.stderr.strip())
        sys.exit(1)

def main():
    print("==================================================")
    print("   AUTOMATED GITHUB UPLOADER FOR LAIBA TANSEER    ")
    print("==================================================")
    
    print("\n1. Configuring Git identity...")
    run_cmd('git config user.email "laibtanser@gmail.com"')
    run_cmd('git config user.name "Laiba Tanseer"')
    print("[OK] Git identity configured.")
    
    print("\n2. Initializing local Git repository...")
    run_cmd('git init')
    print("[OK] Git repository initialized.")
    
    print("\n3. Linking your GitHub repository...")
    run_cmd('git remote add origin https://github.com/laiba-540/My-Portfolio1.git')
    print("[OK] GitHub repository linked.")
    
    print("\n4. Adding all files and folders (including Django code)...")
    run_cmd('git add .')
    print("[OK] Files added to staging.")
    
    print("\n5. Creating local save (commit)...")
    run_cmd('git commit -m "Upload all Django files and folders"')
    print("[OK] Save commit created.")
    
    print("\n5b. Setting branch name to main...")
    run_cmd('git branch -M main')
    print("[OK] Branch name set to main.")
    
    print("\n6. Uploading to GitHub...")
    print("--> Note: If a popup appears asking you to sign in to GitHub, please click sign in to authorize the upload.")
    run_cmd('git push -f origin main')
    
    print("\n==================================================")
    print("🎉 SUCCESS! All folders are uploaded to GitHub!  ")
    print("==================================================")
    print("\nNow you can go to your PythonAnywhere console and run:")
    print("   git pull")

if __name__ == '__main__':
    main()
