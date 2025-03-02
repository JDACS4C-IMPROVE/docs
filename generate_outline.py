import os
import re

def parse_rst(file_path, indent=0):
    outline = ""
    if not os.path.exists(file_path):
        return ""

    with open(file_path, 'r') as file:
        lines = file.readlines()

    inside_toctree = False
    for line in lines:
        if line.strip().startswith(".. toctree::"):
            inside_toctree = True
            continue
        if inside_toctree:
            match = re.match(r'\s+(.*)', line)
            if match:
                link = match.group(1).strip()
                if link.startswith(":") or not link:
                    continue

                # Handle "Title <link>" syntax
                if '<' in link and '>' in link:
                    link = re.findall(r'<(.*)>', link)[0].strip()

                child_rst = link if link.endswith(".rst") else f"{link}.rst"
                child_path = os.path.normpath(os.path.join(os.path.dirname(file_path), child_rst))
                outline += "  " * indent + f"- {child_path}\n"
                outline += parse_rst(child_path, indent + 1)
            elif not line.strip():
                continue
            else:
                break
    return outline

if __name__ == "__main__":
    main_rst = "index.rst"
    sitemap = f"- {main_rst}\n" + parse_rst(main_rst, 1)

    with open("docs_outline.txt", "w") as f:
        f.write(sitemap)

    print("Outline generated: docs_outline.txt")
