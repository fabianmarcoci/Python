def group_by_rhyme(words):
    rhyme_dict = {}

    for word in words:
        rhyme = word[-2:]

        if rhyme not in rhyme_dict:
            rhyme_dict[rhyme] = []
        rhyme_dict[rhyme].append(word)

    return list(rhyme_dict.values())


if __name__ == '__main__':
    words_list = ['ana', 'banana', 'carte', 'arme', 'parte']
    print(group_by_rhyme(words_list))
