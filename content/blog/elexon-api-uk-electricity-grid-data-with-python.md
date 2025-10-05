---
title: Elexon API UK Electricity Grid Data using Python
description: Downloading, cleaning & joining UK electricity grid data with pandas, requests and pydantic.
date_created: 2016-12-08
date_updated: 2025-10-05
competencies:
  - Data Engineering
  - Energy
aliases:
  - 2022-03-23-elexon-api-uk-electricity-grid-data-with-python

---

This post demonstrates how to use Python to download UK electricity data using the Elexon API - specifically data for the [imbalance price](http://adgefficiency.com/what-is-the-uk-imbalance-price/) - both the **imbalance prices** and **imbalance volumes**.

**In this post we will use the Python packages `pandas` for data processing, `requests` making HTTP requests and `pydantic` for structuring our data**.

This work is inspired by [Patrick Avis](http://energyanalyst.co.uk/) - the credit for this work will always be with Patrick!

## The ELEXON API

**Elexon provides generation, volume and price data for the UK electricity grid** through the [Balancing Mechanism Reporting Service (BMRS)](https://www.bmreports.com/bmrs/?q=help/about-us) - the BRMS can best thought of as a dataset.

[The Elexon API guide](https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/) provides detail on the data available through the BRMS. **In this post we will be working with reports `B1770` for imbalance prices and `B1780` for the imbalance volumes**.

The BRMS data is available through the [Elexon Portal](https://www.elexonportal.co.uk/news/latest?cachebust=bgzrrqj2lj) (through your web browser) or the Elexon API (to access data programmatically). Both require a free Elexon account.

You will need to be logged in to your Elexon account to use the portal, or else you will not see the data:

{{< img
    src="/images/elexon/f1.png"
    caption="Elexon Portal - login required to view data"
    width="512"
>}}

**You will also need to create an Elexon account to use the API**, as you need an API key (called a *scripting key* by Elexon) which you can find in the profile section of your Elexon account.

## Python Requirements

You can install the Python packages needed to run the Python program with:

```shell
$ pip install pandas pydantic requests
```

The core logic of our program is below (without the required imports):

```python
url = f"https://api.bmreports.com/BMRS/{report}/v1?APIKey={api_key}&Period=*&SettlementDate={date}&ServiceType={service_type}"
res = requests.get(url)
(Path.cwd() / "data.csv").write_text(res.text)
data = pd.read_csv("./data.csv", skiprows=4)
```

The full program we develop is given at the end of the post.

## Scraping the Elexon API

Let's start by **requesting data from the Elexon API**. We do this by making a **HTTP request** to a URL.

The Elexon API documentation specifies how we need to format our URL:

{{< img
    src="/images/elexon/f2.png"
    caption="Elexon API URL format specification"
    width="512"
>}}

**We will need to specify a few things to get the data we want**: the **report name** (like `B1770`), our **API key**, the **settlement date** (like `2020-01-01`) and the **data format** we want back (either XML or CSV).

### Managing Secrets

The API key (which you can get through the Elexon portal) is a **secret** - it will not end up as part of our codebase.

One way to manage secrets is to create a file `secret.py`, which we can import from in other Python scripts:

```python
#  secret.py
api_key = "your-api-key-here"
```

**Very important that this file `secret.py` does not end up in your source control** (commonly Git) - this file should be added to your `.gitignore` or equivalent. If secrets are in your source control, you are going to have a bad time.

In production environments these secrets are often managed at build/deploy time - where the secret is injected into the environment as environment variables.

### Creating the Request

Before we create our URL in as a string Python, we will define a `pydantic` type called `ElexonRequest`, to organize the data we need in the URL:

```python
import datetime
import pydantic
from secret import api_key


class ElexonRequest(pydantic.BaseModel):
    report: str
    date: datetime.date
    api_key: pydantic.SecretStr = pydantic.SecretStr(api_key)
    service_type: str = "csv"


req = ElexonRequest(report="B1770", date="2020-01-01")
# report='B1770' api_key=SecretStr('**********') date=datetime.date(2020, 1, 1) service_type='csv'
```

We can access data using the attribute (`.`) syntax:

```python
print(req.report, req.date, req.service_type)
# B1770 2020-01-01 csv
```

Now we have the data we need for a request, we can create our URL using a Python f-string:

```python
url = f"https://api.bmreports.com/BMRS/{req.report}/v1?APIKey={req.api_key}&Period=*&SettlementDate={req.date.isoformat()}&ServiceType={req.service_type}"
# https://api.bmreports.com/BMRS/B1770/v1?APIKey=**********&Period=*&SettlementDate=2020-01-01&ServiceType=csv
```

**When we print the URL, the secret is hidden!** This is because we used a `SecretStr` type for the API key. If we want to access the secret in `api_key`, we need to use `api_key.get_secret_value()`.

### Making the HTTP Request

Now we have our URL, **we can use the Python library `requests` to call the Elexon API** by making an HTTP request to the web server behind this URL - the same way your browser sends HTTP requests to a server to access a web page.

Along the way we check that the status code of the HTTP response is `200` (`200` means everything is ok):

```python
import requests

req = ElexonRequest(report="B1770", api_key=api_key, date="2020-01-01")
url = f"https://api.bmreports.com/BMRS/{req.report}/v1?APIKey={req.api_key.get_secret_value()}&Period=*&SettlementDate={req.date.isoformat()}&ServiceType={req.service_type}"
res = requests.get(url)
assert res.status_code == 200
print(res.text[:512])
# *
# *
# *Imbalance Prices Service For Balancing (B1770) Data
# *
# *DocumentID,DocumentRevNum,ActiveFlag,...
```

### Saving and Loading Data

Now all we need to do is save this raw data as a CSV file - making no changes to the data on the way.

We can use `pathlib` to dump this text to a file in a folder called `data`:

```python
from pathlib import Path

fi = Path().cwd() / "data" / f"{req.report}-{req.date}.csv"
fi.parent.mkdir(exist_ok=True)
fi.write_text(res.text)
```

We can use the shell command `head` to look at the first `7` lines of this file:

```shell
$ head -n 7 data/B1770-2020-01-01.csv
*
*
*Imbalance Prices Service For Balancing (B1770) Data
*
*DocumentID,DocumentRevNum,ActiveFlag,ProcessType,...
```

**We can then load this data back again using the Python library `pandas`** - skipping the first `4` rows (they are not valid CSV data):

```python
import pandas as pd

data = pd.read_csv("./data/B1770-2020-01-01.csv", skiprows=4)
```

One final thing we may want to clean is to remove the final row (which contains `<EOF>` - end of file):

```python
data = data.dropna(axis=0, subset=["SettlementDate"])
```

**This is current best practice in data engineering** - saving the raw data and starting the next step by loading the data back again.

It may seem inefficient in terms of storage (it is) - but **storage is cheap, and this system allows more flexible and independent data pipeline design**.

## Creating datasets from the Elexon API

In this section we will create two datasets - one for each report (`B1770` & `B1780`).

Above we have created the code to send a single request to the Elexon API - let's wrap it up inside a function:

```python
import datetime
from pathlib import Path

import requests
import pandas as pd
import pydantic

from secret import api_key


class ElexonRequest(pydantic.BaseModel):
    report: str
    date: datetime.date
    api_key: pydantic.SecretStr = pydantic.SecretStr(api_key)
    service_type: str = "csv"


def send_elexon_request(req: ElexonRequest) -> pd.DataFrame:
    url = f"https://api.bmreports.com/BMRS/{req.report}/v1?APIKey={req.api_key.get_secret_value()}&Period=*&SettlementDate={req.date.isoformat()}&ServiceType={req.service_type}"
    res = requests.get(url)
    assert res.status_code == 200

    fi = Path().cwd() / "data" / f"{req.report}-{req.date}.csv"
    fi.parent.mkdir(exist_ok=True)
    fi.write_text(res.text)

    data = pd.read_csv(fi, skiprows=4)
    #  B1770 has SettlementDate, B1780 has Settlement Date
    data.columns = [d.replace(" ", "") for d in data.columns]
    return data.dropna(axis=0, subset=["SettlementDate"])
```

We can run our function using a single `ElexonRequest`:

```python
data = send_elexon_request(ElexonRequest(report="B1770", date="2020-01-01"))
```

But we want to make many requests - for two reports and many settlement dates.

Below we use a `defaultdict` to hold this data - iterating over both reports and dates to create two datasets:

```python
from collections import defaultdict

dataset = defaultdict(list)
for report in ["B1770", "B1780"]:
    for date in pd.date_range("2020-01-01", "2020-01-03", freq="D"):
        data = send_elexon_request(ElexonRequest(report=report, date=date))
        dataset[report].append(data)
```

We can then take these lists of data and create a single dataframe for each report:

```python
for report, data in dataset.items():
    data = pd.concat(data, axis=0)
    data.to_csv(f"./data/{report}-all.csv", index=False)
    print(f"combined {len(data)} days for {report} into {data.shape}")
    # combined 288 days for B1770 into (288, 15)
    # combined 144 days for B1780 into (144, 15)
```

## Joining our two reports together

At this stage we have two CSV files - one per report. **Joining them together will require a bit more data cleaning**.

There are two things we want to fix in data cleaning:

- **Flatten `B1770`**: It currently has twice as many rows than `B1780`, due to stacking of the long & short imbalance prices
- **Create a proper `datetime` column**: A column that combines the period and the date into a datetime for joining

### Flattening B1770

Notice above how report `B1770` has twice the amount of data as `B1780`? **This is because the long and short imbalance prices are stacked on top of each other**. This is not tidy data - we do not have one row per observation.

We can solve this problem using a pivot:

```python
class ElexonReport(pydantic.BaseModel):
    report: str
    columns: list


rep = ElexonReport(
    report="B1770",
    columns=[
        "SettlementDate",
        "SettlementPeriod",
        "ImbalancePriceAmount",
        "PriceCategory",
    ],
)

data = pd.read_csv(f"./data/{rep.report}-all.csv")

data = (
    data.pivot(
        index=["SettlementDate", "SettlementPeriod"],
        columns="PriceCategory",
        values="ImbalancePriceAmount",
    )
    .sort_index()
    .reset_index(drop=True)
)
```

### Making our datetime column

Now that we have a flat, tidy dataset, **we can create a proper timestamp column to join on** - by creating a date range:

```python
data["datetime"] = pd.date_range(
    start=data["SettlementDate"].min(),
    periods=len(data),
    freq="30T",
    tz="Europe/London",
)

print(
    data.loc[
        :,
        [
            "SettlementDate",
            "SettlementPeriod",
            "datetime",
            "Excess balance",
            "Insufficient balance",
        ],
    ].iloc[:3, :]
)
# PriceCategory SettlementDate  SettlementPeriod                  datetime  Excess balance  Insufficient balance
# 0                 2020-01-01               1.0 2020-01-01 00:00:00+00:00        50.90000              50.90000
# 1                 2020-01-01               2.0 2020-01-01 00:30:00+00:00        51.00000              51.00000
# 2                 2020-01-01               3.0 2020-01-01 01:00:00+00:00        29.37006              29.37006
```

## Cleaning Pipeline

Here is our full cleaning pipeline - from our CSV datasets (one per report) on disk to a single dataset:

```python
reports = [
    ElexonReport(
        report="B1770",
        columns=[
            "SettlementDate",
            "SettlementPeriod",
            "ImbalancePriceAmount",
            "PriceCategory",
        ],
    ),
    ElexonReport(
        report="B1780",
        columns=[
            "SettlementDate",
            "SettlementPeriod",
            "ImbalanceQuantity(MAW)",
            "ImbalanceQuantityDirection",
        ],
    ),
]

dataset = {}
for rep in reports:
    data = pd.read_csv(f"./data/{rep.report}-all.csv")
    data = data.loc[:, rep.columns]

    if rep.report == "B1770":
        data = (
            data.pivot(
                index=["SettlementDate", "SettlementPeriod"],
                columns="PriceCategory",
                values="ImbalancePriceAmount",
            )
            .sort_index()
            .reset_index()
        )

    data = data.sort_values(["SettlementDate", "SettlementPeriod"])

    data["datetime"] = pd.date_range(
        start=data["SettlementDate"].min(),
        periods=len(data),
        freq="30T",
        tz="Europe/London",
    )
    data = data.set_index("datetime")
    dataset[rep.report] = data

final = pd.concat(dataset.values(), axis=1)
final.to_csv("./data/final.csv")
final = final.loc[:, ~final.columns.duplicated()]
```

## Final Data Pipeline

And here is the entire pipeline - both the downloading of the data and the data cleaning pipeline:

```python
from collections import defaultdict
import datetime
from pathlib import Path

import requests
import pandas as pd
import pydantic

from secret import api_key


class ElexonRequest(pydantic.BaseModel):
    report: str
    date: datetime.date
    api_key: pydantic.SecretStr = pydantic.SecretStr(api_key)
    service_type: str = "csv"


class ElexonReport(pydantic.BaseModel):
    report: str
    columns: list


def send_elexon_request(req: ElexonRequest) -> pd.DataFrame:
    url = f"https://api.bmreports.com/BMRS/{req.report}/v1?APIKey={req.api_key.get_secret_value()}&Period=*&SettlementDate={req.date.isoformat()}&ServiceType={req.service_type}"
    res = requests.get(url)
    assert res.status_code == 200

    fi = Path().cwd() / "data" / f"{req.report}-{req.date}.csv"
    fi.parent.mkdir(exist_ok=True)
    fi.write_text(res.text)

    data = pd.read_csv(fi, skiprows=4)
    #  B1770 has SettlementDate, B1780 has Settlement Date
    data.columns = [d.replace(" ", "") for d in data.columns]
    return data.dropna(axis=0, subset=["SettlementDate"])


if __name__ == "__main__":
    reports = [
        ElexonReport(
            report="B1770",
            columns=[
                "SettlementDate",
                "SettlementPeriod",
                "ImbalancePriceAmount",
                "PriceCategory",
            ],
        ),
        ElexonReport(
            report="B1780",
            columns=[
                "SettlementDate",
                "SettlementPeriod",
                "ImbalanceQuantity(MAW)",
                "ImbalanceQuantityDirection",
            ],
        ),
    ]

    dataset = defaultdict(list)
    for rep in reports:
        for date in pd.date_range("2020-01-01", "2020-01-03", freq="D"):
            dataset[rep.report].append(
                send_elexon_request(ElexonRequest(report=rep.report, date=date))
            )

    for report, data in dataset.items():
        data = pd.concat(data, axis=0)
        data.to_csv(f"./data/{report}-all.csv")
        print(f"combined {len(data)} days for {report} into {data.shape}")

    dataset = {}
    for rep in reports:
        data = pd.read_csv(f"./data/{rep.report}-all.csv").loc[:, rep.columns]

        if rep.report == "B1770":
            data = (
                data.pivot(
                    index=["SettlementDate", "SettlementPeriod"],
                    columns="PriceCategory",
                    values="ImbalancePriceAmount",
                )
                .sort_index()
                .reset_index()
            )

        data = data.sort_values(["SettlementDate", "SettlementPeriod"])
        data["datetime"] = pd.date_range(
            start=data["SettlementDate"].min(),
            periods=len(data),
            freq="30T",
            tz="Europe/London",
        )
        dataset[rep.report] = data.set_index("datetime")

    final = pd.concat(dataset.values(), axis=1)
    final = final.loc[:, ~final.columns.duplicated()]
    final.to_csv("./data/final.csv")
```

## Summary

This post demonstrated how to:

- **Access the Elexon API**: Using Python `requests` with proper API key management using `pydantic.SecretStr`
- **Download UK electricity grid data**: For both imbalance prices (`B1770`) and volumes (`B1780`)
- **Clean and transform data**: Using `pandas` to pivot stacked data and create proper datetime indices
- **Join multiple datasets**: Combining price and volume data into a single, tidy dataset
- **Follow data engineering best practices**: Saving raw data before processing, using type hints with `pydantic`, and creating modular, reusable functions

---

Thanks for reading!
