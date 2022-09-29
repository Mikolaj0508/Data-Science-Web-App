
# Project Title

**Data Science Web App** is simply web application which scraps Natural Gas data from U.S. Energy Information Administration (EIA). It uses RESTAPI to get information from EIA Website. Web App functionality is provided by Streamlit framework. Data preparation is possible due to Pandas.

On Natural Gas page you could find price and consumption data scraped from EIA website. All of this information is loaded from offical page not hard-coded.

After customize options you could get sample data, download raw CSV file or get chart of desired USA area(under construction).

To get all this information you have to have your own specific API key, which you colud get automatically on offical website [https://www.eia.gov/opendata/documentation.php].

API key used in this project is hidden.
## Installation

First of all you have to install all packages

```bash
  pip install -r requirements.txt
```
After that just run this line

```bash
  streamlit run main.py
```
    
## Screenshots

[![obraz-2022-09-29-150112372.png](https://i.postimg.cc/kXYTv5Rm/obraz-2022-09-29-150112372.png)](https://postimg.cc/svSPVsJ6)

[![obraz-2022-09-29-150208060.png](https://i.postimg.cc/SNn6qfRB/obraz-2022-09-29-150208060.png)](https://postimg.cc/8jVJmWh4)
