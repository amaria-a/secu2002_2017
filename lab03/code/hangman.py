
# load secret phrase from file
f = open('secret_phrase.txt','r')
# ignore last character as it's a newline
secret_phrase = f.read()[:-1]

# get letters to guess, characters to keep, initialize ones that are guessed
to_guess = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
to_keep = " ,'-"
guessed = []

# create version to show to user with letters turned to -
shown_phrase = ''
for char in secret_phrase:
    # want to preserve certain characters
    # ternary operator, could do using regular if/else as we do below
    char_to_add = char if char in to_keep else '_'
    shown_phrase = shown_phrase + char_to_add

# now start interacting with users to get them to guess letters
# terminate when they have guessed the phrase
while shown_phrase != secret_phrase:
    text = 'The phrase is\n' + shown_phrase + '\nNow guess a letter: '
    x = raw_input(text)
    # only want users to guess single letters
    while len(x) > 1:
        x = raw_input('Sorry, please guess only a single character: ')
    # also want them guessing only letters
    while x not in to_guess:
        x = raw_input('Sorry, please guess only letters: ')
    # now cast input as lowercase value to be consistent with phrase
    x = x.lower()
    # if the user has guessed letter already there's no point in redoing this
    if x not in guessed:
        # log that the user has guessed the character
        guessed.append(x)
        # now replace in shown_phrase if it's in secret_phrase
        if x in secret_phrase:
            # recreate shown_phrase with replacements in guessed
            new_shown_phrase = ''
            for char in secret_phrase:
                if char in guessed or char in to_keep:
                    new_shown_phrase = new_shown_phrase + char
                else:
                    new_shown_phrase = new_shown_phrase + '_'
            # now replace shown_phrase with updated value
            shown_phrase = new_shown_phrase

print 'Congratulations!  You guessed the phrase in', len(guessed), 'tries.'
