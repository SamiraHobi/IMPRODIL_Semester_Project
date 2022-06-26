COMPARISON OF SLANG TERM FREQUENCY

Compare the frequency of slang-terms across different corpora.


1. Introduction

According to Kidd et al. (2016), the use of Australian slang is an important marker of identity
construction among Australians.

This program lets you compare two corpora in terms of how many slang-terms they contain. It will tell you the total 
number of slang-terms as well as the number of unique terms.


2. Usage

If you have one corpus and one list of slang terms, eg. 'ABCE1-plain.txt' as a corpus and 'slang.txt' as the slang list
you can get a list of slang-terms along with their frequency as follows:

    python3 main.py Data/ABCE1-plain.txt Data/slang.txt


Use the '--corpus2' optional flag to read in a second corpus and compare it to the first one.
    
    python3 main.py Data/ABCE1-plain.txt Data/slang.txt --corpus2 Data/ABCNE2-plain.txt



The program requires spaCy (https://spacy.io) for tokenisation. It can be downloaded by running

    python -m spacy download en_core_news_sm


3. Data

The 'Data' directory contains two corpora taken from the 'Australian Radio Talkback' corpus which contains transcripts
of radio interviews. They are available at https://www.ausnc.org.au

Furthermore, there is a slang.txt file which contains a collection of slang-terms which were taken from 
https://www.studiesinaustralia.com/studying-in-australia/living-in-australia/aussie-slang


5. References

Kidd, E., Kemp, N., Kashima, E. S., & Quinn, S. (2016). 
Language, Culture, and Group Membership: An Investigation Into the Social Effects of Colloquial Australian English. 
Journal of Cross-Cultural Psychology, 47(5), 713–733.

