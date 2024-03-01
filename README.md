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

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running NLP4B_Football](#-running-NLP4B_Football)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

NLP4B_Football is a Natural Language Processing project focused on football data, leveraging functionalities like data cleaning, normalization, and analysis powered by BERT and an Ordinary Logistics Regression Model. It tokenizes emojis into text, enhancing readability, and uses machine learning models for insightful prediction, making football data more accessible and analyzable.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | This project mainly revolves around NLP tasks using a BERT model and a custom model, with distinct sections for data cleaning, normalization, and making predictions.|
| 🔩 | **Code Quality**  | The code appears to be modular and organized in different directories based on functionality, but there might be improvement areas in naming conventions and comments.|
| 📄 | **Documentation** | While specific details are mentioned in the file descriptors, detailed inline code explanations or a comprehensive README file are missing.|
| 🔌 | **Integrations**  | This project pulls data from different sources like Reddit and YouTube for cleaning and processing.|
| 🧩 | **Modularity**    | Code appears to be structured in different modules based on functionality (Data cleaning, model creation, prediction).|
| 🧪 | **Testing**       | No testing frameworks evident from the provided data. The project might benefit from unit or functionality tests.|
| ⚡️  | **Performance**   | Without metrics it's hard to assess, but usage of normalization and a pre-trained BERT model suggest optimized processing.|
| 🛡️ | **Security**      | Security aspects not visible in the provided detail. Data handling procedures should be assessed.|
| 📦 | **Dependencies**  | Major dependencies include Python, Jupyter Notebooks, and likely various NLP Python libraries for BERT and custom models.|


---

##  Repository Structure

```sh
└── NLP4B_Football/
    ├── BERT_model
    │   ├── data_normalization.py
    │   ├── labeled_data.xlsx
    │   ├── labeled_normalized_data.csv
    │   └── model.ipynb
    ├── Own_model
    │   ├── model creation
    │   │   ├── complete_dataset.csv
    │   │   ├── logreg_model.pkl
    │   │   ├── own_model _creation.ipynb
    │   │   ├── pred_youtube_cleaned_for_label.xlsx
    │   │   ├── vectorizer.pkl
    │   │   └── youtube_cleaned_for_label_NEW.xlsx
    │   └── model_prediction
    │       ├── logreg_model.pkl
    │       ├── own_model_prediction.ipynb
    │       └── vectorizer.pkl
    ├── README.md
    ├── data_cleaning
    │   ├── clean_not_labeled_data
    │   │   ├── convert.ipynb
    │   │   ├── reddit_clean_not_labeled.csv
    │   │   ├── reddit_clean_not_labeled.xlsx
    │   │   ├── reddit_cleaned_for_label.xlsx
    │   │   └── reddit_cleaning.py
    │   ├── kaggle
    │   │   ├── Kaggle_clean_and_labeled.xlsx
    │   │   ├── convert.py
    │   │   ├── kaggle_clean_and_labeled.csv
    │   │   └── kaggle_cleaning.py
    │   ├── reddit
    │   │   ├── reddit_cleaned_for_label_NEW.xlsx
    │   │   └── reddit_cleaning.ipynb
    │   └── youtube
    │       ├── youtube_cleaned_for_label.xlsx
    │       ├── youtube_cleaned_for_label_NEW.xlsx
    │       └── yt_cleaning.ipynb
    ├── main
    │   └── main.ipynb
    └── web_scraping
        ├── NOT_USED
        │   ├── facebook_OUT
        │   │   ├── __pycache__
        │   │   │   └── secrets.cpython-310.pyc
        │   │   ├── facebook_scrape.ipynb
        │   │   ├── new_facebook_scraper.ipynb
        │   │   └── secrets.py
        │   ├── instagram_OUT
        │   │   └── insta_scrape.py
        │   └── reddit_OUT
        │       ├── r_football_Paul.csv
        │       ├── redditScrape_Ali.ipynb
        │       └── reddit_api_Paul.ipynb
        ├── data_analysis
        │   ├── complete_dataset.csv
        │   ├── complete_dataset.xlsx
        │   └── dataset_analysis.ipynb
        ├── reddit
        │   ├── Reddit_IDs.txt
        │   ├── pw.txt
        │   ├── redditComments_Ali.csv
        │   ├── redditComments_NEW.csv
        │   └── scraping.ipynb
        └── youtube
            ├── dataScrapeFromYoutube.ipynb
            ├── videos_used.txt
            ├── yt_comments.csv
            └── yt_comments_new.csv
```

---

##  Modules

<details closed><summary>main</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [main.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/main/main.ipynb) | The main.ipynb notebook, located at the root within the main directory, serves as the central execution point in the NLP4B_Football repository. It likely orchestrates different modules of the repository including data cleaning, web scraping, and Natural Language Processing model operations. However, without specific function calls or operations, it's hard to determine its particular role in the repository. |

</details>

<details closed><summary>BERT_model</summary>

| File                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                              |
| [model.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/BERT_model/model.ipynb)                     | This code snippet is part of the BERT_model within the NLP4B_Football repository. It plays a significant role in natural language processing tasks, taking care of data normalization and managing labeled data, both crucial for efficient model training and prediction in the football context.                                               |
| [data_normalization.py](https://github.com/prizyou/NLP4B_Football/blob/master/BERT_model/data_normalization.py) | The data_normalization.py script in BERT_model directory is utilized for preprocessing the football-related dataset. Primarily, it reads the labeled data from an Excel file and performs demojization-converting emoji into textual representation. The cleaned data is then saved as a CSV file, ready for further analysis or model training. |

</details>

<details closed><summary>data_cleaning.clean_not_labeled_data</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                  |
| [convert.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/data_cleaning/clean_not_labeled_data/convert.ipynb)           | This codebase is for a natural language processing project around football using two distinct models: BERT and a custom model. It handles data normalization, model creation, and predictions. Additionally, it manages cleaning of non-labeled data. The custom model employs logistic regression and text vectorization.                                                                           |
| [reddit_cleaning.py](https://github.com/prizyou/NLP4B_Football/blob/master/data_cleaning/clean_not_labeled_data/reddit_cleaning.py) | This section pertains to the structuring of a Natural Language Processing model for analyzing football-related data. One part utilizes a pre-trained BERT model for data normalization and pattern recognition, while another contains a custom-built model for generating predictions. Furthermore, a section is dedicated to cleaning unlabeled data from various sources like Reddit and YouTube. |

</details>

<details closed><summary>data_cleaning.kaggle</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                 | ---                                                                                                                                                                                                                                                                                                |
| [convert.py](https://github.com/prizyou/NLP4B_Football/blob/master/data_cleaning/kaggle/convert.py)                 | This `convert.py` script belongs to the data cleaning section of the NLP4B_Football project. It primarily focuses on converting an Excel file containing cleaned and labeled data from Kaggle into a CSV file, augmenting the project's flexibility in processing diverse data formats.            |
| [kaggle_cleaning.py](https://github.com/prizyou/NLP4B_Football/blob/master/data_cleaning/kaggle/kaggle_cleaning.py) | This repository contains Natural Language Processing models for a football analytics project. The BERT and custom models process, normalize, and cleanse football-related data. The clean dataset is used to train the models, which then predict labels for YouTube and Reddit football comments. |

</details>

<details closed><summary>data_cleaning.youtube</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [yt_cleaning.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/data_cleaning/youtube/yt_cleaning.ipynb) | The code contained in this repository is primarily dedicated to developing and applying Natural Language Processing models for analyzing football related content. Within the BERT_model directory, the script prepares labeled data for the BERT model, which is trained in the model notebook. The Own_model directory houses scripts for creating a separate model, using a cleaned dataset, and making predictions with it. |

</details>

<details closed><summary>data_cleaning.reddit</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [reddit_cleaning.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/data_cleaning/reddit/reddit_cleaning.ipynb) | This code is a key part of the NLP4B_Football repository, which focuses on natural language processing tasks in football-related data. The primary function of this code is to manage and facilitate data normalization, model creation, and predictions using two different models: a BERT model and a custom model. Also, emphasis is put on data cleaning operations, continuing up to labeling and normalization for subsequent use in prediction and modeling. |

</details>

<details closed><summary>Own_model.model_prediction</summary>

| File                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                   |
| [own_model_prediction.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/Own_model/model_prediction/own_model_prediction.ipynb) | The code snippet is part of the NLP4B_Football repository, specifically from BERT_model or Own_model. It processes data like normalization, labeling, and modeling, which aids in football-related natural language processing tasks. The repository invokes machine learning techniques to gain insights from football-related data. |

</details>

<details closed><summary>Own_model.model creation</summary>

| File                                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                      |
| [own_model _creation.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/Own_model/model creation/own_model _creation.ipynb) | This code is part of the NLP4B_Football repository's BERT_model component where it conducts the important task of data normalization. The process refines the labeled_data.xlsx file, preparing it for further stages within the machine learning pipeline. The normalization plays a crucial role in enabling efficient model training. |

</details>

<details closed><summary>web_scraping.NOT_USED.instagram_OUT</summary>

| File                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                        |
| [insta_scrape.py](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/NOT_USED/instagram_OUT/insta_scrape.py) | This codebase is related to an NLP (Natural Language Processing) project aimed at football-related text classification. It contains two models, a BERT based model for data normalization and text classification, and a custom model for predicting football event labels. There is also a data cleaning module to preprocess unlabeled data from Reddit. |

</details>

<details closed><summary>web_scraping.NOT_USED.facebook_OUT</summary>

| File                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [new_facebook_scraper.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/NOT_USED/facebook_OUT/new_facebook_scraper.ipynb) | This code repository holds an NLP (Natural Language Processing) application designed for football-related data. It majorly consists of two sections: a BERT model module and another created in-house. These modules include normalization, model creation and prediction scripts. Data cleaning is also included facilitating pre-formatting for text input. Primary objective is to transform conversational data into structured data.           |
| [secrets.py](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/NOT_USED/facebook_OUT/secrets.py)                                 | The `secrets.py` script stored in the `facebook_OUT` directory under `web_scraping/NOT_USED` is used for credential management. It securely stores the username and password credentials, utilized when accessing Facebook for web scraping processes. The script helps maintain confidentiality and manage authentications, which are vital for the repository's data scraping architecture.                                                       |
| [facebook_scrape.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/NOT_USED/facebook_OUT/facebook_scrape.ipynb)           | This codebase is part of the NLP4B_Football project that uses natural language processing to analyze football-related discussions. Two distinct models are present: a BERT model for data normalization and sentiment prediction, and a custom Logistic Regression model for text classification. The structure also includes scripts for data cleaning and preprocessing, illustrating the project's robustness in handling diverse, raw datasets. |

</details>

<details closed><summary>web_scraping.NOT_USED.reddit_OUT</summary>

| File                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [reddit_api_Paul.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/NOT_USED/reddit_OUT/reddit_api_Paul.ipynb)   | This codebase is intended for Natural Language Processing (NLP) within a football context. The core feature is a BERT model which normalizes and learns from labeled football data. The repository also includes a custom model creation and prediction mechanism that utilizes logistic regression, facilitated by the necessary stored datasets and Pickle objects.                                                  |
| [redditScrape_Ali.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/NOT_USED/reddit_OUT/redditScrape_Ali.ipynb) | This repository is a part of the NLP4B_Football project. It contains different models, such as BERT and a custom model, trained on normalized and labeled football-related data. The data used for training and predictions are cleaned and sourced from various platforms including YouTube, Reddit, and Kaggle as part of the data cleaning and web scraping modules. There's also a provision for dataset analysis. |

</details>

<details closed><summary>web_scraping.data_analysis</summary>

| File                                                                                                                              | Summary                                                                                                                                                                                                                         |
| ---                                                                                                                               | ---                                                                                                                                                                                                                             |
| [dataset_analysis.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/data_analysis/dataset_analysis.ipynb) | This code snippet primarily defines the structure and foundation of the repository. It sets up key elements, which shape the functional architecture and data organization, providing a backbone for the software's operations. |

</details>

<details closed><summary>web_scraping.youtube</summary>

| File                                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                               |
| [videos_used.txt](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/youtube/videos_used.txt)                         | The code principally contributes to the NLP4B_Football project's text analysis operation. It incorporates two main parts: the BERT_model, which normalizes data and applies a pre-trained BERT model for predictions; and the Own_model, where a custom predictive model is developed and used. It collectively aids in text classification and sentiment analysis for football-related discourse.                |
| [dataScrapeFromYoutube.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/youtube/dataScrapeFromYoutube.ipynb) | This codebase forms part of a Natural Language Processing application targeting football-related text. It contains code for two models-a customized model and a BERT model. Each model has components for data normalization, model creation, and prediction. The models use machine learning to interpret and categorize football text data. Also, the repository includes data cleaning and labeling utilities. |

</details>

<details closed><summary>web_scraping.reddit</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pw.txt](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/reddit/pw.txt)                 | The pw.txt file located in the web_scraping/reddit directory stores the password used for authenticating and authorizing the scraping operations on Reddit. This file's secret key plays a critical role in facilitating data extraction to generate the dataset required for the machine learning models in the repository.                                                                                                                                                                      |
| [Reddit_IDs.txt](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/reddit/Reddit_IDs.txt) | This file, Reddit_IDs.txt, located within the web_scraping/reddit directory, contains identifiers of football-related Reddit posts. It supports the operation of web scraping by specifying the source posts to retrieve data for the NLP model.                                                                                                                                                                                                                                                  |
| [scraping.ipynb](https://github.com/prizyou/NLP4B_Football/blob/master/web_scraping/reddit/scraping.ipynb) | This codebase focuses on Natural Language Processing (NLP) for football commentary, featuring two separate models-a BERT model and a proprietary model. The BERT model normalizes football-related data while the proprietary model enables learning, predicting, and labeling YouTube comments. The implementation oscillates between data cleaning, data normalization, model creation, and model prediction, resulting in a curated, classified dataset that can be used for further analyses. |

</details>

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
- [X] `► Implement the Machine Learning Algorithm`
- [X] `► Brainstorm a possible second Machine Learning Algorithm that we can use`
- [X] `► Study code, pose questions, refine algorithm`
- [X] `► Finish BERT Transformation and generate Outpout`
- [X] `► Perform model validation and conformance checking`
- [X] `► Apply cross validation and overfitting check`
- [X] `► Use the NLP Models on the Youtube Dataset to See weather League or International is more offensive`

### Presentaion Phase

- [X] `► Work on the Project Report parts`
- [X] `► Prepare the Presentaion of the Project`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/prizyou/NLP4B_Football/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/prizyou/NLP4B_Football/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/prizyou/NLP4B_Football/issues)**: Submit bugs found or log feature requests for Nlp4b_football.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/prizyou/NLP4B_Football
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/prizyou/NLP4B_Football/blob/main/LICENSE) file.

---

[**Return**](#-quick-links)

---
