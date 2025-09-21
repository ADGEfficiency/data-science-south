---
title: 'Kilowatts kW vs. Kilowatt Hours kWh'
description: Being careful and consistent when dealing with kilowatts and kilowatt-hours is a basic for all energy professionals.
date: 2016-10-21
date_updated: 2025-09-05
competencies:
  - Energy
aliases:
- energy-basics-kw-vs-kwh
- /energy-basics-kw-vs-kwh

---

**Being careful and consistent when dealing with kilowatts `kW` and kilowatt-hours `kWh` is a basic for all energy professionals**. Someone who misuses these shows either a lack of care or a lack of understanding - both of which can be fatal.

## Understanding the Difference Between kW and kWh

**Understanding the difference between kilowatts `kW` and kilowatt-hours `kWh` is therefore a basic for energy industry professionals**. The key to understanding the difference is understanding the how they relate to time.

An analogy with distance and speed can is helpful to grasp the concepts of `kW` and `kWh`. **We measure distance in fixed amounts – such as 50 kilometers. Energy is measured in the same way using the unit `kWh`**. `50 kWh` is a fixed amount of energy.

**Speed is the rate at which we are covering distance – such as 50 km/h. The rate of energy generation or consumption is measured using units of kW**. This rate is known as power. The `kW` is a measurement of `kJ/s` (`kJ` is a different unit to measure energy. For reference `3,600 kJ = 1 kWh`).

| Concept  | Amount | Unit  | Rate   | Unit   |
|----------|--------|-------|--------|--------|
| Distance | 50     | km    | Speed  | km/hr  |
| Energy   | 50     | kWh   | Power  | kW     |

**If you ever see `kW/hr` – this is almost certainly an error**. Technically this is equivalent to acceleration – the rate at which we are changing our power. People often mistakenly use `kW/hr` when they should be using `kWh` – don't be one of these people!

## Relating kW to kWh

How then to relate `kW` to `kWh`? **We need one more piece of information – the length of time over which we are producing or consuming energy**.

If we were driving a car at a certain speed, to know how far we had driven we need to know how long we had been driving. **Likewise if we are consuming energy at a certain rate, to know how much energy we had consumed we need to know how long we had been operating**.

For example, if we had been consuming at 50 kW for 1 hour, we would have consumed 50 kWh. Two hours would lead to a consumption of 100 kWh, half an hour 25 kWh.

**Table 2 – Relationship between rate, length of time and consumption**

*How varying the rate (speed or power) affects consumption*

| Time   | Speed    | Distance | Rate  | Amount  |
|--------|----------|----------|-------|--------|
| 1 hour | 50 km/hr | 50 km    | 0.5 kW| 0.5 kWh|
| 1 hour | 75 km/hr | 75 km    | 1 kW  | 1 kWh  |
| 1 hour |100 km/hr |100 km    | 2 kW  | 2 kWh  |

*How varying the length of time affects consumption*

| Time     | Speed    | Distance | Rate | Amount  |
|----------|----------|----------|------|--------|
| 0.5 hour |100 km/hr | 50 km    | 1 kW | 0.5 kWh|
| 1 hour   |100 km/hr |100 km    | 1 kW | 1 kWh  |
| 2 hours  |100 km/hr |200 km    | 1 kW | 2 kWh  |

**These concepts need to be grasped forwards, backwards and side to side**. You must be comfortable with moving from:

```
kW * hr = kWh
kWh / hr = kW
kWh / kW = hr
```

## Analyzing Energy Data

We can now use these concepts to analyze energy data.

Suppose you have the following data for a CHP scheme. This is a CHP scheme with the facility to dump heat (not all heat generated is necessarily recovered).

**Table 3 – Sample data**

| Parameter              | Unit | Value     |
|------------------------|-----|----------|
| Engine electric size   | kWe |       400|
| Engine thermal size    | kW  |       400|
| Annual heat recovered  | kWh | 1,809,798|
| Annual power generated | MWh |     2,571|
| Annual operating hours | hr  |     5,638|

What insights can we gain from this? I would look at the following:

### Annual Heat Recovery

Calculate the maximum amount of heat our engine could generate in a year (i.e. assuming full load operation for the entire year).
```
maximum heat generation = engine thermal size * annual operating hours
22,55,200 kWh of heat = 400 kW * 5,638 hours
```
**This validates the annual heat recovery as reasonable at 80% of the maximum available heat**.

Calculate the average heat recovery
```
average heat recovery = annual heat recovery / annual operating hours
321 kW = 1,809,798 kWh / 5,638 hr
```
We do not why this number is low. **It could be due to part load operation of the CHP or due to heat dumping**.

### Annual Power Generation

Again we dimension the power generation using the operating hours. Note the division to convert from kWh to MWh.

```
maximum power generated = engine electric size * annual operating hours
2,255 MWh = 400 kW * 5,638 hours / 1000
```

**This flags up an error with the annual power generated value of `2,571 MWh` as it is greater than our maximum!**

We could also spot this error by calculating
```
average electric output = annual power generated / annual operating hours
456 kWe = 2,571 MWh / 5638 hr * 1000
```
This gives us an average engine electric output of `456 kWe` - **which is greater than the size of our engine**.

## Summary

**The two concepts of an amount of energy (kWh) and the rate of energy consumption/generation (kW) are related to each other by a length of time**.

Understanding this allows energy industry professionals to check the validity of data, as well as calculate new data to evaluate performance. **Both skills are valuable to engineers and non-engineers alike**.

Thanks for reading!
