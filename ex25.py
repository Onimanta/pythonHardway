import ex25_functions

sentence = "All good things come to those who wait."
words = ex25_functions.break_words(sentence)
print words
sorted_words = ex25_functions.sort_words(words)
print sorted_words
ex25_functions.print_first_word(words)
ex25_functions.print_last_word(words)
print words
ex25_functions.print_first_word(sorted_words)
ex25_functions.print_last_word(sorted_words)
print sorted_words
sorted_words = ex25_functions.sort_sentence(sentence)
print sorted_words
ex25_functions.print_first_and_last(sentence)
ex25_functions.print_first_and_last_sorted(sentence)