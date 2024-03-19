# Hacker_News_Insights
This repository contains a Python project that analyzes sentiment and topics discussed on Hacker News using natural language processing techniques. 

The project employs several techniques and mechanisms to analyze sentiment and topics on Hacker News:

1. **Data Collection**: It fetches the latest posts from Hacker News using its API, extracting key information such as titles, URLs, scores, authors, and timestamps.

2. **Text Preprocessing**: The titles of the posts are preprocessed to remove noise and irrelevant information. This includes lowercasing, removing special characters, and eliminating stopwords.

3. **Sentiment Analysis**: Sentiment analysis is performed on the cleaned titles using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer. This assigns sentiment scores to each title, indicating whether they are positive, negative, or neutral.

4. **Topic Modeling**: Latent Dirichlet Allocation (LDA) topic modeling technique is applied to identify the most prominent topics in the dataset. This categorizes the articles or documents based on their content, allowing for a deeper understanding of the topics discussed on Hacker News.

5. **Visualization**: The project utilizes Dash, a Python framework for building web applications, to create an interactive dashboard. Visualizations such as histograms, bar plots, and sentiment score rankings are included in the dashboard to help users explore sentiment trends and topic distributions among Hacker News posts.

Overall, these techniques and mechanisms enable users to gain insights into the sentiment tendencies and trending topics within the Hacker News community, facilitating a better understanding of the discussions taking place on the platform.
