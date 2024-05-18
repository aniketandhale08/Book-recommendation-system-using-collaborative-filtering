# Book Recommendation System Using Collaborative Filtering
## Introduction
This project is a book recommendation system that uses collaborative filtering to suggest books based on user preferences. It includes data processing, model training, and deployment with Docker, GitHub Actions, and Azure Web App. The goal is to help users find books they will enjoy.

![Designer](https://github.com/aniketandhale08/Book-recommendation-system-using-collaborative-filtering/assets/99685171/b8142068-6eac-410b-a8c7-6314a9eeaf41)

## Problem Statement
Readers face an overwhelming number of book choices, making it hard to find titles that match their interests. Traditional browsing is time-consuming and often doesn't cater to individual tastes. There is a need for a personalized and efficient method to discover books.

## Goal
The project's goal is to develop a book recommendation system that:
- Provides personalized book suggestions.
- Streamlines the book discovery process.
- Increases reader engagement.
- Adapts to user feedback.
- Offers an accessible and user-friendly interface.

## Data Description
The dataset includes three CSV files: `books.csv`, `ratings.csv`, and `users.csv`, with a total of 271,360 records. Key features include ISBN, book title, author, publisher, and user ratings.
The dataset is publicly available and can be downloaded here at [Kaggle](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset/data). 

## Data Preprocessing
Steps were taken to preprocess the data:
1. **Data Loading**: Load books, users, and rating data using Pandas.
2. **Data Cleaning and Transformation**:
   - Rename columns for consistency.
   - Handle missing values.
   - Filter out users with fewer than 200 ratings.
3. **Data Merging**: Merge ratings with book details on the ISBN field.
4. **Creating a Pivot Table**: Form a user-book matrix with users as columns, books as rows, and ratings as values.
5. **Handling Sparse Data**: Create a sparse matrix using `csr_matrix` from Scipy.

## Methodology
The project follows these steps:
1. **Data Ingestion**: Divide data into training and test datasets.
2. **Data Preprocessing**: Treat missing values and perform feature engineering.
3. **Model Building**: Train multiple models and select the best based on performance metrics.
4. **Deployment**: Deploy the model using Docker, GitHub Actions for CI/CD, and Azure Web App.

## Conclusion
This project developed a book recommendation system using collaborative filtering, aiming to personalize book suggestions and enhance the reading experience. The system handles data preprocessing, model training, and deployment effectively. Future improvements include refining personalization algorithms and enhancing data quality.

## 12. Licence, Author, & Acknowledgement

[MIT Licence](LICENSE)

**Author:** Aniket Andhale

**Contact:** [LinkedIn](https://www.linkedin.com/in/aniketandhale08/)
