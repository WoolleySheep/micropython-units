# micropython-units
A lightweight library for representing physical quantities

## Example
    from units import Temperature, TemperatureDelta, TemperatureUnit

    temp = Temperature(50, TemperatureUnit.CELSIUS)
    temp2 = temp + TemperatureDelta(25, TemperatureUnit.KELVIN)  # Temperature(75, TemperatureUnit.CELSIUS)

## Purpose
Dealing with the units of physical quantities in SW is tricky. At best, developers adopt conventions to smooth the process, such as variable name postscripts (eg: `gauge_reading_kpa`), or a common unit that all values are translated into at the system boundaries. At worst, wires get crossed and the Mars Climate Orbiter burns up because NASA uses metric while Lockheed Martin uses imperial.

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

Unit-agnostic manipulation of physical quantities is also supported through two classes for each quantity type; <X> and <X>Delta. This approach is inspired by `datetime` and `timedelta` in cpython. This allows for arbitrarily large deltas, while ensuring that the physical quantities themselves always make sense.

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
### Testing
Pre-requisites
- Docker (https://www.docker.com/)

Steps
1. Download the micropython unix port image, then run it as a new container, binding the units repo
    
    docker run -it --name micropython-units-testing --network=host --mount type=bind,source=<PATH_TO_LOCAL_MICROPYTHON_UNITS_REPO>,target=/home --entrypoint bash micropython/unix:latest

2. Navigate to the repo directory

    cd ~/../home

3. Run micropython

    micropython

4. Install unittest & typing

    import mip

    mip.install("unittest")
    mip.install("github:Josverl/micropython-stubs/mip/typing.py")

5. Run unittests

    import unittest
    unittest.main("tests")
