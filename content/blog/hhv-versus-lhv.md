---
title: What is the Difference Between HHV and LHV?
description: Explaining the conventions for quantifying the heat of combustion.
date_created: 2016-10-17
date_updated: 2025-09-04
competencies:
- Energy
aliases:
- energy-basics-hhv-versus-lhv
- /energy-basics-hhv-versus-lhv

---

## What are HHV and LHV?

**Two conventions exist for quantifying the amount of heat produced in fuel combustion** `[kWh/kg]`, similar to how different currencies can value the same thing with different amounts.

These two conventions are:

- **Higher heating value (HHV)** aka **Gross Calorific Value (GCV)**
- **Lower Heating Value (LHV)** aka **Net Calorific Value (NCV)**

This post uses HHV/GCV and LHV/NCV interchangeably, as they can be in industry.

{{< img
    src="/images/hhv-versus-lhv/f1.png"
    caption="A fire-tube shell boiler"
    width="500"
>}}

## The Key Difference: Water Vapour Treatment

**The difference between HHV and LHV is how we account for water vapour produced during combustion**.

These conventions arise from a practical engineering reality. **Combustion produces water vapour, and condensing this water vapour releases significant energy**.

**The high heating value includes this condensation energy. The lower calorific value doesn't include the energy released in condensing water**. This is why a gross calorific value is higher than a net calorific value.

- **HHV**: Water is condensed to a liquid → more heat is recovered
- **LHV**: Water vapour remains as vapour → less heat is recovered

### Why This Distinction Matters

**Water vapour in combustion products is not often condensed in practice**:

- **Steam or hot water boilers**: Condensing water requires reducing the flue gas temperature low enough where **acids present in the flue gas will also condense out and cause stack corrosion** and potential failure
- **Power generation**: Water usually remains as a vapour as **the temperature within the power turbine or pistons of the engine is too high**

## Application: Which Efficiency Should You Use?

### The Engineering Dilemma

A British engineer argues with a European engineer about what to assume for a gas boiler efficiency.

**The European engineer demands they assume 89% – the British engineer disagrees and wants to assume 80%**.

Who is correct? Which efficiency (89% or 80%) is the correct assumption?

| Table 1 – Typical HHV and LHV efficiencies  | **% HHV**  | **% LHV** |
|---------------------------------------------|------------|-----------|
| Gas boiler                                  | 80         | 89        |
| Gas engine (2 MWe)                          | 38         | 42        |
| Gas turbine (5 MWe)                         | 28         | 31        |

### The Answer: It Depends on Gas Pricing

**It depends on how the efficiency will be used**.

A common calculation is to calculate the gas consumption associated with supply heat from a gas boiler. If we then want to calculate the cost of this gas, we multiply by a gas price:

```python
annual_gas_consumption = annual_heat_consumption / gas_boiler_efficiency
annual_gas_cost = annual_gas_consumption * gas_price
```

**The gas price will be of the form `cost / energy [£/MWh]`. The MWh can be given on either a HHV or LHV basis**. The correct way to specify a gas price is therefore either `£/MWh HHV` or `£/MWh LHV`. This leaves no room for misunderstanding.

**To calculate the cost using a UK gas price we would want to have assumed an efficiency of 80% HHV. This is because UK gas prices are given on an HHV basis**. Either convention can be used as long as all of our fuel consumptions, efficiencies and energy prices are given on the same basis. **Consistency is the entire ball game here**.

**Many data sheets for electricity generators will specify gas consumption or efficiency on an LHV basis**. If you are working in a country that prices fuel on an HHV basis (such as the UK) you will need convert this gas consumption to an HHV basis before you can calculate the cost.

## Summary

**HHV and LHV are two conventions for quantifying heat of combustion**. The difference lies in how we account for water vapour produced during combustion:

- **HHV (Higher Heating Value)**: Includes energy from condensing water vapour → higher value
- **LHV (Lower Heating Value)**: Excludes condensation energy → lower value

### Key Risks and Best Practices

- **Convention mismatch**: Using LHV fuel consumption with HHV gas prices **leads to significant cost underestimation**
- **Datasheet assumptions**: Using efficiency values directly from datasheets without checking basis **can eliminate project margins or drop IRR below hurdle rates**
- **Best practice**: **Always specify HHV or LHV** when working with fuel consumptions, efficiencies and prices - be the engineer who writes 'MWh HHV' and '£/MWh HHV'

**The key is consistency** - ensure all fuel consumptions, efficiencies, and energy prices use the same basis.

Thanks for reading!
