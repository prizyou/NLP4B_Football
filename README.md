<p align="center">
    <h1 align="center">Seminar Project: NLP Model for detecting offensive language in Football Comments</h1>
</p>
<p align="center">
  <img src="https://github.com/prizyou/NLP4B_Football/raw/main/Stock_Title_Picture.jpeg" alt="ProjectStockPic">
</p>
<p align="center">
    <em>Unlocking Football Insights! </em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python">
	<img src="https://img.shields.io/badge/License-MIT-orange" alt="License">
<p>
<p align="center">
		<em>Developed with the Software / Tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

##  Quick Links

> - [Overview](#overview)
> - [Project Roadmap](#project-roadmap)
> - [Features](#features)
> - [Repository Structure](#repository-structure)
> - [Getting Started](#getting-started)
>   - [Installation](#installation)
>   - [Running NLP4B_Football](#running-nlp4b_football)
>   - [Tests](#tests)
> - [License](#license)

---

##  Overview

NLP4B_Football is a Natural Language Processing project focused on football data, leveraging functionalities like data cleaning, normalization, and analysis powered by BERT and an Ordinary Logistics Regression Model. It tokenizes emojis into text, enhancing readability, and uses machine learning models for insightful prediction, making football data more accessible and analyzable.

---

##  Project Roadmap

### Preperation Phase

- [X] `► Find Data Sources`
- [X] `► Install Anaconda`
- [X] `► Join the Githup repository`
- [X] `► Collect Ideas for the Project`

### Main Phase

- [X] `► Collect Data from Instagram / Reddit`
- [X] `► Collect Data from Kaggle Datasaet and Clean Data`
- [X] `► Think of how to merge the datasets`
- [X] `► Clean and Label the Data`
- [X] `► Research about BERT`
- [X] `► Implement the BERT Model`
- [X] `► Brainstorm a second Model and implement it`
- [X] `► Study code, pose questions, refine algorithm`
- [X] `► Finish BERT Transformation and generate Outpout`
- [X] `► Perform model validation and conformance checking`
- [X] `► Apply cross validation and overfitting check`
- [X] `► Use the NLP Models on the Youtube Dataset to See weather League or International is more offensive`

### Presentaion Phase

- [X] `► Work on the Project Report parts`
- [X] `► Prepare the Presentaion of the Project`

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture** | This project mainly revolves around NLP tasks using a BERT model and a custom model, with distinct sections for data cleaning, normalization, and making predictions.|
| 🔩 | **Code Quality**  | The code is modular and organized in different directories based on functionality.|
| 📄 | **Documentation** | This README provides an overview of the Project Flow, as well as the [PROJECT REPORT](https://github.com/prizyou/NLP4B_Football/blob/main/Project%20Report.pdf).|
| 🔌 | **Integrations**  | This project pulls data from different sources like Reddit and YouTube.|
| 🧩 | **Modularity**    | Code is structured in different modules based on functionality (Data cleaning, model creation, prediction etc.).|
| ⚡️  | **Performance**  | Both Models perform well with Scores at minimum over 80, up to 96 in all common metrices (Accuracy, Recall, ...).|
| 📦 | **Dependencies**  | Major dependencies include Python, Jupyter Notebooks, and various NLP Python libraries for BERT and the custom model.|


---

##  Repository Structure

```sh
└── NLP4B_Football/
    │
    │
    ├── BERT_model
    │   │
    │   ├── data_normalization.py
    │   ├── labeled_data.xlsx
    │   ├── labeled_normalized_data.csv
    │   └── model.ipynb
    │
    │
    ├── Own_model
    │   │
    │   ├── model creation
    │   │   ├── complete_dataset.csv
    │   │   ├── logreg_model.pkl
    │   │   ├── own_model_creation.ipynb
    │   │   ├── pred_youtube_cleaned_for_label.xlsx
    │   │   ├── vectorizer.pkl
    │   │   └── youtube_cleaned_for_label_NEW.xlsx
    │   │
    │   └── model_prediction
    │       ├── logreg_model.pkl
    │       ├── own_model_prediction.ipynb
    │       └── vectorizer.pkl
    │
    │
    ├── README.md
    ├── LICENSE
    ├── Stock_Title_Picture.jpeg
    │
    │
    ├── data_cleaning
    │   │
    │   ├── clean_not_labeled_data
    │   │   ├── convert.ipynb
    │   │   ├── reddit_clean_not_labeled.csv
    │   │   ├── reddit_clean_not_labeled.xlsx
    │   │   ├── reddit_cleaned_for_label.xlsx
    │   │   └── reddit_cleaning.py
    │   │
    │   ├── kaggle
    │   │   ├── Kaggle_clean_and_labeled.xlsx
    │   │   ├── convert.py
    │   │   ├── kaggle_clean_and_labeled.csv
    │   │   └── kaggle_cleaning.py
    │   │
    │   ├── reddit
    │   │   ├── reddit_cleaned_for_label_NEW.xlsx
    │   │   └── reddit_cleaning.ipynb
    │   │
    │   └── youtube
    │       ├── youtube_cleaned_for_label.xlsx
    │       ├── youtube_cleaned_for_label_NEW.xlsx
    │       └── yt_cleaning.ipynb
    │
    │
    ├── main
    │   └── main.ipynb
    │
    │
    ├── data_analysis
    │   ├── complete_dataset.csv
    │   ├── complete_dataset.xlsx
    │   └── dataset_analysis.ipynb
    │
    │
    └── web_scraping
        │
        ├── NOT_USED
        │   │
        │   ├── facebook_OUT
        │   │   ├── __pycache__
        │   │   │   └── secrets.cpython-310.pyc
        │   │   ├── facebook_scrape.ipynb
        │   │   ├── new_facebook_scraper.ipynb
        │   │   └── secrets.py
        │   │
        │   ├── instagram_OUT
        │   │   └── insta_scrape.py
        │   │
        │   └── reddit_OUT
        │       ├── r_football_Paul.csv
        │       ├── redditScrape_Ali.ipynb
        │       └── reddit_api_Paul.ipynb
        │
        │
        ├── reddit
        │   ├── Reddit_IDs.txt
        │   ├── pw.txt
        │   ├── redditComments_Ali.csv
        │   ├── redditComments_NEW.csv
        │   └── scraping.ipynb
        │
	│
        └── youtube
            ├── dataScrapeFromYoutube.ipynb
            ├── videos_used.txt
            ├── yt_comments.csv
            └── yt_comments_new.csv
```

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **JupyterNotebook**: `version x.y.z`

###  Installation

1. Clone the NLP4B_Football repository:

```sh
git clone https://github.com/prizyou/NLP4B_Football
```

2. Change to the project directory:

```sh
cd NLP4B_Football
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running NLP4B_Football

Use the following command to run NLP4B_Football:

```sh
jupyter nbconvert --execute notebook.ipynb
```

###  Tests

To execute tests, run:

```sh
pytest notebook_test.py
```

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/prizyou/NLP4B_Football/blob/main/LICENSE) file.
