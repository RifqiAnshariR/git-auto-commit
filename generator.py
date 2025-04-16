from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re
from config import COMMIT_TYPES
from prompt import natural_prompt
from helper import diff_to_natural, type_to_natural

def generate_commit_message(diff):
    model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )

    # Handle special tokens for Deepseek
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    filtered_diff = "\n".join(line for line in diff.splitlines() if line.startswith("+") or line.startswith("-"))
    natural_diff = diff_to_natural(filtered_diff)
    natural_type = type_to_natural(COMMIT_TYPES)
    prompt = natural_prompt(natural_diff, natural_type)

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
        max_new_tokens=30,
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
        commit_msg = raw_output

    return commit_msg