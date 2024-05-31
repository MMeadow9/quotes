def format_text(text: str, max_symbs: int, max_words: int=None):
    """
    :param max_symbs: Максимальное кол-во символов в строке
    :param max_words: Максимальное кол-во слов в строке
    :return: Отформатированный текст
    """
    formated_text = []
    line = []
    len_line = 0
    for word in text.split():
        if max_words:
            if len(line) >= max_words:
                formated_text.append(" ".join(line))
                line = []
                len_line = 0
                continue
        if len_line >= max_symbs:
            formated_text.append(" ".join(line))
            line = []
            len_line = 0
            continue
        else:
            len_line += len(word) + 1
            line.append(word)

    formated_text.append(" ".join(line)) if line else 0

    return "\n".join(formated_text)

