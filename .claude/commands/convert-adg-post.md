You are converting a blog post from another website (adgefficiency) to this website (data-science-south).

The original adgefficiency blog posts are in `./ai/adgefficiency-blog-posts-to-import/`.  They should be moved into `./content/blog`

The filename for the post to look at is provided at the end of this prompt.

For the YAML frontmatter:

- change excerpt to description
- add a date_updated set to today's date
- update the taxonomy to use comptencies

Convert image links to use she `img` shortcode:

{{< img
    src="/images/bash-shell/terminal.png"
    caption="The DEC VT100 terminal (Hardware)"
    width="500"
>}}

You must change the `src` to point at `/images`.

Example frontmatter after changes:

<frontmatter>
---
title: What is the Difference between HHV vs. LHV?
description: Explaining the conventions for quantifying the heat of combustion.
date_created: 2016-10-17
date_upated: 2025-09-04
competencies:
  - Energy
aliases:
- 2016-10-17-energy-basics-hhv-versus-lhv
- energy-basics-hhv-versus-lhv

---
</frontmatter>

For the file:

- remove the date
- move the markdown file into content/blog
- remove `energy-basics` or `energy-insights` from the file name
- add the original file name as an alias in the frontmatter

For the post:
- add sub headers
- add bold to key points

Example of post before:

<post-before-conversion>
Heat transfer is a fundamental energy engineering operation.  Hot water loops are commonly used to transfer heat in district heating networks and on industrial sites.

The capital & operating cost of many hot water loops are higher than they should be.  This post will explain why this is happening in the context of the foundational energy engineering equation `Q = m * Cp * dT`.

![Figure 1 – A simple hot water loop]({{ "/assets/q_mcdt/hot-water-loop-1.png"}})
**Figure 1 – A simple hot water loop**

This equation shows how to calculate heat transfer in our hot water loop:
```
Q = m * Cp * dT

heat = mass flow * specific heat capacity * temperature difference

kW = kg/s * kJ/kg/°C * °C
```
The mass flow rate `m [kg/s]` is a measurement of the amount of water flowing around the hot water loop.

The specific heat capacity `Cp [kJ/kg/°C]` is a thermodynamic property specific of the fluid used to transfer heat. We could manipulate the specific heat capacity only by changing the fluid used in the loop.

Water is a good fluid choice for cost and safety considerations.  The specific heat capacity of water does vary with temperature but for the scope of a hot water loop it is essentially constant.

The temperature difference `dT [°C]` is the difference in temperature before and after heat transfer.

Optimization of a hot water loop requires correctly setting the flow rate and temperature.  We could use a high mass flow rate and low temperature difference.  We could also use a low mass flow rate with a high temperature difference.

A low mass flow with high temperature difference is optimal and will reduce our capital  & operating costs.   A low mass flow rate minimizes the amount of electricity required to pump water around the loop.

A high temperature difference leads to:

- increase in the maximum capacity of the loop to deliver heat.  Pipe size limits the capacity of the loop by limiting the maximum flow rate.  More heat can be transferred at the maximum flow rate by using a larger temperature difference.

- maximises heat recovery from CHP heat sources such as jacket water or exhaust.

- maximises electric output from steam turbine based systems by allowing a lower condenser pressure.

The capital cost benefit comes from being able to either transfer more heat for the same amount of investment or to install smaller diameter pipework.

The operating cost benefit arises from reduced pump electricity consumption and increased CHP system efficiency.

Thanks for reading!
</post-before-conversion>


Example of post after

<converted-post>
This post will explain the heat transfer equation $Q = m \cdot C_p \cdot dT$ and how to apply it to optimize the capital and operating cost of hot water loops.

## The Heat Transfer Equation

```mermaid
flowchart LR
    HG["Heat Generation<br/> Q = m · C_p · dT"]
    HC["Heat Consumption <br/> Q = m · C_p · dT"]

    HG -->|"m [kg/s]<br/>T_FLOW [°C]"| HC
    HC -->|"m [kg/s]<br/>T_RET [°C]"| HG

    style HG fill:#ffeeee,stroke:#ff6666,stroke-width:2px
    style HC fill:#eeeeff,stroke:#6666ff,stroke-width:2px
```

**A simple hot water loop**

This equation shows how to calculate heat transfer in our hot water loop:

$$Q \text{ [kW]} = m \text{ [kg/s]} \cdot C_p \text{ [kJ/kg/°C]} \cdot dT \text{ [°C]}$$

- **Heat transfer rate** $Q$ [kW]: amount of thermal energy transferred per unit time.
- **Mass flow rate** $m$ [kg/s]: measurement of the amount of water flowing around the hot water loop.
- **Specific heat capacity** $C_p$ [kJ/kg/°C]: thermodynamic property specific of the fluid used to transfer heat. We could manipulate the specific heat capacity only by changing the fluid used in the loop.
- **Temperature difference** $dT$ [°C]: difference in temperature before and after heat transfer.

## Application: Sizing Hot Water Loops

**Hot water loops are commonly used to transfer heat in district heating networks and on industrial sites**. The capital and operating costs of many hot water loops are higher than they should be.

Optimization of a hot water loop requires correctly setting the flow rate and temperature.  **We could use a high mass flow rate and low temperature difference.  We could also use a low mass flow rate with a high temperature difference**.

Water is a good fluid choice for cost and safety considerations.  The specific heat capacity of water does vary with temperature but for the scope of a hot water loop it is essentially constant.

**A low mass flow with high temperature difference is optimal and will reduce our capital & operating costs**. A low mass flow rate minimizes the amount of electricity required to pump water around the loop.

A high temperature difference leads to:

- **Increased heat capacity**: Pipe size limits the capacity of the loop by limiting the maximum flow rate. More heat can be transferred at the maximum flow rate by using a larger temperature difference
- **Maximized heat recovery**: From CHP heat sources such as jacket water or exhaust
- **Maximized electric output**: From steam turbine based systems by allowing a lower condenser pressure

**The capital cost benefit comes from being able to either transfer more heat for the same amount of investment or to install smaller diameter pipework**.

The operating cost benefit arises from reduced pump electricity consumption and increased CHP system efficiency.

## Summary

Heat transfer is a fundamental energy engineering operation.

The heat transfer equation $Q = m \cdot C_p \cdot dT$ relates the heat transfer rate to the mass flow rate, specific heat capacity and temperature difference.

It is fundamental to optimizing hot water loop systems:

- **Low mass flow, high temperature difference** minimizes both capital and operating costs
- **Reduced pumping costs** from lower flow rates
- **Smaller pipe diameters** possible with higher temperature differences
- **Enhanced heat recovery** from CHP systems
- **Increased system capacity** within existing infrastructure constraints

Thanks for reading!
</converted-post>

Convert the following blog post
