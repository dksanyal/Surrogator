# Surrogator
Discover open access surrogates of paywalled research papers

Surrogator is a tool to automatically identify open access surrogates for research papers.
We call a collection of research papers written by the same author(s) (or research group) as surrogates for each other if they are very closely related in content.
 
EXAMPLES: 
A conference paper and its extension published in a journal could be treated as surrogates. 

In the following, [1A] and [1B] form an example of surrogates:

[1A] Maity, Mukulika, Bhaskaran Raman, and Mythili Vutukuru. "Tcp download performance in dense wifi scenarios." Communication Systems and Networks (COMSNETS), 2015 7th International Conference on. IEEE, 2015.

[1B] Maity, Mukulika, Bhaskaran Raman, and Mythili Vutukuru. "TCP Download Performance in Dense WiFi Scenarios: Analysis and Solution." IEEE Transactions on Mobile Computing 16.1 (2017): 213-227.

Similarly a technical report could be a surrogate for a conference publication.

UTILITY:
If the reader has access to one of the papers, he has a fair idea of the other paper, too. This is extremely useful if one of the papers is open access and the other is behind a paywall. We, at the National Digital Library of India (NDLI), are using this aspect to take you as close as possible to paywalled articles and also to increase the reach of your own research. We have used Surrogator to discover open access surrogates of access-restricted papers indexed in NDLI.

TOOL DESIGN:
The tool is a Python script with a frontend GUI. Can also be run from commandline in Linux. Tested on Python 3.4 on Ubuntu.
Uses several advanced modules like BeautifulSoup, PyQt4, nltk, selenium, pandas, numpy, gensim.models, and many more. It is highly customizable. Incorporates state-of-the-art machine learning algorithms.

TESTING:
Results of preliminary evaluation of Surrogator on a sample set of 120 Computer Science and Electrical Engg. papers is provided in EvaluationSurrogatorV2_v1_0.xlsx. 

CODE:
We provide 2 versions:

Version 1: This is a simplified script. Corresponds to a Demo at CoDS-COMAD 2018.

[Input: Keywords, Source; Output: List of results; How to run: python3.6 surrogator__v1_11.py] 

[Latest version: 1.11; Tested on: CentOS Linux release 7.3.1611 (Core), Python 3.6 only]


Version 2: This is a script with enhanced functionality. Corresponds to poster at JCDL 2018.

[Input: Keywords. Source, Exact match / Near match, Fields to compare (authors/title/abstract), Maximum difference in publication years, Number of pages of Google Scholar to use, how to compare abstracts, how many of Top-K results to return; Output: List of results; How to run: How to run: python3.6 surrogator__v2_3.py]

[Latest version: 2.6; Tested on: CentOS Linux release 7.3.1611 (Core), Python 3.6 only; Additional requirements: Download https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz to script directory, download  https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.simple.zip, unzip and save the folder wiki.sample in script directory, Firefox 60, geckodriver v0.20.1]

