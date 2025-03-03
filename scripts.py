import os
import re
import socket
from collections import Counter

#defining the file paths
file1  = "/home/data/IF-1.txt"
file2 = "/home/data/AlwaysRememberUsThisWay-1.txt"
output_path = "/home/data/ouptput/result.txt" #the file path for the results 

os.makedirs(os.path.dirname(output_path), exist_ok=True)

#Checking if the file exists
if not os.path.exists(file1) or not os.path.exists(file2):
	print("Error: one or both text files do not exist in path given.")
	exit(1)

# Function to handle contractions like won't, don't 
def handle_contractions(text):
    contractions = {
        "I'm": "I am", "can't": "cannot", "won't": "will not", "don't": "do not",
        "isn't": "is not", "aren't": "are not", "I've": "I have", "you've": "you have",
        "he's": "he is", "she's": "she is", "it's": "it is", "they're": "they are",
        "what's": "what is", "where's": "where is", "who's": "who is"
    }
    # Replace contractions with full form (ex: can't can not, etc.)
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text

# Function to count words and find top 3 frequent words 
def count_words(file_path, handle_contractions_flag=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Convert to lowercase letters
        if handle_contractions_flag:
            text = handle_contractions(text)  # Handle contractions
    # removing characters for exmaple like whitespace
        words = re.findall(r'\b\w+\b', text)  # Find words 
        word_count = len(words)  # Count total words
        word_frequencies = Counter(words)  # Count word frequencies
        top_words = word_frequencies.most_common(3)  # Get top 3 frequent words
    return word_count, top_words

# Count words and get top words for both of the text files
try:
    word_count1, top_words1 = count_words(file1)
    word_count2, top_words2 = count_words(file2, handle_contractions_flag=True)

    # Calculate total words across both text files
    total_word_count = word_count1 + word_count2

    # Get the IP address of the container
    ip_address = socket.gethostbyname(socket.gethostname())

    # Prepare the results
    results = f"""
    === Results ===

    Total words in IF-1.txt: {word_count1}
    Top 3 words in IF-1.txt: {top_words1}

    Total words in AlwaysRememberUsThisWay-1.txt: {word_count2}
    Top 3 words in AlwaysRememberUsThisWay-1.txt: {top_words2}

    Grand total words across both files: {total_word_count}

    IP Address of the container: {ip_address}
    """

    # Write results to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(results)

    # Print the result file content to the console
    with open(output_path, 'r', encoding='utf-8') as output_file:
        print(output_file.read())

		
except Exception as e:
	print(f"Error processing files: {e}")
