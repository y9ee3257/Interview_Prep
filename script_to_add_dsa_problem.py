#!/usr/bin/env python3
"""
LeetCode add script (executable)

What this does (high level)
---------------------------
1. Extracts the problem slug from a LeetCode problem URL.
2. Creates a Python file for the problem in the configured folder,
   with the LeetCode URL as a top-of-file comment.
3. Updates the README.md:
   - Adds the URL under the last topic (creates a "General Problems" topic if none exist).
   - If SHOULD_PRACTICE_AGAIN is True, also adds the URL under "### Practice Again"
     (creates that section if missing).
   - Maintains sequential numbering within each section.
   - Prevents duplicate entries inside the same section, but allows the same URL to
     be present in different sections (e.g., main topic AND Practice Again).

Configuration
-------------
Edit the variables in the CONFIGURATION block below and run the script.
"""

import os
import re
from typing import List, Tuple, Optional

# ===========================
# CONFIGURATION (edit here)
# ===========================
LEETCODE_URL = "https://leetcode.com/problems/add-two-numbers/"
SHOULD_PRACTICE_AGAIN = True
CREATE_FILE = True
FOLDER_PATH = "dsa/leetcode_top_interview_questions/linked_list"
README_PATH = "dsa/leetcode_top_interview_questions/readme.md"

# ===========================


def get_problem_slug(url: str) -> str:
    m = re.search(r"/problems/([\w\-]+)/?", url)
    if not m:
        raise ValueError(f"Invalid LeetCode URL: {url}")
    return m.group(1)


def ensure_folder(folder: str) -> None:
    os.makedirs(folder, exist_ok=True)


def create_problem_file(folder: str, slug: str, url: str) -> str:
    """Create a python file with the url as top comment. Return filepath."""
    ensure_folder(folder)
    filename = slug.replace("-", "_") + ".py"
    path = os.path.join(folder, filename)
    # Only write if file doesn't exist to avoid overwriting your notes,
    # but you can always re-run to create if missing.
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {url}\n\n")
        print(f"✅ Created file: {path}")
    else:
        print(f"ℹ️  File already exists: {path}")
    return path


def read_readme(path: str) -> List[str]:
    if not os.path.exists(path):
        print(f"⚠️ README not found. A new README will be created at {path}")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def write_readme(path: str, lines: List[str]) -> None:
    # Ensure file ends with newline
    if lines and not lines[-1].endswith("\n"):
        lines[-1] = lines[-1] + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"✅ Updated README: {path}")


def find_section_ranges(lines: List[str]) -> List[Tuple[str, int, int]]:
    """
    Find all '### Section' ranges.
    Return list of tuples: (section_name, start_index, end_index_exclusive)
    end_index_exclusive is index of next section header or len(lines)
    """
    headers = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("### "):
            section = stripped[4:].strip()
            headers.append((section, i))
    ranges = []
    for idx, (name, start) in enumerate(headers):
        end = headers[idx + 1][1] if idx + 1 < len(headers) else len(lines)
        ranges.append((name, start, end))
    return ranges


def get_last_topic_name(lines: List[str]) -> str:
    """
    Return the name of the last non-'Practice Again' topic.
    If no topics exist, return 'Problems'.
    """
    ranges = find_section_ranges(lines)
    non_practice = [r for r in ranges if r[0].strip().lower() != "practice again"]
    if non_practice:
        return non_practice[-1][0]
    return "Problems"


def section_exists(lines: List[str], section_name: str) -> bool:
    return any(line.strip() == f"### {section_name}" for line in lines)


def create_section_at_end(lines: List[str], section_name: str) -> Tuple[List[str], int]:
    """
    Append a section header at the end and return new lines and index of header.
    Ensures there is a blank line before the new header for readability.
    """
    if lines and not lines[-1].endswith("\n"):
        lines[-1] = lines[-1] + "\n"
    if lines and lines[-1].strip() != "":
        lines.append("\n")
    lines.append(f"### {section_name}\n")
    # ensure a blank line after header for consistent insertion logic
    if lines[-1] != "\n":
        lines.append("\n")
    return lines, len(lines) - 2  # header index


def get_section_range(lines: List[str], section_name: str) -> Tuple[int, int]:
    """
    Return (start_index, end_index) for the section. If missing, return (-1,-1).
    start_index points at the header line (### ...).
    end_index is the index of the next section header or len(lines).
    """
    ranges = find_section_ranges(lines)
    for name, start, end in ranges:
        if name.strip() == section_name:
            return start, end
    return -1, -1


def next_number_for_section(lines: List[str], start_idx: int, end_idx: int) -> int:
    """
    Compute the next sequential number for the section by scanning lines
    between start_idx+1 and end_idx-1 for existing numbering 'N. ' and returning max+1.
    """
    max_num = 0
    for i in range(start_idx + 1, end_idx):
        line = lines[i].strip()
        m = re.match(r"^(\d+)\.\s", line)
        if m:
            try:
                val = int(m.group(1))
                if val > max_num:
                    max_num = val
            except ValueError:
                pass
    return max_num + 1


def url_in_section(lines: List[str], start_idx: int, end_idx: int, url: str) -> bool:
    """Return True if url appears in the given section slice."""
    for i in range(start_idx + 1, end_idx):
        if url in lines[i]:
            return True
    return False


def insert_url_into_section(lines: List[str], section_name: str, url: str) -> List[str]:
    """
    Ensure section exists, then insert url with next number.
    Do not add duplicate inside the same section.
    """
    start_idx, end_idx = get_section_range(lines, section_name)
    if start_idx == -1:
        lines, header_idx = create_section_at_end(lines, section_name)
        start_idx = header_idx
        end_idx = len(lines)

    # Recompute end_idx in case lines changed
    _, end_idx = get_section_range(lines, section_name)

    if url_in_section(lines, start_idx, end_idx, url):
        print(f"ℹ️  URL already present in section '{section_name}', skipping insertion there.")
        return lines

    nxt = next_number_for_section(lines, start_idx, end_idx)
    new_line = f"{nxt}. {url}\n"

    # Insert before end_idx (so before next section header or EOF)
    insert_at = end_idx
    # If there's trailing blank lines at end_idx-1, insert before them to keep items contiguous
    while insert_at - 1 > start_idx and lines[insert_at - 1].strip() == "":
        insert_at -= 1

    lines.insert(insert_at, new_line)
    print(f"✅ Inserted into '{section_name}' as {nxt}.")
    return lines


def update_readme(lines: List[str], url: str, should_practice: bool) -> List[str]:
    """
    Add URL under last topic and under Practice Again (if requested).
    Returns updated lines.
    """
    # If README empty, create initial topic
    if not lines:
        lines = ["### General Problems\n", "\n"]

    topic_name = get_last_topic_name(lines)
    lines = insert_url_into_section(lines, topic_name, url)

    if should_practice:
        lines = insert_url_into_section(lines, "Practice Again", url)

    return lines


def main():
    if CREATE_FILE:
        try:
            slug = get_problem_slug(LEETCODE_URL)
        except ValueError as e:
            print(f"❌ {e}")
            return
        create_problem_file(FOLDER_PATH, slug, LEETCODE_URL)

    lines = read_readme(README_PATH)
    new_lines = update_readme(lines, LEETCODE_URL, SHOULD_PRACTICE_AGAIN)
    write_readme(README_PATH, new_lines)


if __name__ == "__main__":
    main()
