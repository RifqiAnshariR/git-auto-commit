def natural_prompt(natural_diff, natural_type):
    return f"""<|beginoftext|>system
    You are a professional code reviewer.
    <|endoftext|>
    <|beginoftext|>user
    Generate a consice Git commit message from the following Diff.

    Diff:
    {natural_diff}

    Add one of these following commit types related to the generated Git commit message.

    commit types:
    {natural_type}

    Return generated commit message and commit type ONLY in this ONE LINE format:
    "<commit type>: <commit message>"
    Return without additional explanation or note.
    <|endoftext|>
    <|beginoftext|>assistant
    """