# Discrete Signals labs

## Installation

To use the provided code, you will need to have the following dependencies installed:

- `numpy`
- `matplotlib`
- `sounddevice` (for `exo6_tp1.py` only)

You can install these dependencies using pip:

```
pip install numpy matplotlib sounddevice
```

## Usage

### `exo1_tp1.py`

This script plots two signals, `u=sin(pi/4*x)` and `v=cos(pi/4*x)`, on the same plot.

To run the script, simply execute the file:

```
python exo1_tp1.py
```

This will display the plot of the two signals.

### `exo2_tp1.py`

This script generates and plots four different signals: a Dirac pulse, a step signal, a rectangular window, and a Gaussian function.

To run the script, simply execute the file:

```
python exo2_tp1.py
```

This will display the four plots.

### `exo5_tp1.py`

This script performs various operations on two signals, `u=sin(pi/4*x)` and `v=cos(pi/4*x)`, including addition, multiplication, gating, and inversion.

To run the script, simply execute the file:

```
python exo5_tp1.py
```

This will display the plots of the resulting signals.

### `exo6_tp1.py`

This script generates a melody by playing a sequence of musical notes from A4 to the next G#.

To run the script, simply execute the file:

```
python exo6_tp1.py
```

This will play the melody and display a plot of the frequencies of the musical notes.

## API

The code in these files uses the following APIs:

- `numpy`: for numerical operations
- `matplotlib.pyplot`: for plotting the signals
- `sounddevice` (for `exo6_tp1.py` only): for playing the melody

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the project's repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

No specific testing framework is used in these code files. However, you can run the scripts and visually inspect the resulting plots to ensure they are working as expected.
