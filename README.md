# Airports

Airports is one of the domains, which is a part of the IndicWiki Project.

# Description

The aim of this domain is to create many articles (about 20000) about various airports around the world. Hence, we are generating these data-rich articles in telugu for about 20000 airports, and uploading them to Wikipedia, so that people who can read only in their native language (here, telugu) can benefit from this information.

# Installation and setup

Create virtual environment in the project folder using the following commands.

```bash
pip install virtualenv

pip install python3.9 

virtualenv -p python3.9 AirportsEnv
```

After the successful creation of virtual environment (venv), clone the repository or download the zip folder of the project and extract it. Run the following commands from the Airports (root) directory to activate the virtual environment and install all necessary dependencies.

```bash
source AirportsEnv/bin/activate

pip install -r requirements.txt
```

requirements.txt comes along with the Project Directory.

# Guide to generate XML dump, articles for different Airports

- Clone the repository into the local system.

- Enter the 'curDir' folder inside the cloned repo.

- Open the notebook file genXML.ipynb, Configure From_n and To_n variables then Execute the notebook by clicking on "Run all", where From_n and To_n correspond to the row numbers of the first and last desired articles (only serial order is possible). For example From_n = 30 and To_n = 50 would generate xml dump for Airports in rows 30-50 (inclusive). By default, dump is generated for all Birds (case where no mdifications are done).

- On executing the above Notebook xml dump is obtained in Airports.xml. If From_n and To_n were modified then the file name would be Airports_{From_n}-{To_n}.xml, names of these files would have the range passed in their filenames (such as Airports_30-50.xml etc).

# GitHub Structure

- The Airports (root) folder contains files as

   - requirements.txt → python requirements file

   - birds.xml → the xml dump for all birds

The folder curDir contains the entire implementation corresponding to article generation. This directory contains the codebase for the new model, converting knowledge base to intermediate structured article (dataframe of labeled article sentences) which can be modified and updated by users and then converting this data to XML page which can be imported in mediawiki.


# Data
Github Folder Link:
This folder contains various datasets (final and intermediate), and the implementations as to how they were obtained. Different formats of the dataset are present as follows (like csv, excel etc):
- Airports.html → HTML sweetviz report of the Airport dataset.
- Airports.xlsx → Excel file containing data of all the 20000+ airports including all their attributes values.
- Airports_Dataset_English_only.xlsx → Excel file containing data of all the airports only in English
- Dataset_final.xlsx → Final Dataset of all the airports including both English and telugu translated values of attributes.
Data_collection

# GitHub Folder Link:
Our whole data is based on datasets taken from this website - Dataset formats @ OurAirports
This website is a free site where visitors can explore airports around the world. It mainly contains 3 datasets. They are

- Airports.csv
- Airports_frequencies.csv
- Airports_runway.csv
Each csv file contains a unique id and an identifier. We have taken this ident as a primary key.
Apart from this, we have scraped English Wikipedia info boxes and added to our final dataset.
We used beautiful soup for scraping the data. You can find the code here.

Translation → Contains all the datasets that got translated columns wise in the form of csv, excel, etc.

All the intermediate files are saved in 2 types i.e
CSV
EXCEL	

This folder also contains the code used to scrape the data from different websites.

- Image_scraping.py ->This is a python file used to scrape the images from the Wikipedia info boxes.
- Wiki_scrape.py -> This is a python file used to scrape data from the Wikipedia info boxes.
- Join.py-> This is a python file used to join two excel or csv files based on a primary key.	
 
# Translation
GitHub Folder Link:
For most of our translation we used  Google Translate .This allows us to translate whose size is upto 2MB. After using this Google Translate, we had few unconverted data which was manually cleaned. We used Bing translator and Yandex translator to translate this unconverted data
Templates

GitHub Folder Link:
- template.j2->This file consists of the improved template to generate wikitext provided a airplanes’ data, corresponding to latest dataset.

# Contributors
Students: Srihitha, Nikhil Chandra, Varun.

Student Mentors: Bala Bhavana K, Jayaprakash Aluri 

