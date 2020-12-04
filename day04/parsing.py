import pyparsing as pp

pp.ParserElement.setDefaultWhitespaceChars(" \t")

key = pp.Word(pp.alphas)
value = pp.Word(pp.alphanums + "#")
entry = pp.Group(key + pp.Suppress(":") + value)
line_end = pp.Suppress(pp.LineEnd() ^ pp.StringEnd())
line = entry[1, ...] + line_end

block = pp.Group(line[1, ...]) + line_end
blocks = block[1, ...]


def parse_entry(text: str):
    result = tuple(entry.parseString(text)[0])
    return result


def parse_passports(text: str):
    result = blocks.parseString(text).asList()
    return result


def to_password_dicts(parse_result):
    return [dict(block) for block in parse_result]