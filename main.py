import subprocess
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re

def get_staged_diff():
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout.strip()

def generate_commit_message(diff):
    model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )

    # Handle special tokens untuk DeepSeek
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    filtered_diff = "\n".join(line for line in diff.splitlines() if line.startswith("+") or line.startswith("-"))
    
    commit_types = """
    - build: Build system or dependencies
    - ci: CI config/scripts
    - chore: Maintenance
    - docs: Documentation
    - feat: New features
    - fix: Bug fixes
    - perf: Performance
    - refactor: Code restructuring
    - revert: Revert commit
    - style: Code formatting
    - test: Tests
    - security: Security fixes
    """

    prompt = f"""<|beginoftext|>system
    You are a helpful AI assistant.<|endoftext|>
    <|beginoftext|>user
    Generate a short Git commit message of Diff based on commit types. Generates only commit message.

    Commit Types:
    {commit_types}

    Diff:
    ```{filtered_diff}```
    <|endoftext|>
    <|beginoftext|>assistant"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048,
        return_attention_mask=True
    ).to(model.device)
    
    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_new_tokens=50,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Ambil bagian setelah 'assistant'
    if "assistant" in full_response:
        raw_output = full_response.split("assistant")[-1].strip()
    else:
        raw_output = full_response.strip()

    # Ambil isi dalam tanda kutip
    match = re.search(r'"(.*?)"', raw_output)
    if match:
        commit_msg = match.group(1)
    else:
        # commit_msg = raw_output.splitlines()[0].strip("` ").strip()
        commit_msg = "Error: Unable to generate commit message."
        
    return commit_msg

def main():
    diff = get_staged_diff()
    if not diff:
        print("No staged changes to commit.")
        return

    message = generate_commit_message(diff)
    subprocess.run(["git", "commit", "-m", message])
    print(f"Commit message: {message}")

if __name__ == "__main__":
    main()
