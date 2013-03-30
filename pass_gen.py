#!/usr/bin/env python


def filter_word(word, min_len, max_len):
    if "'" in word:
        return False
    if "%" in word:
        return False
    if len(word) > max_len:
        return False
    if len(word) < min_len:
        return False
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description=
                                     'Generates passwords with words.')
    parser.add_argument('--dict', dest='filename',
                        default='dict.txt',
                        help='set the dict filename, defaults to dict.txt')
    parser.add_argument('--max', dest='pass_length',
                        default=15, type=int,
                        help='set the maximum length of a '
                        'generated password, defaults to 15')
    parser.add_argument('--words', dest='word_count',
                        default=4, type=int,
                        help='set the maximum number of words in a '
                        'generated password, defaults to 4')
    parser.add_argument('--retries', dest='retries',
                        default=12, type=int,
                        help='set the maximum number of times to look '
                        'for a new word if the found word would exceed '
                        'the max length')
    parser.add_argument('--minword', dest='min_word_length',
                        default=3, type=int,
                        help='set the minimum number of characters in a word')
    parser.add_argument('--maxword', dest='max_word_length',
                        default=8, type=int,
                        help='set the maximum number of characters in a word')
    arg = parser.parse_args()
    thelines = None
    with open(arg.filename) as thefile:
        thelines = thefile.readlines()
    length_limit = arg.pass_length
    import random
    password = ''
    for i in range(arg.word_count):
        too_long_checks = 0
        while too_long_checks < arg.retries:
            word = random.choice(thelines)
            word = word[:-1]  # Remove newline
            word = word[0].upper() + word[1:]  # Capitalize first letter
            if word[-1] == 's':
                # Make possible plurals singular (might break words).
                word = word[:-1]
            if filter_word(word, arg.min_word_length, arg.max_word_length):
                if len(password) + len(word) > length_limit:
                    too_long_checks += 1
                    break
                password += word
                break
    print(password)

if __name__ == '__main__':
    main()
