---
title: Working with Time
description: Learn to handle dates, times, and timezones in data analysis and programming.
date_created: 2025-08-27
date_updated: 2025-08-27
competencies:
- "Analytics"
- "Software Engineering"
draft: true
---

## Why Learn About Time?

Time is used everywhere - most datasets have a time dimension in at least one column (such as `last_modified_utc`).

## Why is Time Challenging?

Time is complex - it can be represented in many different ways, and is not straightfoward to work with, especially when you do not control how the dates or times are represented.

Time is challenging because so many things are arbitrary - where timezones are, if daylight saving applies or not - all these things are conventions that are arbitrary but consistent.

Working with time requires gaining a certain amount of *boilerplate knowledge*, such as:

- The format code for year is `%Y`
- What ISO861 is
- What `strptime` and `strftime` do

This boilerplate, *you just need to remember how to do it* knowledge is a huge part of being able to work with time well.

## What is a Date?

A date is made of a year, month and day:

```python
import datetime
datetime.date(2020, 1, 1)
```

We can access the elements of our `date` object as attributes, like for year using `.year`:

```python
dt = datetime.date(2020, 1, 1)
dt.year
```

And day using `.day`:

```python
dt.day
```


## What is a Time?

A time is made of hours, minutes and seconds:

```python
import datetime
datetime.time(12, 30, 0)
```

We can access the elements of our `time` object as attributes, the same as we did for our `date`. We can access the hour using `.hour`:

```python
dt = datetime.time(12, 30, 0)
dt.hour
```

And minute using `.minute`:

```python
dt.minute
```

## What is a Datetime?

A datetime is a combination of the two objects we have been looking at - **a date and a time**.

We can create a `datetime` object from scratch, using the same syntax as for dates and times:

```pyrepl
import datetime
datetime.datetime(2050, 12, 25, 18, 30)
```

We can access the elements of our `datetime` object (such as the year) with the same attribute syntax as `date` or `time`:

```pyrepl
import datetime
dt = datetime.datetime(2050, 12, 25, 18, 30)
dt.year
```

## Combine

The `combine` method of the `datetime` *object* in the `datetime` *module* (hence the `datetime.datetime`) allows us to create a `datetime` object from a `date` and a `time`:

```pyrepl
import datetime

datetime.datetime.combine(datetime.date(2020, 1, 1), datetime.time(12, 30))
```

## Replace

The `replace` method allows changing the attributes of a `datetime` object, such as changing the year:

```pyrepl
import datetime

dt = datetime.datetime(2020, 1, 1, 12, 30)
dt.replace(year=2021)
```

## Getting the Current Time

We can get a Python object representing the current time using your computer clock:

```pyrepl
import datetime
datetime.datetime.today()
```

We can also get the current time in the UTC timezone using `datetime.datetime.utcnow()`, which also returns a `datetime` object, but in UTC time.

Both `utcnow` and `today` return objects that are timezone naive (they have no timezone attached to them).

## Datetime Representations

The datetime representations we have looked at are **partitioned representations** - each element of the datetime is stored in it's own space (such as the year or month) - each element is an integer component of time.

An alternative representation of a datetime is an **offset representations** - offset from anchor (such as seconds since UNIX epoch).

## UNIX Time

The UNIX time is an numeric representation of time - it is the number of seconds that have elapsed since the *UNIX epoch* (arbitrary set at 1st January 1970).

You can get a UNIX timestamp of the current time using `time.time`:

```pyrepl
import time
time.time()
```

If you ever see a long float or integer in a datetime column, it is likely UNIX time.

## Timedeltas

The `timedelta` allows us to create offsets from `datetime` objects, such as one hour ahead:

```pyrepl
import datetime

dt = datetime.datetime(2020, 1, 1, 12, 30)
dt + datetime.timedelta(hours=1)
```

Timedeltas are useful when you want to transform a date by a fixed length of time - such as the same time the next day:

```pyrepl
import datetime
datetime.datetime(2020, 1, 1, 12, 30) + datetime.timedelta(hours=24)
```


## Datetime Strings and Objects

### Motivation - Why a section on strftime and strptime?

Much of working with data follows a process of:

```
data on disk -> data in memory -> data on disk
```

This process can also be redrawn with the types of the data:

```
string -> object -> string
```

These two operations (`string -> object` and `object -> string`) are so common in data work that Python includes it's own mini-language for doing these transformations.

They are also impossible to remember which is which!

- string -> datetime object = strptime = parser
- datetime object + format code -> string = strftime = formatter

### Strings versus objects

Understanding the difference between `strftime` and `strptime` requires understanding the difference between a Python *string* and *object*.

With a string, what you see is what you get.  While the Python string also has additional data (class attributes) and functionality (class methods), a string is a straightforward piece of data.  

A Python object can be arbitrary complex - it can have all sorts of crazy methods (functionality) and attributes (data).  An object is much more than what it appears on the surface.

The complexity with this distinction is that *technically*, a Python string *is* also Python object. However, a string that lives in a text file (such as in a CSV or JSON file) is not a Python object - even if the piece of data that string becomes in Python, is an object ^^

A string is a concrete representation - its a simple, what you see is what you get representation of time.  That's not to say everything is clear - the meaning datetime string can be ambigious, even if it can be clearly read.  

## Datetime Strings versus Datetime Objects

We can create different representations of the same datetime as both an object and a string.

First we can create a Python `datetime` object:

```pyrepl
import datetime
dt = datetime.datetime(2020, 12, 25, 18, 30)
```

This representation of the datetime lives inside a Python process in memory - it's a Python object, that has data and functionality beyond just showing the datetime.  What we see above is what we get when we `print` an object - it's `__repr__` method.

If we wanted to store or read this piece of data in a text file (like a CSV or JSON file), we need to transform this Python `datetime` object into a string.


### Representing datetimes as strings

There are many ways to represent a datetime as a string - commonly in data work you should use ISO8061 as much as possible.  ISO8061 is a standard for formatting of datetime strings.

A good habit to set is to use ISO 8601 wherever possible - most libraries will handle ISO 8601 formatted data without any additional effort.

The Python `datetime` object has a `isoformat` method which will create an ISO8061 formatted string:

```pyrepl
import datetime
dt = datetime.datetime(2020, 12, 25, 18, 30)
dt.isoformat()
```

Likewise we can use `fromisoformat` to create a datetime from an ISO8061 formatted string:


```pyrepl
import datetime
datetime.datetime.fromisoformat('2020-12-25T18:30:00')
```

## ISO 8061

The ISO 8061 format specifies that dates look like `YEAR-MONTH-DAY` (`YYYY-MM-DD`), with a `-` separator:

```
2022-01-24

%Y-%m-%d
```

ISO8071 uses a `T` to separate the date from the time, with a `:` separator for the time components:

```
2022-01-24T23:51:45

%Y-%m-%dT%H:%M:%S
```

Timezones

```
2022-01-24T23:51:45+0200

%Y-%m-%dT%H:%M:%S%z
```

## Format Codes 

There are lots of different ways to format datetimes as strings - format codes allow us to start to make sense of how to structure a datetime as a string.

Let's stick with our familiar datetime of Christmas 2050:

```pyrepl
import datetime
dt = datetime.datetime(2020, 12, 25, 18, 30)
```

Let's start with a few format codes weekday `%A`, day `%d` and month `%B`.

We can use format codes to define how we want our datetime string to look - combined with the `strftime` function we can create a datetime string:

```pyrepl
dt.strftime('%A %d of %B')
```

## `strftime` 

`strftime` creates strings from datetime objects.

We can change the string we produce with `strftime` by changing the format code for month:

```pyrepl
dt.strftime('%A %d of %m')
```

We can also include the year:

```pyrepl
dt.strftime('%A %d of %B of %Y')
```

For the day to day work of a data professional, we hope familiarity with that the following format codes for 

For a full list of format codes, check out the [Python strftime cheat sheet](https://strftime.org/).  For an interactive experience, check out [strftime reference and sandbox](https://www.strfti.me/).


## `strptime`

`strptime` parses datetime objects from strings.

So far we have focused on creating strings from our datetime objects.  What if we have the opposite - we have a string and want to make a datetime object?

We can do this using `strptime` - which strips the datetime from a string:

```pyrepl
import datetime

dt = datetime.datetime(2020, 12, 25, 18, 30)
fmt = '%A %d of %B of %Y'
dt = dt.strftime(fmt)
st = datetime.datetime.strptime(dt, fmt)
```

## `strptime` parses datetime objects from strings

So far we have focused on creating strings from our datetime objects.  What if we have the opposite - we have a string and want to make a datetime object?

We can do this using `strptime` - which strips the datetime from a string:

```pyrepl
import datetime

dt = datetime.datetime(2020, 12, 25, 18, 30)
fmt = '%A %d of %B of %Y'
dt = dt.strftime(fmt)
st = datetime.datetime.strptime(dt, fmt)
```

## Practical Tips

Use UTC everywhere

Consider a `_utc` suffix

Understand how your database stores timestamps and timezones.

## Why Learn About Timezones?

Timezones are a modern problem.

Our ability to communicate & travel over large distances means requires us to reference time all across the planet - past, present and future, in many locations.

Daylight savings introduces even more complexity to the timezone problem - daylight saving means that a single location can have multiple timezones in one year.

While timezones and daylight savings are complex, they are an undeniably important part of working with data.

Mastering them is well within your capability - hence this lesson.

## Why Timezones are Hard

Timezones force us to do something unnatural - consider the **same point in time** in **different places**.

Timezones are arbitrary - where we draw timezone boundaries is a political decision.  China for example has only a single timezone.

Timezones can change - cities can change from timezone to another, due to either daylight savings or a change of timezone.

## Advice for Working with Timezones

Make the decision early on about whether you need to support multiple timezones.

Stick to one timezone if you can - if your entire business is within a single timezone, use this to your advantage!  You may even be able to use timezone naive timestamps.

Use standard timezones (timezones that do not observe daylight saving) where possible.

[Default to UTC - even if it's not a silver bullet](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/).  Consider storing the timezone alongside a UTC timestamp.

Consider storing the elements of the datetime (such as year or day) as separate columns (which we know know is a partitioned representation).

## What is a Timezone?

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

## Working with Timezones in Python

This section is focused on how to work with timezones in Python.

We will be using the `pytz` library - which is not part of the Python standard library, but is used by many popular data science libraries (such as `pandas`).

This section covers:

- `pytz` and the `tz` database,
- naive versus aware timestamps,
- timezone localization versus timezone conversion,
- 
## `pytz`

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

### Naive versus timezone aware timestamps

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


## How to Convert Timezones with `astimezone`

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

## Why Daylight Saving is Hard

Like timezones, daylight savings is hard because it forces us to do something unnatural - consider the same point in time at different places.

Daylight savings is also hard because it forces us to do something unnatural - consider a discontinuity in time.  Daylight savings means we end up with both missing and duplicate timestamps.


## Standard versus Non-Standard Timezones

An important distinction in timezones is the difference between standard timezones (which are not affected by daylight savings) and non-standard timezones (where daylight is in effect).

## Advice for Working with Daylight Saving

Where possible - don't!  A **standard** timezone is a timezone that is unaffected by daylight saving, such as UTC, or Australian Eastern Standard Time (AEST).

## Daylight Saving

Let's return to the plant we explored in our section on timezones.  Our planet has two villages - Alpha and Omega - and three timezones:

- Coordinated Universal Time (UTC+00:00).
- Alpha Standard Time (UTC+00:00),
- Omega Standard Time (UTC+12:00),

Omega is located far to the south where the summer days are much longer than the days in winter.

This seasonal pattern means that for the same time of the day (like 1200 or 1800) the sun is in a very different position at different times of the year.

Omega decides to implement a daylight saving time - decide to maintain two timezones - one timezone we follow in the summer, one timezone we follow in the winter.

We now end up with:

- Coordinated Universal Time (UTC+00:00).
- Alpha Standard Time (UTC+00:00),
- Omega Standard Time (UTC+12:00),
- Omega Daylight Time (UTC+13:00).

## The Consequences of Daylight Saving

To demonstrate the consequences of our decision to maintain two timezones, we will use `pytz` to generate the what happens in the daylight savings days:

- one short (23 hour) day with missing times,
- and one long (25 hour) day with duplicate times.

Let's look what happens during spring, when we transition from winter to summer.  

We will use `pandas` to do this: 

```pyrepl
from datetime import date, timedelta
dt = date.fromisoformat('2020-09-27')

df = pd.DataFrame({
    'datetime': pd.date_range(
        dt, dt + timedelta(days=1), freq='H', tz='Pacific/Auckland'
    )
})
print(df.shape)
print(df.head(10))
```

For this timezone, daylight saving currently commences on:

- the last Sunday in September, when 2.00am becomes 3.00am, 
- ends on the first Sunday in April, when 3.00am becomes 2.00am.

2020
  Sun, Apr 5, 2020 3:00 AM
- begins 0200 Sunday 27 Sept


Let's look what happens during autumn, when we transition from summer to winter:

```pyrepl
df = df.set_index('datetime')
df['2020-05-05': '2020-04-06']
```

And in the transition from winter to summer:

```pyrepl
df['2020-09-27': '2020-09-27']
```
