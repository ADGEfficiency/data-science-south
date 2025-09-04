---
title: What is the Difference between HHV vs. LHV?
date: 2016-10-17
date_upated: 2025-09-04
competencies:
  - Energy
description: Explaining the conventions for quantifying the heat of combustion. 

---

## Higher Heating Value vs. Lower Heating Value

In the same way that two different currencies can value the same thing with a different amount of the currency, **two conventions exist for quantifying the amount of heat produced in fuel combustion `[kWh/kg]`*.  

These two conventions are:

- **Higher heating value (HHV)** aka **Gross Calorific Value (GCV)**
- **Lower Heating Value (LHV)** aka **Net Calorific Value (NCV)**

This post uses HHV/GCV and LHV/NCV interchangeably, as they can be in industry.

![Figure 1 - A fire-tube shell boiler]({{ "/assets/hhv_lhv/steam-boiler.jpg"}})
**Figure 1 – A fire-tube shell boiler**

## Water Produced During Combustion

The difference between the HHV and LHV is how **we account for water vapour produced during combustion**.

These conventions arise from a practical engineering reality.  **It’s about the water vapour produced during combustion**.  In one of natures most beautiful symmetries combustion produces water vapour.  Condensing this water vapour releases a lot of energy.

The high heating value includes this energy.  The lower calorific value doesn't include the energy released in condensing water.  This is why a gross calorific value is higher than a net calorific value.

- **HHV** Water is condensed to a liquid -> more heat is recovered
- **LHV**: Water vapour remains as vapour –> less heat is recovered

The reason for the distinction is that **water vapour in combustion products is not often condensed in practice**:

- **Steam or hot water boilers**: Condensing water requires reducing the flue gas temperature low enough where acids present in the flue gas will also condense out and cause stack corrosion and potential failure.
- **Power generation**: Water usually remains as a vapour as the temperature within the power turbine or pistons of the engine is too high.

## The Two Engineers

A British engineer argues with a European engineer about what to assume for a gas boiler efficiency.

The European engineer demands they assume 89% –  the British engineer disagrees and wants to assume 80%.

Who is correct? Which efficiency (89% or 80%) is the correct assumption?

| Table 1 – Typical HHV and LHV efficiencies  | **% HHV**  | **% LHV** |
|---------------------------------------------|------------|-----------|
| Gas boiler                                  | 80         | 89        |
| Gas engine (2 MWe)                          | 38         | 42        |
| Gas turbine (5 MWe)                         | 28         | 31        |

**It depends on how the efficiency will be used**.  

A common calculation is to calculate the gas consumption associated with supply heat from a gas boiler.  If we then want to calculate the cost of this gas, we multiply by a gas price:

```python
annual_gas_consumption = annual_heat_consumption / gas_boiler_efficiency
annual_gas_cost = annual_gas_consumption * gas_price
```

The gas price will be of the form `cost / energy [£/MWh]`.  The MWh can be given on either a HHV or LHV basis.  The correct way to specify a gas price is therefore either `£/MWh HHV` or `£/MWh LHV`.  This leaves no room for misunderstanding.

To calculate the cost using a UK gas price we would want to have assumed an efficiency of 80 % HHV.  This is because UK gas prices are given on an HHV basis.  Either convention can be used as long as all of our fuel consumptions, efficiencies and energy prices are given on the same basis.  Consistency is the entire ball game here.

Many data sheets for electricity generators will specify gas consumption or efficiency on an LHV basis.  If you are working in a country that prices fuel on an HHV basis (such as the UK) you will need convert this gas consumption to an HHV basis before you can calculate the cost.

## Summary

Key risks and best practices:

- **Convention mismatch**: Using LHV fuel consumption with HHV gas prices leads to significant cost underestimation
- **Datasheet assumptions**: Using efficiency values directly from datasheets without checking basis can eliminate project margins or drop IRR below hurdle rates
- **Best practice**: Always specify HHV or LHV when working with fuel consumptions, efficiencies and prices - be the engineer who writes 'MWh HHV' and '£/MWh HHV'

Thanks for reading!
