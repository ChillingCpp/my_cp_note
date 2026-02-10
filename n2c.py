import re
import itertools

class Node:
    _ids = itertools.count()

    def __init__(self, title):
        self.id = f"N{next(Node._ids)}"
        self.title = title.strip()
        self.children = []

def parse_markdown(md: str):
    root = Node("Pattern Recognize")
    stack = [(0, root)]

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line:
            continue

        m = re.match(r"(#+)\s+(.*)", line)
        if m:
            level = len(m.group(1))
            node = Node(m.group(2))

            while stack and stack[-1][0] >= level:
                stack.pop()

            stack[-1][1].children.append(node)
            stack.append((level, node))
            continue

        m = re.match(r"(\s*)-\s+(.*)", line)
        if m:
            indent = len(m.group(1))
            level = 100 + indent // 2
            node = Node(m.group(2))

            while stack and stack[-1][0] >= level:
                stack.pop()

            stack[-1][1].children.append(node)
            stack.append((level, node))

    return root
def escape(text: str) -> str:
    return (
        text.replace("[", "(")
            .replace("]", ")")
            .replace("{", "(")
            .replace("}", ")")
    )

def emit(node: Node, lines: list):
    for c in node.children:
        lines.append(f"{node.id}[{escape(node.title)}] --> {c.id}[{escape(c.title)}]")
        emit(c, lines)
if __name__ == "__main__":
    with open("note.md", encoding="utf-8") as f:
        md = f.read()

    tree = parse_markdown(md)

    lines = ["flowchart TD"]
    emit(tree, lines)

    with open("tree.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
