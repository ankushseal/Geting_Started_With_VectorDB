**README**

## Healthcare Data Analysis with Vector Database

This repository contains a Proof of Concept (POC) for analyzing healthcare data using a vector database. The goal of this POC is to demonstrate how vector databases can be utilized for searching and analyzing healthcare records based on a specific input query.

### Prerequisites

Before running the code, ensure you have the following dependencies installed:

- Python 3.x
- qdrant-client
- sentence-transformers

You can install the dependencies via pip:

```bash
pip install qdrant-client sentence-transformers
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/healthcare-data-analysis.git
cd healthcare-data-analysis-using-vectordb
```

2. Run the Python script `healthcare_analysis.py`:

```bash
python healthcare_analysis.py
```

3. Follow the prompts to input the Date of Birth (DOB) you want to search for.

### Description

This POC utilizes a vector database and the Sentence Transformers library to analyze healthcare data based on Date of Birth (DOB) queries. It includes the following components:

- **Vector Database Setup**: The code initializes a vector database using the qdrant-client library and defines a collection named "HC_data" for storing healthcare records.

- **Data Encoding**: Each healthcare record is encoded using the Sentence Transformers library to generate vector representations based on the Date of Birth (DOB).

- **Data Upload**: Encoded records are uploaded to the vector database, associating each record with its corresponding vector representation.

- **Search**: Users can input a Date of Birth (DOB) query, which is encoded into a vector representation and used to search the vector database for similar records. The closest matching records are retrieved and displayed along with their scores.

### Input Data

The input data consists of sample healthcare records containing the following fields:

- `memberid`: Member ID
- `member_name`: Member Name
- `covg_start_date`: Coverage Start Date
- `covg_end_date`: Coverage End Date
- `address`: Member Address
- `city`: Member City
- `dob`: Date of Birth

### Output

The output displays the healthcare records that closely match the input Date of Birth (DOB) query along with their scores indicating the similarity.

### Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug fixes, please feel free to open an issue or create a pull request.

### Acknowledgements

- [qdrant-client](https://github.com/qdrant/qdrant) - Python client for Qdrant vector database.
- [Sentence Transformers](https://github.com/UKPLab/sentence-transformers) - Python library for sentence and text embeddings.
