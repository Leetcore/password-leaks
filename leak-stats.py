output: list[str] = []
filtered_lines: list[str] = []
pw_stats: list[dict[str, str]] = []

pw_count: dict[str, int] = {}
pw_length: dict[str, int] = {}
pw_strength: dict[str, float] = {}

with open("top100-full.txt") as file:
    for line in file:
        line = line.strip()
        # split line by ":" format is "email:pw"
        line_array = line.split(":")
        if len(line_array) != 2:
            continue

        email = line_array[0]
        pw = line_array[1]

        # count pws
        if pw_count.get(pw):
            pw_count[pw] = pw_count[pw] + 1
        else:
            pw_count[pw] = 1

        # longest pws
        pw_length[pw] = len(pw)

        # calc pw strengths
        pw_strength[pw] = 0
        length = len(pw)
        special_chars = '[@_!#$%^&*()<>?/\\|}{~:]'
        has_lowercase_char = False
        has_uppercase_char = False
        has_digit = False
        has_special_char = False
        for char in pw:
            if char.islower():
                has_lowercase_char = True
            if char.isupper():
                has_uppercase_char = True
            if char.isdigit():
                has_digit = True
            if char in special_chars:
                has_special_char = True

        strength = 0
        if has_lowercase_char:
            strength += 26
        if has_uppercase_char:
            strength += 26
        if has_digit:
            strength += 10
        if has_special_char:
            strength += 23
        pw_strength[pw] = length * strength

    sorted_pw_strength = sorted(pw_strength.items(), key=lambda item: item[1], reverse=True)
    print("complexity: ")
    print(sorted_pw_strength[:100])
    
    print("password length:")
    sorted_pw_length = sorted(pw_length.items(), key=lambda item: item[1], reverse=True)
    print(sorted_pw_length[:100])

    print("multiple passwords:")
    sorted_dict = sorted(pw_count.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict[:100])

    with open("result.txt", "a") as f:
        f.write(str(sorted_pw_strength[:100]))
        f.write("\n")
        f.write(str(sorted_pw_length[:100]))
        f.write("\n")
        f.write(str(sorted_dict[:100]))
    