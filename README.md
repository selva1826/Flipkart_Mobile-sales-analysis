# Flipkart Mobile sales analysis

## Overview

This repository contains the analysis of mobile phone data from Flipkart. The goal of this project is to uncover consumer preferences and market trends, providing valuable insights for sellers on the platform.

## Project Summary

### Business Problem

A hypothetical business challenge was posed: an authorized Flipkart seller wants to know the best product, brand, specifications, and deals to maximize profits with minimal investment. The following key questions were addressed:
1. Should the seller focus on products from a single brand or multiple brands?
2. What insights and relationships can be discovered through exploratory data analysis (EDA) and data visualization?
3. A thorough examination of each brand's performance and customer preferences.

### Data Collection

Data was extracted from the Flipkart website via web scraping on September 14, 2021. The dataset contains 3114 samples with the following attributes:
- **Brand**: Name of the mobile manufacturer
- **Model**: Model number of the mobile phone
- **Color**: Color of the model
- **Memory**: RAM of the model (4GB, 6GB, 8GB, etc.)
- **Storage**: ROM of the model (32GB, 64GB, 128GB, 256GB, etc.)
- **Rating**: Customer rating of the model (out of 5)
- **Selling Price**: Discounted price of the model in INR
- **Original Price**: Actual price of the model in INR

### Key Insights

1. **Color Preferences**:
   - Black mobiles are the most popular due to their classic and versatile appeal.
   - Gold mobiles are also popular, conveying a sense of luxury and premium quality.
   - Rose gold, midnight black, and gray are less popular colors.

2. **Memory and Storage Preferences**:
   - 4GB RAM variants are highly popular due to their balance of performance and cost.
   - 64GB and 128GB storage options are common for their practicality and value.
   - Very low storage capacities, such as 140MB, are outdated and less preferred.

3. **Brand Performance**:
   - Samsung has the highest number of models available on Flipkart, catering to various price points and user preferences.
   - Brands like Apple, Samsung, and realme have a high proportion of models with ratings above 4.0, indicating strong customer satisfaction.
   - Google Pixel models have consistently received high ratings due to their reliability and alignment with the latest trends.

4. **Price Categories**:
   - Mid-range mobiles (10K-30K INR) dominate the market across various brands.
   - Highly-rated mobiles are often found in this price range, challenging the notion that only premium-priced models receive high ratings.

5. **Special Trends**:
   - Higher-rated mobiles are not always premium or expensive. Many highly-rated models fall within the affordable 10K-30K INR price range.
   - Quality over quantity is evident as brands like iQOO and Google Pixel, with fewer models, achieve high ratings consistently.

### Conclusion

The analysis reveals significant insights into consumer preferences and market trends on Flipkart. Sellers can leverage these findings to optimize their product offerings, focusing on popular colors, balanced memory and storage options, and maintaining high product quality to achieve better customer ratings.

## Repository Contents

- **data/**: Contains the raw and processed data files.
- **notebooks/**: Jupyter notebooks with the EDA, visualizations, and analysis.
- **reports/**: PDF and other report formats summarizing the findings.
- **scripts/**: Python scripts used for data scraping, cleaning, and analysis.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flipkart-mobile-data-analysis.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd flipkart-mobile-data-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter notebooks in the `notebooks` directory to explore data and analysis.
## Acknowledgements

 - [Flipkart Mobile Dataset](hhttps://www.kaggle.com/datasets/devsubhash/flipkart-mobiles-dataset)
 - [README](https://github.com/SelvaganapathyRY/Flipkart-Mobile-Data-Analysis/edit/main/README.md)
