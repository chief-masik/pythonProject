import re


def main(x):
    pattern = r"<%.?\n?glob.?\n?(\w+)\s?<=\s?#(-?\d+) %>"

    matches = re.findall(pattern, x)
    parsed_data = [(item[0], int(item[1])) for item in matches]

    return parsed_data


input_str1 = '.do <% glob xeen <=#-7965 %> <% glob aarbexe <= #-5596 %>' \
            '<% glob arre_293<=#-8823 %> <% glob abi <= #955 %> .end'
input_str2 = '.do <% glob inama <= #1190 %><% glob/ente <= #-4771 %><% glob' \
            ' tioned_730 <= #-9744 %> .end'
input_str3 = '.do <% glob xeen <=#-7965 %> <% glob aarbexe <= #-5596 %>' \
            '<%\nglob\narre_293<=#-8823 %> <% glob abi <= #955 %> .end'

print(main(input_str3))
