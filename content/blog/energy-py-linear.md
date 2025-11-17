---
title: Optimize Energy Assets with energy-py-linear
description: A Python library for optimizing batteries, EVs, CHP and renewable generators using mixed-integer linear programming.
date_created: 2019-02-06
date_updated: 2025-11-01
github: https://github.com/ADGEfficiency/energy-py-linear
competencies:
- Energy
aliases:
- 2019-02-06-intro-energy-py-linear

---

**Optimizing energy assets is critical for maximizing profit and minimizing carbon emissions** - but most energy asset operators rely on simple heuristics or manual dispatch decisions.

**Linear programming offers a better solution** - it can find optimal dispatch schedules for batteries, electric vehicles, combined heat and power generators, and renewable assets.

**This post introduces energy-py-linear** - a Python library that makes it easy to optimize energy assets using mixed-integer linear programming (MILP).

You can find the source code at [ADGEfficiency/energy-py-linear](https://github.com/ADGEfficiency/energy-py-linear) and the documentation at [energypylinear.adgefficiency.com](https://energypylinear.adgefficiency.com/latest).

## Why Linear Programming for Energy?

**Linear programming is the right tool for many energy optimization problems** - energy systems often have linear characteristics that make them well-suited for linear solvers.

Advantages:

- **Deterministic**: No randomness like gradient descent, same inputs always produce same outputs
- **Fast**: Linear programs are solved efficiently, feasible solutions exist on constraint boundaries
- **Proven**: Widely used in industry for energy dispatch and scheduling
- **Interpretable**: Easy to understand why the optimizer made specific decisions

## What Can energypylinear Do?

energypylinear optimizes the dispatch of various energy assets:

- **Batteries**: Electricity storage with configurable power, capacity and round-trip efficiency
- **Electric vehicles**: Smart charging with flexible connection schedules
- **CHP generators**: Combined heat and power with gas consumption and heat recovery
- **Heat pumps**: Electrically-driven thermal energy conversion
- **Renewable generators**: Solar and wind with optional curtailment
- **Boilers**: Thermal generation from fuel combustion

Assets can be optimized individually or together as a site, with customizable objectives (profit, carbon, or custom) and constraints.

## Installation

Requires Python 3.11 or 3.12:

```shell
$ pip install energypylinear
```

## Example: Battery Arbitrage

The simplest use case is optimizing a single battery for price arbitrage:

```python
import energypylinear as epl

asset = epl.Battery(
    power_mw=2.0,
    capacity_mwh=4.0,
    efficiency_pct=0.9,
    electricity_prices=[100.0, 50, 200, -100, 0, 200, 100, -100],
)

simulation = asset.optimize()
```

The battery will charge when prices are low (or negative) and discharge when prices are high.

## Example: Multi-Asset Site Optimization

The real power of energypylinear comes from optimizing multiple assets together:

```python
import energypylinear as epl

assets = [
    epl.Battery(power_mw=2.0, capacity_mwh=4.0),
    epl.CHP(
        electric_power_max_mw=100, electric_power_min_mw=30, electric_efficiency_pct=0.4
    ),
    epl.Boiler(),
    epl.Valve(),
]

site = epl.Site(
    assets=assets,
    electricity_prices=[100, 50, 200, -100, 0],
    high_temperature_load_mwh=[105, 110, 120, 110, 105],
    low_temperature_load_mwh=[105, 110, 120, 110, 105],
)

simulation = site.optimize()
```

The optimizer coordinates all assets to minimize cost while meeting thermal loads.

## Example: Carbon-Optimized Renewable Site

energypylinear can optimize for carbon emissions instead of profit:

```python
import energypylinear as epl

assets = [
    epl.Battery(power_mw=10, capacity_mwh=20, efficiency_pct=0.9),
    epl.RenewableGenerator(
        electric_generation_mwh=[10, 20, 30, 20, 10],
        electric_generation_lower_bound_pct=0.5,
        name="solar",
    ),
]

site = epl.Site(
    assets=assets,
    electricity_carbon_intensities=[0.5, -0.5, 0.5, 0.5, -0.5],
    export_limit_mw=25,
)

simulation = site.optimize(objective="carbon")
```

The results show how the battery and solar generation coordinate to minimize carbon:

```
   site-electricity_carbon_intensities  site-export_limit_mw  site-export_power_mwh  solar-electric_generation_used_mwh  battery-electric_charge_mwh  battery-electric_discharge_mwh
0                                  0.5                    25                  10.00                                10.0                        0.00                          0.00
1                                 -0.5                    25                  25.00                                20.0                        5.00                          0.00
2                                  0.5                    25                  25.00                                30.0                        0.00                          5.00
3                                  0.5                    25                  15.00                                20.0                        0.00                          5.00
4                                 -0.5                    25                  10.00                                10.0                        0.00                          0.00
```

Key observations:

- **Interval 1**: Negative carbon intensity, battery charges to enable maximum export
- **Intervals 2-3**: Positive carbon intensity, battery discharges to maximize export
- **Export limit**: 25 MW limit is respected throughout

## Advanced Features

energypylinear supports advanced use cases:

- **Custom constraints**: Add your own linear constraints to the model
- **Custom objectives**: Define alternative objective functions beyond cost or carbon
- **Network charges**: Model complex electricity tariffs with time-of-use pricing
- **Battery degradation**: Account for capacity fade over time
- **Dispatch forecasts**: Optimize future dispatch based on forecasted prices

## When to Use energypylinear

energypylinear is ideal for:

- **Business case modeling**: Evaluating investment in energy assets
- **Day-ahead dispatch**: Optimizing assets based on day-ahead price forecasts
- **Carbon analysis**: Understanding carbon impact of different dispatch strategies
- **Multi-asset coordination**: Finding optimal schedules across multiple assets

energypylinear is not suitable for:

- **Real-time control**: Too slow for sub-second dispatch decisions
- **Nonlinear systems**: Only models linear relationships
- **Very large systems**: Performance degrades with thousands of intervals or assets

## Summary

energypylinear makes it easy to optimize energy assets using mixed-integer linear programming.

Key features:

- **Multiple asset types**: Batteries, EVs, CHP, heat pumps, renewables, boilers
- **Flexible objectives**: Optimize for profit, carbon, or custom objectives
- **Site optimization**: Coordinate multiple assets together
- **Customizable**: Add custom constraints and objectives
- **Production-ready**: Type-safe, well-tested, documented

Learn more:

- **Documentation**: [energypylinear.adgefficiency.com](https://energypylinear.adgefficiency.com/latest)
- **Source code**: [github.com/ADGEfficiency/energy-py-linear](https://github.com/ADGEfficiency/energy-py-linear)
- **Installation**: `pip install energypylinear`

Thanks for reading!
