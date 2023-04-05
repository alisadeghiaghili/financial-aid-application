# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:11:22 2023

@author: sadeghi.a
"""
import re
import nltk
from nltk.corpus import wordnet

def replace_synonyms(text):
    # Define a function to replace each word in the text with a random synonym
    def replace_word_with_synonym(word):
        # Get the synonyms for the word
        synonyms = wordnet.synsets(word)
        if synonyms:
            # Get the synonyms for the first definition of the word
            synonyms = synonyms[0].lemmas()
            if synonyms:
                # Get a random synonym and replace the word with it
                synonym = synonyms[0].name()
                return synonym.replace('_', ' ')
        return word
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Replace each word with a synonym
    words = [replace_word_with_synonym(word) for word in words]
    
    # Join the words back into a string
    text = ' '.join(words)
    
    return text

field = input('Enter the field name: ')
courseName = input('Enter the course name: ')
instituteName = input('Enter the institute name: ')
print()
print()

part1 = r"I am a student from a developing country keen on learning about, {field}. \
    Since the quality of education in our college is not up to the mark, \
    the only way to get a viable career option in the future for me is to \
    take this course. Since I am a student and our college does not permit \
    part-time jobs, I would not be able to carry the expenses to pay for the \
    certificate of this course. Financial Aid will help me take this course \
    without any adverse impact on my monthly essential needs. I am really \
    excited about this course since it provides me with a great opportunity \
    to grow my skills and become a professional as I graduate in the same \
    or prospective fields with a great resume. Coursera has been a great \
    platform among my peers and following them I am very excited to take my \
    course here!". format(field = replace_synonyms(field))
    
print(re.sub(pattern = r'\\|\n|\s{2,}', repl = '', string = part1))
print("===========================================================")

part2 = r"{field} is being in high demand, I want to complete the \
    {courseName} Course at the {instituteName}. This course will boost my job prospects \
    after graduation from my institute. It will help me perform better in \
    carrying out {field} and give me an edge over my competitors. A \
    verified certificate will attach credibility to the certificate I receive \
    from this course. I plan to complete all assignments on or before time as \
    I have done in previous Signature Track Courses. As written above, \
    Coursera has been not only suggested by my student peers but also our \
    college faculty, and so following their prestigious advice, I would be \
    glad to gain more knowledge and hone my skills with this course. Also, I \
    intend to participate in Discussion Forums, which I think will supplement \
    my learning. I also plan to grade assignments that are peer-reviewed \
    which I believe will be an invaluable learning opportunity.". format(field = replace_synonyms(field.lower()), courseName = replace_synonyms(courseName), instituteName = replace_synonyms(instituteName))
    
print(re.sub(pattern = r'\\|\n|\s{2,}', repl = '', string = part2))
