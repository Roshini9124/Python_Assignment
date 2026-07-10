def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        result = ""
        for ch in substring:
            if ch not in result:
                result += ch
        print(result)
 