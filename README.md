# micropython-units
A lightweight library for working with physical quantities

## Example
    from units import Temperature, TemperatureDelta, TemperatureUnit

    temp = Temperature(50, TemperatureUnit.CELSIUS)
    temp2 = temp + TemperatureDelta(25, TemperatureUnit.KELVIN)  # Temperature(75, TemperatureUnit.CELSIUS)
    temp2_in_frt = temp2.as_unit(TemperatureUnit.FAHRENHEIT)  # 167

## Purpose
Dealing with physical quantities in SW is tricky, because the same quantity can have different values depending on the unit used. While conventions exist to address this (such as using variable name postscripts that specify the unit, or adopting a single unit that all values should be converted to at the system boundary), these impose an additional cognitive load on developers. And when it goes wrong, wires get crossed and the Mars Climate Orbiter burns up because NASA uses metric while Lockheed Martin uses imperial.

This library aims to remove the cognitive load of managing units, by making physical quantities unit-agnostic. Units are only considered during object instantiation, and when the developer explicitly requests the quantity in terms of a specific unit.

    # Physical quantity enters the system and is immediately converted to a unit-agnostic form
    temp_in_celsius = read_sensor_value_in_celsius() # 26.0
    temp = Temperature(temp_in_celsius, TemperatureUnit.CELSIUS)

    ...

    # Pass a physical quantity around without worrying about the unit
    function_that_takes_a_temperature(temp)

    ...

    # Where the interface demands a specific unit, then easily extract the raw value
    temp_in_fahrenheit = temp.as_unit(TemperatureUnit.FAHRENHEIT)   # 78.8
    external_function_requiring_fahrenheit(temp_in_fahrenheit)

Unit-agnostic manipulation of physical quantities is also supported through two classes for each quantity type; <X> and <X>Delta. This approach is inspired by `datetime` and `timedelta` in CPython. This allows for arbitrarily large deltas, while ensuring that the physical quantities themselves always make sense.

    temp1 = read_temperature_sensor()   # Temperature(35, TemperatureUnit.CELSIUS)

    ...

    temp2 = read_temperature_sensor()   # Temperature(37, TemperatureUnit.CELSIUS)
    change_in_temp = temp2 - temp1      # TemperatureDelta(2, TemperatureUnit.CELSIUS)

    ...

    _ = TemperatureDelta(-400, TemperatureUnit.CELSIUS) # This is perfectly valid, as one temperature can be 400 degrees less than another
    _ = Temperature(-400, TemperatureUNIT.CELSIUS)   # This will throw an exception, as it's less than absolute zero and breaks physics


## Physical quantities supported (more to follow)
- Temperature

## For users
### How to install
    import mip

    mip.install("github:WoolleySheep/micropython-units")

For more information see [the office package management resource](https://docs.micropython.org/en/latest/reference/packages.html)

## For contributors
### Development
#### Pre-requisites
- uv[https://docs.astral.sh/uv/]
#### Linting
    uv run ruff check .\units
    uv run pylint .\units
#### Static type analysis
    uv run pyright .\units
#### Formatting
    uv run ruff format .\units .\tests

### Testing
Code that works in Python is not guaranteed to function the same (or at all) in micropython. As such tests should be run on the micropython unix port, using the micropython-variant of `unittest`.
#### Pre-requisites
- [Docker](https://www.docker.com/)
#### Steps
1. Download the micropython unix port image, then run it as a new container, binding the `micropython-units` repo
    ```
    docker run -it --name micropython-units-testing --network=host --mount type=bind,source=<PATH_TO_LOCAL_MICROPYTHON_UNITS_REPO>,target=/home --entrypoint bash micropython/unix:latest
    ```
2. Navigate to the repo directory
    ```
    cd ~/../home
    ```
3. Run micropython
    ```
    micropython
    ```
4. Install the `unittest` & `typing` dependencies
    ```
    import mip

    mip.install("unittest")
    mip.install("github:Josverl/micropython-stubs/mip/typing.py")
    ```
5. Run unit tests
    ```
    import unittest
    unittest.main("tests")
    ```

## Acknowledgements
This library was heavily inspired by the [C# UnitsNet package](https://github.com/angularsen/UnitsNet).
