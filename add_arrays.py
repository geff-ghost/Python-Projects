
# ...existing code...
def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for s in strs:
            if s[i] != ch:
                return shortest[:i]
    return shortest

# if __name__ == "__main__":
#     tests = [
#         (["flower","flow","flight"], "fl"),
#         (["dog","racecar","car"], ""),
#         ([""], ""),
#         (["a"], "a"),
#     ]
#     for inp, expected in tests:
#         out = longest_common_prefix(inp)
#         print(inp, "->", out, "expected:", expected)


strs = ["flo", "flower", "flop", "flow", "flight", "fl", "far"]
print(min(strs))
print(strs.index(min(strs)))
print(min(strs, key=len))
print(strs.index(min(strs, key=len)))