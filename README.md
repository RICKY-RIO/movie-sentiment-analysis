# Movie Sentiment Analysis

This project performs sentiment analysis on movie reviews using machine learning. It classifies movie reviews into two categories: **positive** or **negative**.

## Overview

This project uses a **Logistic Regression** model trained on a dataset of movie reviews. The model is then served through a **FastAPI** backend to predict sentiment for new reviews. 

## Features
- **Model**: A sentiment analysis model trained using `Logistic Regression`.
- **API**: A FastAPI-based web service that accepts a movie review as input and returns the sentiment (positive/negative).
- **Model Training**: The model is trained using movie reviews and saved as a `.pkl` file for use in the API.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/RICKY-RIO/movie-sentiment-analysis.git
