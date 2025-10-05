---
title: What is the UK Imbalance Price?
description: An introduction to how the UK recovers electricity grid balancing costs.
date_created: 2016-12-01
date_updated: 2025-10-05
competencies:
  - Energy
aliases:
  - 2022-03-24-what-is-the-uk-imbalance-price
  - what-is-the-uk-imbalance-price

---

**The imbalance price is the price of electricity that generators or suppliers pay for imbalance on the UK electricity grid**.

## How the UK Electricity Market Works

In the UK generators and suppliers (known as parties) contract with each other for the supply of electricity. **Generators sell electricity to suppliers who then sell electricity to residential, commercial and industrial customers**.

As System Operator **NESO (National Energy System Operator) handles real time balancing of the UK grid**. Parties submit details of their contracts to NESO one hour before delivery (known as gate closure) - allowing NESO to understand the expected imbalance.

NESO will then take actions to correct any predicted imbalance. **The Balancing Mechanism allows parties to submit bids or offers to change their position by a certain volume at a certain price** - NESO will select from these bids and offers to balance the grid in a safe, low cost way.

## Grid Balancing Services

NESO also has the ability to balance the system using actions outside the Balancing Mechanism:

- **Short Term Operating Reserve (STOR)**: Reserve capacity for short-term grid balancing, procured through daily pay-as-clear auctions since April 2021
- **Frequency Response**: Plants used to balance real time frequency variations
- **Reserve Services**: Additional capacity held in reserve
- **Emergency measures**: In more drastic scenarios NESO may call upon closed power plants or disconnect customers

**NESO attempts to minimize balancing costs within technical constraints**. Parties submit their expected positions at gate closure. For a number of reasons parties do not always meet their contracted positions.

**Imbalance occurs when a party's actual generation or consumption differs from their contracted position**. Generators may produce more or less electricity than contracted - a wind farm might generate less due to lower wind speeds, or a gas plant might trip offline unexpectedly. Suppliers may consume more or less than contracted - actual customer demand might be higher on a cold day, or lower if a large industrial customer shuts down unexpectedly. **The difference between the contracted and actual position is charged using the Imbalance Price**.

## Calculation of the Imbalance Price

**Elexon uses the costs that NESO incurs in correcting imbalance to calculate the Imbalance Price**. This is then used to charge parties for being out of balance with their contracts.

Since November 2015 (modification P305), the UK has used a **single imbalance pricing mechanism**. This means the System Buy Price (SBP) and System Sell Price (SSP) are equal in each settlement period. Both parties with energy deficits and those with energy surpluses are charged or paid at the same price.

Elexon details the process for the [calculation of the Imbalance Price here](https://www.elexon.co.uk/bsc/settlement/imbalance-pricing/).

## Data Availability

Data for the UK grid is available through the [ELEXON API](https://www.elexon.co.uk/change/new-balancing-mechanism-reporting-service-bmrs/) - [see here for a guide on how to access the Elexon API data in Python](https://adgefficiency.com/elexon-api-uk-electricity-grid-data-with-python/).

## Summary

The UK Imbalance Price is a key mechanism for maintaining grid stability and cost recovery:

- **Parties contract** for electricity supply one hour before delivery (gate closure)
- **NESO balances** the grid in real-time using the Balancing Mechanism
- **Single pricing** applies since November 2015 - System Buy Price equals System Sell Price
- **Imbalance charges** recover costs when parties deviate from contracted positions
- **Multiple balancing services** provide flexibility to maintain grid stability
- **Data is publicly available** through the ELEXON API for analysis and forecasting
