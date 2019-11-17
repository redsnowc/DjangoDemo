import jieba

from app.consts import SensitiveWord


def for_test(value, args):
    return value * args


def sensitive_word_filter(value):
    cut_msg = jieba.lcut(value)
    print(cut_msg)

    check = list(set(cut_msg) & set(SensitiveWord))
    print(check)

    if check:
        new_value = ""
        for i in check:
            new_value = value.replace(i, "*" * len(i))
        return new_value
    return value
