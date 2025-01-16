# Identifying Brute Force Attacks with Network Packet Capturing and Support Vector Machines

This repository contains the code and resources for a project investigating the detection of brute force attacks on network traffic using machine learning, specifically Support Vector Machines (SVMs). The analysis was conducted using the CSE-CIC-IDS2018 dataset, with a focus on SSH and FTP brute force attacks.

This repository is part of the final project of Data Analytics, a course I took during my time at Northumbria University in Newcastle, taught by [Lucas França, PhD](https://lfranca.uk/) and [Jamie Mahoney, PhD](https://researchportal.northumbria.ac.uk/en/persons/jamie-mahoney).

This project was idealized to run in Linux systems and requires, among other things, AWS CLI and Poetry.

### Project Structure

 - `notebooks/`
   - `1-reading-raw-data.ipynb`: data download and preprocessing
   - `2-exploratory-analysis.ipynb`: additional processing and exploratory analysis with graphs
   - `3-models.ipynb`: SVM model training and analysis
 - `scripts/`
   - `download_data.py`: used by the first notebook for fetching data from S3 bucket

### Running the notebooks

You need to have poetry installed in order to manage dependencies.

```shell
poetry shell
poetry update
```

Wherever you run the Jupyter Notebooks, activate the environment when choosing the kernel.
