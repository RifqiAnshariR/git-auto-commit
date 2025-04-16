import subprocess

def get_staged_diff():
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout.strip()

def diff_to_natural(diff):
    lines = diff.strip().split('\n')
    changes = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Modified line (one deletion followed by one addition)
        if line.startswith('-') and i + 1 < len(lines) and lines[i + 1].strip().startswith('+'):
            removed = lines[i][1:].strip()
            added = lines[i + 1][1:].strip()
            changes.append(f"Modified `{removed}` to `{added}`")
            i += 2

        # Added line
        elif line.startswith('+'):
            added = line[1:].strip()
            changes.append(f"Added `{added}`")
            i += 1

        # Removed line
        elif line.startswith('-'):
            removed = line[1:].strip()
            changes.append(f"Removed `{removed}`")
            i += 1

        else:
            i += 1

    return "\n".join(changes)

def type_to_natural(types):
    return "".join([f"Use this as commit type: {ctype}, if Diff related to {info['description']} (keywords: {', '.join(info['keywords'])}). "for ctype, info in types.items()])
