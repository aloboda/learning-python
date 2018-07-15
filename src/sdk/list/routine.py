

if __name__ == '__main__':
    # TODO:andrii.loboda:2018-06-12: make as test
    letters = ['A', 'B', 'C', 'D']
    print('Initial array: {}'.format(letters))
    print('`A` in letters: {}'.format('A' in letters))

    consonants = [letter for letter in letters if letter != 'A']
    print('consonants: {}'.format(consonants))

    consonants_gen = (letter for letter in letters if letter != 'A')
    print('consonants: {}'.format(consonants_gen))
    print('consonants: 0=>{0}'.format(next(consonants_gen)))
    print('consonants: 1=>{0}'.format(next(consonants_gen)))

    empty_gen = (item for item in [] if False)
    print('empty generator: {0}'.format(empty_gen))
    print('First item of empty generator:{0}'.format(next(empty_gen, 'Not found')))

    indices_of_the_same_value = [i for i, x in enumerate([1, 2, 3, 4, 1, 2, 3, 4]) if x == 2]
    print('Indices of the same value: {0}'.format(indices_of_the_same_value))
