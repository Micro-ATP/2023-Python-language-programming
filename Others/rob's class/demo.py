from collections import defaultdict

def group_anagrams(strs):
    anagrams_dict = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        anagrams_dict[key].append(s)

    result = [set(group) for group in anagrams_dict.values()]

    return result

input_strs = ["listen", "cab", "abc", "silent", "hello", "hit", "enlist", "ith"]
output_groups = group_anagrams(input_strs)
print(output_groups)

# powered by Genshin Impact