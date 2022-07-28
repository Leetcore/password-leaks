import os

with open("wiki_domains.txt", "r") as f:
    count = 0
    group_regex: list[str] = []
    for line in f:
        count = count + 1
        email = line.split(":")[0]
        group_regex.append("@" + email.strip().replace('.', '\\.').replace('-', '\\-'))

        if count % 20 == 0:
            command = "grep -riah -E '" + "|".join(group_regex) +"' /Volumes/Externe/CompilationOfManyBreaches/data | tee top100-plain-"+ str(count) + ".txt"
            print(command)
            if count == 100:
                os.system(command)
            group_regex = []