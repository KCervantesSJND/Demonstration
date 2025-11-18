import numpy as np
import matplotlib.pyplot as plt

# set default random number generator
# seed is reproducable
rng = np.random.default_rng(2025)

# number of simulations to run
N = int(1e7)

# first value is the number of trials
# second is the cummulative mean
def plotValues(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    p = arr.cumsum()
    q = np.arange(len(arr)) + 1
    return q, p / q

## simulate N rolls of dice
samp = (
    rng
    .integers(1, 7, (2, N))
    .sum(axis = 0)
)

## find data on how many times 7 occurs
x, y = plotValues(samp == 7)

fig, ax = plt.subplots()

## plots the actual probability as a flat line
ax.axhline(1 / 6, color = "tab:orange")

ax.plot(x, y)
ax.set_xlabel("Number of Trials")
ax.set_xscale("log", base = 10)
ax.set_ylabel("Relative Frequency")
ax.set_title("Rolling a 7 with a Pair of Dice")

plt.savefig("plot.png")