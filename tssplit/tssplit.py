def tssplit(s, quote='"\'', delimiter=':;,', escape='/^', trim=''):
    """Split a string by delimiters with quotes and escaped characters, optionally trimming results

    :param s: A string to split into chunks
    :param quote: Quote signs to protect a part of s from parsing
    :param delimiter: A chunk separator symbol
    :param escape: An escape character
    :param trim: Trim characters from chunks
    :return: A list of chunks
    """

    in_quotes = in_escape = False
    token = ''
    result = []

    for c in s:
        if in_escape:
            token += c
            in_escape = False
        elif c in escape:
            in_escape = True
            if in_quotes:
                token += c
        elif c in quote and not in_escape:
            in_quotes = False if in_quotes else True
        elif c in delimiter and not in_quotes:
            if trim:
                token = token.strip(trim)
            result.append(token)
            token = ''
        else:
            token += c

    if trim:
        token = token.strip(trim)
    result.append(token)
    return result


if __name__ == "__main__":
    pass
