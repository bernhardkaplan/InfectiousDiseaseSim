import matplotlib.pyplot as plt
import sys
import pandas as pd
import os

def plot_sim_data(fn, scale=1.):
    assert os.path.exists(fn)
    df = pd.read_csv(fn)
    t = df['t']
    x = df['x'] * scale
    y = df['y'] * scale
    z = df['z'] * scale
    w = df['w'] * scale

    fig, axes = plt.subplots(4, 1)

    ax = axes[0]
    ax.plot(t, x)
    ax.set_ylabel('x: infected')
    ax.set_xticklabels([])

    ax = axes[1]
    ax.plot(t, z)
    ax.set_ylabel('z: dead')
    ax.set_xticklabels([])

    ax = axes[2]
    ax.plot(t, w)
    ax.set_ylabel('w: recovered')
    ax.set_xticklabels([])

    ax = axes[3]
    ax.plot(t, y)
    ax.set_ylabel('y: healthy')
    ax.set_xlabel('Time')
    ax.set_xticklabels([])

    plt.show()


if __name__ == '__main__':

    print(len(sys.argv))
    if len(sys.argv) < 2:
        fn = 'corona_sim.csv'
    else:
        fn = sys.argv[1]

    scale = 1 #82 * 1e6
    plot_sim_data(fn, scale)

