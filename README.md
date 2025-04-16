# 📌 Description  
**Git Auto Commit Message**  
This is an automation tool to generate Git commit messages based on the conventional rule from staged diff changes. It uses **deepseek-coder-1.3b-instruct** model.

# 🚀 How to Run  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/RifqiAnshari/git-auto-commit.git  
   cd git-auto-commit  
   ```  
2. Set up the virtual environment:  
   ```bash  
   python -m venv venv  
   venv\Scripts\activate  # On Windows  
   # source venv/bin/activate  # On macOS/Linux
   ```  
3. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. Run the script with Python (recommended: Python 3.8+):  
   ```bash  
   python main.py  
   ```  

# ⚙️ PowerShell Configuration  
To use the custom Git alias for this script, follow these steps:  

1. Change git_acm.ps1 file with your actual file path. 

2. Enter this command to your terminal (powershell):  
   ```powershell
   git config --global alias.acm '!powershell -ExecutionPolicy Bypass -File "<absolute path of .ps1 file>"'
   ```  

3. This alias will allows you to run the script using:  
   ```bash  
   git acm  
   ```

# 📄 Usage  
- Automatically fetches staged Git changes and generates a commit message.  
- The generated commit message follows by the conventional commit types defined in the configuration.  
- Once confirmed, the script commits the changes with the generated message.  

---

Made with ❤️!