# micropython-units
A lightweight library for working with physical quantities

## Example
```python
from units import Temperature, TemperatureDelta, TemperatureUnit

temp = Temperature(50, TemperatureUnit.CELSIUS)
temp2 = temp + TemperatureDelta(25, TemperatureUnit.KELVIN)  # Temperature(75, TemperatureUnit.CELSIUS)
temp2_in_frt = temp2.as_unit(TemperatureUnit.FAHRENHEIT)  # 167
```

## Purpose
Dealing with physical quantities in SW is tricky, as the same quantity can have different values depending on the unit used. While conventions exist to address this (such as including units in variable/function names, or adopting a single unit that all physical quantities of a type should be converted to at the system boundary), these impose an additional cognitive load on developers. And when it goes wrong, wires get crossed and the Mars Climate Orbiter burns up because NASA uses metric while Lockheed Martin uses imperial.

## Implementation

### High-level
This library aims to remove the cognitive load of managing units, by making physical quantities unit-agnostic. Units are only considered during object instantiation, and when the developer explicitly requests the quantity in terms of a specific unit.
```python
# Physical quantity enters the system and is immediately converted to a unit-agnostic form
pressure_in_pascal = read_sensor_value_in_pascal() # 102110.0
pressure = Temperature(pressure_in_celsius, PressureUnit.PASCAL)

...

# Pass a physical quantity around without worrying about the unit
function_that_takes_a_pressure(pressure)

...

# Where the interface demands a specific unit, then get the raw value
pressure_in_psi = pressure.as_unit(PressureUnit.POUND_PER_SQUARE_INCH)   # 14.8098...
external_function_requiring_psi(pressure_in_psi)
```

### Physical quantities
Unit-agnostic manipulation & comparison of physical quantities is also supported through a pair of classes for each quantity type; `PHYSICAL_QUANTITY` and `PHYSICAL_QUANTITY_Delta`. This approach is inspired by `datetime` and `timedelta` in CPython. This allows for arbitrarily large/small/negative differences, while ensuring that the physical quantities themselves always make sense.
```python
pressure1 = read_pressure_sensor()   # Pressure(1.1, PressureUnit.ATMOSPHERE)

...

pressure2 = read_pressure_sensor()   # Pressure(1.3, PressureUnit.ATMOSPHERE)
change_in_pressure = temp2 - temp1      # PressureDelta(0.2, PressureUnit.ATMOSPHERE)

...

_ = TemperatureDelta(-400, TemperatureUnit.CELSIUS) # This is perfectly valid, as one temperature can be 400 degrees less than another
_ = Temperature(-400, TemperatureUNIT.CELSIUS)   # This will throw an exception, as it's less than absolute zero and breaks physics
```

### Rates of change
Often the rate at which a physical quantity is changing is what is of interest. Rates of change are similar to `PHYSICAL_QUANTITY_Delta` classes but they take an extra `TimeDelta` parameter in their constructor.
```python
current_flow_rate = VolumetricFlowRate(5.5, VolumeUnit.MILLILITER, TimeUnit.MINUTE)
set_pump_speed(current_flow_rate)
```

## Units supported supported (more to follow)
- Physical quantities
    - Pressure
    - Temperature
    - Volume
    - Time
- Rates of change
    - Volumetric Flow Rate

## For users
### How to install
```python
    import mip

    mip.install("github:WoolleySheep/micropython-units")
```

For more information see [the office package management resource](https://docs.micropython.org/en/latest/reference/packages.html)

## For contributors
### Development
#### Pre-requisites
- [uv](https://docs.astral.sh/uv/)
#### Linting
    uv run ruff check .\units
    uv run pylint .\units
#### Static type analysis
    uv run pyright .\units
#### Formatting
    uv run ruff format .\units .\tests
#### Updating dependencies
    uv lock --upgrade

### Testing
#### Running unit tests on the micropython unix port
Code that runs in CPython is not guaranteed to function the same (or at all) in micropython. As such tests should be run on the micropython unix port, using the micropython-variant of `unittest`.
##### Pre-requisites
- [Docker](https://www.docker.com/)
##### Steps
1. Download the micropython unix port image, then run it as a new container, binding the `micropython-units` repo
    ```
    docker run -it --name micropython-units-testing --network=host --mount type=bind,source=<PATH_TO_LOCAL_MICROPYTHON_UNITS_REPO>,target=/home --entrypoint bash micropython/unix:latest
    ```
2. Navigate to the repo directory
    ```
    cd ~/../home
    ```
3. Activate the micropython unix port
    ```
    micropython
    ```
4. Install the `unittest` & `typing` dependencies
    ```python
    import mip

    mip.install("unittest")
    mip.install("github:Josverl/micropython-stubs/mip/typing.py")
    ```
5. Run unit tests
    ```python
    import unittest
    unittest.main("tests")
    ```
#### Test coverage report
A test coverage report can be generated to ensure the unit tests are exercising the anticipated functionality. The coverage module is designed for CPython, not micropython, so it may not be entirely accurate.
##### Pre-requisites
- [uv](https://docs.astral.sh/uv/)
##### Steps
1. Generate the coverage report
    ```
    uv run coverage run -m unittest
    ```
2. Display the coverage report in html format
    ```
    uv run coverage html
    ```

## Acknowledgements
This library was heavily inspired by the [C# UnitsNet package](https://github.com/angularsen/UnitsNet).
