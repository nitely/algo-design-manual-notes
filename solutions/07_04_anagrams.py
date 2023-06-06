# -*- coding: utf-8 -*-

# Generate all possible phrase anagrams

# Backtrack, exhaustive search
# runtime O(n!) factorial

# XXX we can make this usable for long phrases
# by using a Trie to store the dictionary and
# doing pruning based on word prefixes


WORDS = {
    'the',
    'bets',
}


def check_dict(words):
    return set(words.split(' ')).issubset(WORDS)


def backtrack_anagrams(input):
    input = ''.join(input.split(' ')).lower()
    # include possible spaces
    solution = [0] * (len(input) * 2 - 1)
    def _backtrack(k, spaces):
        if k-spaces == len(input):
            words = ''.join(
                input[i] if i != -1 else ' '
                for i in solution[:k])
            if check_dict(words):
                print(words)
        else:
            in_perm = set(solution[:k])
            seen = set()
            for i, n in enumerate(input):
                if i in in_perm:
                    continue
                # only fix unique letters in current branch,
                # prune duplicates fixed in K position
                if n in seen:
                    continue
                seen.add(n)
                solution[k] = i
                _backtrack(k + 1, spaces)
            # Add possible space. Avoid multiple spaces,
            # and starting space
            if k > 0 and solution[k-1] != -1:
                solution[k] = -1
                _backtrack(k + 1, spaces + 1)
    _backtrack(0, 0)


backtrack_anagrams('the best')
# the bets
# bets the
