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
If the reader has access to one of the papers, he has a fair idea of the other paper, too. This is extremely useful if one of the papers is open access and the other is behind a paywall. We, at the National Digital Library of India (NDLI), are exploring this aspect to take you as close as possible to paywalled articles and also to increase the reach of your own research. As part of our research, we have used Surrogator to discover open access surrogates of access-restricted papers indexed in NDLI.
If you use our tool, please cite the following papers (especially [A]):

[A] T. Y. S. S. Santosh, Debarshi Kumar Sanyal, Plaban Kumar Bhowmick, and Partha Pratim Das. 2018. Surrogator: A Tool to Enrich a Digital Library with Open Access Surrogate Resources. In Proceedings of ACM/IEEE Joint Conference on Digital Libraries, Poster Track (JCDL’18).

[B] T. Y. S. S. Santosh, Debarshi Kumar Sanyal, and Plaban Kumar Bhowmick. 2018. Surrogator: Enriching a Digital Library with Open Access Surrogate Resources. In ACM India Joint International Conference on Data Sciences and Management of Data, Demo Track (CoDS-COMAD’18).

TOOL DESIGN:
The tool is a Python script with a frontend GUI. Can also be run from commandline in Linux. Tested on Python 3.4 on Ubuntu.
Uses several advanced modules like BeautifulSoup, PyQt4, nltk, selenium, pandas, numpy, gensim.models, and many more. It is highly customizable. Incorporates state-of-the-art machine learning algorithms.


CODE:
We provide 2 versions:

Version 1: This is a simplified script. Corresponds to a Demo at CoDS-COMAD 2018.

 [Input: Keywords, Source; Output: List of results.

 Latest version: 1.11; Tested on: CentOS Linux release 7.3.1611 (Core), Python 3.6 only

 How to run: python3 surrogator__v{version}.py]


Version 2: This is a script with enhanced functionality. Corresponds to poster at JCDL 2018.

[Input: Keywords. Source, Exact match / Near match, Fields to compare (authors/title/abstract), Maximum difference in publication years, Number of pages of Google Scholar to use, how to compare abstracts, how many of Top-K results to return; Output: List of results.

 Latest version: 2.6; Tested on: CentOS Linux release 7.3.1611 (Core), Python 3.6 only; Additional requirements: Download https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz to script directory, Download  https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.simple.zip, unzip and save the folder wiki.sample in script directory, Install Firefox v60, Download geckodriver v0.20.1 to script directory

 How to run: python3 surrogator__v{version}.py]


TESTING:
Results of preliminary evaluation of Surrogator on a sample set of 120 Computer Science and Electrical Engg. papers is provided in EvaluationSurrogatorV2_v1_0.xlsx. It corresponds to a slightly old sub-version of Surrogator v2.


N.B. 
1. The screenshots and XL sheet EvaluationSurrogatorV2_v1_0.xlsx correspond to a slightly old sub-version of Surrogator v2. So the screenshots differ from the interface of Surrogator v2 available in this repository. The results returned by Surrogator depends on NDLI and Google Scholar's output. Therefore, the results you get by running Surrogator may differ from what is reported in the XL sheet.

2. Excessive use of Surrogator might lead to Google Scholar blocking your IP.

3. This tool is a research prototype to test certain ideas. It does not intend to use Google Scholar data or any other data in any unethical manner.

4. The tool is not integrated with NLDI. Therefore, NDLI does not show use the services of this tool in any form.

5. We shall be delighted to receive your feedback, bug reports, bug fixes, change requests and upgrades to the tool.


