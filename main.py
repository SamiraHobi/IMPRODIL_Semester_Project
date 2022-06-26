"""
Count all slang terms in a corpus.
"""

import spacy
from collections import Counter
from argparse import ArgumentParser, FileType

nlp = spacy.load("en_core_web_sm")


def split_corpus_at_newline(filename: object) -> list:
    """
    Split the input file at every newline character.

    :param filename: Corpus as a text file
    """
    cor_list: list[str] = [line.rstrip('\n') for line in filename]
    return cor_list


def tokenise_slang(slang_file: object) -> list:
    """
    Tokenise all slang terms by splitting at every new line character.

    :param slang_file: slang stored in text file
    """
    slang_list = [line.rstrip('\n') for line in slang_file]
    return slang_list


def tokenise_corpus(corpus_list: list) -> list:
    """
    Tokenise a corpus with SpaCy.

    :param corpus_list: list where every line of a corpus is saved as a string
    """
    tok_lst = []
    for element in corpus_list:
        spacy_element = nlp(element)
        for token in spacy_element:
            token = token.text
            tok_lst.append(token)
    return tok_lst


def put_slangwords_in_list(tokenised_list: list, slang_lst: list) -> list:
    """
    Check if slang term occurs in corpus, if yes add every instance to c_lst.

    :param tokenised_list: list of tokens of a corpus
    :param slang_lst: list of slang terms saved a strings
    """
    c_lst = []
    for slang in slang_lst:
        # make all tokens case insensitive
        slang = slang.casefold()
        for token in tokenised_list:
            token = token.casefold()
            if slang == token:
                c_lst.append(token)
    return c_lst


def count_slangwords(to_be_counted_list: list) -> list:
    """
    Count number of occurrences of each slang term.

    :param to_be_counted_list: list of slang-words that occurred in corpus
    """
    count = Counter(to_be_counted_list)
    return count.most_common()


def main():
    # create a cli
    parser = ArgumentParser(description="Count the number of slang terms in at least one corpus.")
    parser.add_argument('corpus1', type=FileType('r'),
                        help="The file containing the first corpus.")
    parser.add_argument('slang_file', type=FileType('r'), help="The list containing slang terms.")
    parser.add_argument('--corpus2', '-i', type=FileType('r'),
                        help='A second corpus if ones wishes to compare the frequency of slang terms.')
    # Parse console arguments
    args = parser.parse_args()
    split_corpus = split_corpus_at_newline(args.corpus1)
    tokenised_slang = tokenise_slang(args.slang_file)
    tokenised_corpus = tokenise_corpus(split_corpus)
    ready_for_counting = put_slangwords_in_list(tokenised_corpus, tokenised_slang)
    counted_list = count_slangwords(ready_for_counting)
    # if the optional flag is used, compare the two corpora
    if args.corpus2:
        split_corpus2 = split_corpus_at_newline(args.corpus2)
        tokenised_corpus2 = tokenise_corpus(split_corpus2)
        ready_for_counting2 = put_slangwords_in_list(tokenised_corpus2, tokenised_slang)
        counted_list2 = count_slangwords(ready_for_counting2)
        print('This is a list of slang-terms for the first corpus: ', counted_list)
        print('The most frequent term is', counted_list[0])
        print('Number of total slang-terms:', len(ready_for_counting), 'number of unique slang-terms:',
              len(counted_list))
        print('This is a list of slang-terms for the second corpus:', counted_list2)
        print('The most frequent term is', counted_list2[0])
        print('Number of total slang-terms:', len(ready_for_counting2), 'number of unique slang-terms:',
              len(counted_list2))
    # if no optional flag is used, simply count the slang-terms of the first and only corpus
    else:
        print('This is a list of slang-terms for the corpus', counted_list)
        print('The most frequent term is', counted_list[0])
        print('Number of total slang-terms:', len(ready_for_counting), 'number of unique slang-terms:', len(counted_list))


if __name__ == '__main__':
    main()
