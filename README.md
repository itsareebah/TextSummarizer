# Text Summarization Tool
## Overview

This project is a text summarization tool implemented in Python, leveraging Natural Language Processing (NLP) techniques to generate concise and informative summaries from input documents. The tool employs algorithms such as cosine similarity and PageRank to rank sentences and select the most important ones for the summary.

## Features
Summarizes text documents to generate concise summaries.
Considers line and paragraph breaks for accurate summarization.
Prioritizes informative sentences based on importance score and length.
Supports customization of the number of sentences in the summary.
## Requirements
Python 3.x
NLTK (Natural Language Toolkit)
NetworkX
Installation

Clone the repository:
```bash 
git clone https://github.com/itsareebah/TextSummarizer.git
```
Usage
Place your text document (e.g., input.txt) in the project directory.
Run the following command to generate a summary:
bash
Copy code
```python
python summarize.py
```
Examples
For input text:

```
The importance of regular exercise cannot be overstated. Exercise has numerous benefits for both physical and mental health.
 It can help reduce the risk of chronic diseases such as heart disease, diabetes, and certain types of cancer. 
Additionally, exercise can improve mood and reduce symptoms of anxiety and depression. It's recommended that 
adults aim for at least 150 minutes of moderate-intensity exercise per week, such as brisk walking or 
cycling. However, even small amounts of exercise can provide health benefits, so 
finding activities that you enjoy and incorporating them into your routine is key.
```

Output summary:
```
Additionally, exercise can improve mood and reduce symptoms of anxiety and depression.
The importance of regular exercise cannot be overstated.
Exercise has numerous benefits for both physical and mental health.
```
## Acknowledgements
This project utilizes the NLTK and NetworkX libraries for text processing and graph-based algorithms.
