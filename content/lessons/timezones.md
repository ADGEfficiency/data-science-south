---
title: Timezones
description: TODO
date: 2024-12-07
draft: true
---

## Why Timezones are Hard

Timezones force us to do something unnatural - consider the **same point in time** in **different places**.

Timezones are arbitrary - where we draw timezone boundaries is a political decision.  China for example has only a single timezone.

Timezones can change - cities can change from timezone to another, due to either daylight savings or a change of timezone.

### Advice for Working with Timezones

Make the decision early on about whether you need to support multiple timezones.

Stick to one timezone if you can - if your entire business is within a single timezone, use this to your advantage!  You may even be able to use timezone naive timestamps.

Use standard timezones (timezones that do not observe daylight saving) where possible.

[Default to UTC - even if it's not a silver bullet](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/).  Consider storing the timezone alongside a UTC timestamp.

Consider storing the elements of the datetime (such as year or day) as separate columns (which we know know is a partitioned representation).

Consider putting the timezone in the column name.

### What is a Timezone?

Imagine a small planet with one village - Alpha.

<img src="/datetimes/f2.png" alt="This image is in /static" width="50%">

Because of how the sun moves around this planet, different parts of the planet are in light or darkness at the same moment in time. 

For the inhabitants of Alpha, *who abhor to explore*, this doesn't matter - they live in Alpha, and always follow Alpha Standard Time - a 24 hour clock.

Until one day, a group of villagers leave for the unknown.

One day a second village is discovered - named Omega, located on the other side of the planet.  When it's day in Alpha, it is night in Omega (and vice versa).

Eager to share and learn, the village of Omega adopts Alpha Standard Time.  Quickly the effects of this decision start to become apparent.

School starts at 0600 in Alpha Standard Time - for the residents of Omega to start school at the same time of day, they start school at 1800!

In order for the time to make sense in both villages, our planet three implements timezones:

- Alpha Standard Time,
- Omega Standard Time,
- Coordinated Universal Time (known as UTC).

## UTC

One timezone we call UTC, which stands for *Coordinated Universal Time*. 

UTC serves as the anchor that we base all our other timezones off.  

UTC (or Coordinated Universal Time) is a *standard* timezone - it does not observe daylight saving.

We locate UTC in Alpha - Alpha Standard Time and UTC are the same time.  We can say that Alpha Standard Time is `UTC+00:00`.

Why have two timezones that cover the same timezone exactly?  The reason is that Alpha Standard Time may change in the future - for example, we may decide to shift AST to `UTC-01:00` - one hour behind UTC.  UTC avoids all this complication and will not change for any reason, making it a useful place to reference all other timezones from.

### Offset timezones

Our other two timezones covers our two villages - Alpha Standard Time at `UTC+00:00` and Omega Standard Time at `UTC+12:00`.

## `pytz`

`pytz` is used by many popular data science libraries (such as `pandas`) for timezone support.

This section covers:

- `pytz` and the `tz` database,
- naive versus aware timestamps,
- timezone localization versus timezone conversion.

`pytz` uses the *tz database* - a standardization of timezones that includes good support for timezones that are not constant offsets from UTC - such as daylight savings timezones (also known as *non-standard* timezones).

`pytz` attempts to model all timezones and their changes since 1970 - including daylight saving time and leap seconds.

An important technicality with the `tz` database (and by extension `pytz` and `pandas`) is that the `+/-` in the `GMT` offsets are *reversed* from the way offsets are defined for ISO 8061:

| pytz timezone | ISO 8061 UTC offset | 
|---------------|-------------------|
| ETC/GMT-10     | +10:00             | 
| ETC/GMT-2     | +02:00             | 
| ETC/GMT+0     | +00:00             | 
| ETC/GMT+2     | -02:00             | 
| ETC/GMT+10     | -10:00             | 

This reversal of sign can cause problems - especially with users that are used to the more common ISO8061 UTC offsets. 

### Naive vs Timezone Aware 

The Python `datetime` standard library has a small quirk - the function `.utcnow()` returns a timezone naive datetime:

```pyrepl
import datetime

datetime.datetime.utcnow().isoformat()
```

This timestamp, which is in the UTC timezone, is here a naive timestamp.

### How to make a timezone aware datetime object in Python?

We could make this timestamp *timezone-aware* by using the `pytz` library:


## Timezone Localization

Localization is used when you have a naive timezone, and you want to make it timezone aware.

We can start out creating a datetime using `utcnow`, which creates a timezone naive datetime:

```pyrepl
from datetime import datetime
dt = datetime.utcnow()
naive = dt.isoformat()
```

We can then localize this timezone to UTC, by creating a pytz timezone:

```pyrepl
import pytz

tz = pytz.timezone('UTC')
aware = tz.localize(dt)
```

This makes a datetime timezone aware - note the `Z` on the end of time timestamp now:

```pyrepl
aware.isoformat()
```

### Convert Timezones with `astimezone`

Timezone conversion is similar to localization - except in conversion we start with a timezone aware datetime.

In `pytz` conversion is done using the `astimezone` method:

```pyrepl
import datetime
import pytz

dt = pytz.timezone('UTC').localize(datetime.datetime.utcnow())
dt.astimezone(pytz.timezone('Pacific/Auckland'))
```

We can now see our datetime is timezone aware, by the inclusion of `+13:00` in the ISO 8061 timestamp:

```pyrepl
dt.isoformat()
```
