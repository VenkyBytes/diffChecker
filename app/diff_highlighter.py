from itertools import zip_longest
import difflib

class DiffHighlighter:
    @staticmethod
    def highlight_diff(left_text, right_text):
        left_lines = left_text.splitlines()
        right_lines = right_text.splitlines()

        highlighted_left = []
        highlighted_right = []
        line_numbers = []

        differ = difflib.Differ()
        diff_lines = list(differ.compare(left_lines, right_lines))

        for i, diff_line in enumerate(diff_lines, start=1):
            line_numbers.append(i)

            if diff_line.startswith('  '):  # Unchanged line
                highlighted_left.append(diff_line[2:])
                highlighted_right.append(diff_line[2:])
            elif diff_line.startswith('- '):  # Removed line
                highlighted_left.append('<span class="highlight-removed">' + diff_line[2:] + '</span>')
                highlighted_right.append('')
            elif diff_line.startswith('+ '):  # Added line
                highlighted_left.append('')
                highlighted_right.append('<span class="highlight-added">' + diff_line[2:] + '</span>')

        return line_numbers, highlighted_left, highlighted_right
