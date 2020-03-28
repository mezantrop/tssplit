def tssplit(s, quote='"', delimiter='/', escape='|'):
    in_quotes = in_escape = False
    token = ''
    result = []

    for c in s:
        if in_escape:
            token += c
            in_escape = False
        elif c == escape:
            in_escape = True
            if in_quotes:
                token += c
        elif c == quote:
            in_quotes = False if in_quotes else True
        elif c == delimiter and not in_quotes:
            result.append(token)
            token = ''
        else:
            token += c

    result.append(token)
    return result


if __name__ == "__main__":
    pass
