import string

# Global Variables
words = []
total_words = 0
unique_words = 0
stopwords = set([
    "a", "an", "the", "and", "or", "but", "if", "then", "else", "for", "to", "of", "in", "on", "at", "by", "with", "about", 
    "as", "from", "into", "over", "after", "before", "between", "under", "above", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "doing", "have", "has", "had", "having", "can", "could", "shall", "should", "will", "would",
    "may", "might", "must", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "her", "its", "our", "their", 
    "mine", "yours", "hers", "ours", "theirs", "use", "through", "also", "many", "these", "however", "without", "another", "which"
])
bigrams = []

# Functions
def mian_menu():
    options = ["View Corpus Statistics", "Top-N Most Frequent Words", "Search Word Frequency", "Predict Next Word", "Exit"]

    while True:
        print("======== Mini-NLP Corpus Analyzer ========")
        if(total_words == 0):
            load_file()
        
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input(f"Enter your choice (1-{len(options)}): ")
        if choice == "1":
            view_corpus_statistics()
        elif choice == "2":
            n = get_valid_option("Enter the value of N for Top-N Most Frequent Words (0 to cancel): ", int, None, 0, total_words)
            if n == 0:
                print("Cancelled. Returning to main menu.")
                continue
            s = get_valid_option("Filter stop-words? (y/n):  ", str, ["y", "n"])
            display_top_n_words(n, s == "y")
        elif choice == "3":
            word = get_valid_option("Enter the word to search for its frequency (or type '0' to return): ", str)
            if word == "0":
                print("Cancelled. Returning to main menu.")
                continue
            search_word_frequency(word)
        elif choice == "4":
            word = get_valid_option("Enter the word to predict the next word (or type '0' to return): ", str)
            if word == "0":
                print("Cancelled. Returning to main menu.")
                continue
            predict_next_word(word)
        elif choice == "5":
            print("Exit")
            break
        else:
           print("Invalid choice. Please try again.")     
            
def load_file():
    try:
        path = "sample.txt"
        with open(path, "r", encoding="utf-8") as file:
            file_content = file.read().lower().strip()
            file_content = file_content.translate(str.maketrans("", "", string.punctuation)) # Remove punctuation
        global words, total_words, unique_words, bigrams
        words = file_content.split()
        bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
        total_words = len(words)
        unique_words = len(set(words))
        print(f"Loaded '{path}' ({total_words} total words).")
    except (FileNotFoundError):
        with open("sample.txt", "w") as file:
            file.close()

def view_corpus_statistics():
    if total_words == 0:
        print("Corpus is empty! Please add text to 'sample.txt' first.")
        return
    
    print("======== Corpus Statistics ========")
    print(f"Total Words: {total_words}")
    print(f"Unique Vocabulary: {unique_words}")
    print(f"Average Word Length: {sum(len(word) for word in words) / total_words:.2f}")
    print(f"Lexical Diversity: {unique_words / total_words:.2f} ({(unique_words / total_words) * 100:.2f}% variety)")
    print("-----------------------------------")
    goto_main_menu()

def display_top_n_words(n, filter_stopwords=False):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    if filter_stopwords:
        sorted_words = [word for word in sorted_words if word[0] not in stopwords]
    print("-----------------------------------")
    print(f"Top {n} Most Frequent Words:")
    for i in range(min(n, len(sorted_words))):
        print(f"{i+1}. {sorted_words[i][0]} - {sorted_words[i][1]} occurrences ({(sorted_words[i][1] / total_words) * 100:.2f}%)")
    print("-----------------------------------")
    goto_main_menu()

def search_word_frequency(word):
    if total_words == 0:
        print("Corpus is empty! Please add text to 'sample.txt' first.")
        return
    frequency = words.count(word.lower())
    print(f"The word '{word}' appears {frequency} times in the corpus.")
    goto_main_menu()

def predict_next_word(word):
    if total_words == 0:
        print("Corpus is empty! Please add text to 'sample.txt' first.")
        return
    next_words = [bigram[1] for bigram in bigrams if bigram[0] == word.lower()]
    if next_words:
        most_common_word = max(set(next_words), key=next_words.count)
        print(f"Most likely next word after '{word}' is '{most_common_word}' (appeared {next_words.count(most_common_word)} times after '{word}')")
    else:
        print(f"No prediction available for '{word}'.")
    goto_main_menu()

# Helper Functions
def get_valid_option(prompt, input_type=str, valid_options=None, minValue=None, maxValue=None):
    while True:
        user_input = input(prompt)
        try:
            user_input = input_type(user_input)
            if valid_options and user_input not in valid_options:
                print(f"Error: Please enter one of the following options: {valid_options}")
                continue
            if minValue is not None or maxValue is not None:
                if not check_limit(user_input, minValue, maxValue):
                    continue
            return user_input
        except ValueError:
            print(f"Error: Please enter a valid {input_type.__name__}.")


def check_limit(value, minimum=None, maximum=None):
    if not isinstance(value, (int, float)):
        print("Error: Value must be a number.")
        return False
    if minimum is not None and value < minimum:
        print(f"Error: Minimum value is {minimum}.")
        return False
    if maximum is not None and value > maximum:
        print(f"Error: Maximum value is {maximum}.")
        return False
    return True

def goto_main_menu():
    input("\nPress Enter to return to the main menu...")

# Main Program
mian_menu()
        
    