import re


def replace_latex_E(text):
    def find_matching_brace(s, start):
        stack = []
        for i, char in enumerate(s[start:], start=start):
            if char == "{":
                stack.append(i)
            elif char == "}":
                if stack:
                    stack.pop()
                    if not stack:
                        return i
        return -1

    def replace_E_with_brackets(s):
        pattern = re.compile(r"\\E{")
        result = []
        last_pos = 0

        while True:
            match = pattern.search(s, last_pos)
            if not match:
                break

            start = match.start()
            result.append(s[last_pos:start])
            result.append("E\\left[")
            end = find_matching_brace(s, match.end() - 1)
            if end != -1:
                inner_content = s[match.end() : end]
                result.append(replace_E_with_brackets(inner_content))
                result.append("\\right]")
                last_pos = end + 1
            else:
                # No matching closing brace found, append the rest as is
                result.append(s[start:])
                break

        result.append(s[last_pos:])
        return "".join(result)

    return replace_E_with_brackets(text)


for fname in ["appendix_one.tex", "appendix_two.tex"]:
    # Read the LaTeX file
    with open(fname, "r") as file:
        content = file.read()

    # Perform the replacement
    new_content = replace_latex_E(content)

    # Write the modified content back to the file
    with open(fname, "w") as file:
        file.write(new_content)
