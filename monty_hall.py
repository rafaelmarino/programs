import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def simulate(n_rounds=100):
    """
    Simulate Monty Hall games.

    Args:
        n_rounds: number of rounds to play
    Returns:
        staying_wins: list with n_round binary results, 1s are wins.
        switching_wins: list with n_round binary results, 1s are wins.
    """
    random.seed(99)
    door_set = {1, 2, 3}  # set of all doors
    staying_wins = []
    switching_wins = []
    for _ in range(n_rounds):
        prize_door = random.randint(1, 3)
        choice = random.randint(1, 3)  # player's choice
        # staying strategy:
        if choice == prize_door:
            staying_wins.append(1)
        else:
            staying_wins.append(0)
        # switching strategy:
        # the presenter may or may not have a choice:
            # if prize_door == players choice, 2 doors to choose from
            # else, there's only one door left
        host_choice = random.choice(list(door_set - {choice, prize_door}))
        new_choice = (door_set - {choice, host_choice}).pop()
        if new_choice == prize_door:
            switching_wins.append(1)
        else:
            switching_wins.append(0)
    return staying_wins, switching_wins


def plot_cumulative_wins(n):
    """
    Plot the number of cumulative wins for a Monty Hall simulation.

    Args:
        n: desired number of Monty Hall simulation rounds.
    Returns:
        Plot with cumulative wins under Switching and Sticking Strategies.
    """
    # original colors: [, ]
    staying_wins, switching_wins = simulate(n)
    cumsum_sticking = np.cumsum(staying_wins)
    cumsum_switching = np.cumsum(switching_wins)
    # plt.style.use('seaborn-whitegrid')
    fig = plt.figure(figsize=(10, 6), dpi=80)
    ax = fig.gca()
    plt.plot(range(1, len(cumsum_switching) + 1), cumsum_switching,
             marker='o', ls="", label="Switching Strategy", color='#482677FF')
    plt.plot(range(1, len(cumsum_sticking) + 1), cumsum_sticking,
             marker='v', ls="", label="Staying Strategy", color='#29AF7FFF')
    plt.xticks(np.arange(0, len(cumsum_sticking) + 1, 10))
    plt.title('Monty Hall Simulation - Cumulative Wins', fontsize=18,
              color='black')
    ax.set_ylabel("Cumulative Wins", fontsize=16, style='italic',
                  color='black')
    ax.set_xlabel("Number of Trials", fontsize=16, style='italic', 
                  color='w')
    ax.tick_params(axis="x", labelsize=14, labelcolor="black", color="black")
    ax.tick_params(axis="y", labelsize=14, labelcolor="black", color="black")
    # spines
    # ax.spines['bottom'].set_color('w')
    # ax.spines['top'].set_color('w')
    # ax.spines['right'].set_color('w')
    # ax.spines['left'].set_color('w')
    # legend
    leg = plt.legend()
    for text in leg.get_texts():
        text.set_color("black")
        text.set_fontsize(16)
    # for line, text in zip(l.get_lines(), l.get_texts()):
    #     text.set_color(line.get_color())
    #     text.set_fontsize(16)
    # grid
    ax.grid(axis="x", color="black", alpha=.3, linewidth=1, linestyle=":")
    ax.grid(axis="y", color="black", alpha=.3, linewidth=1, linestyle=":")
    plt.savefig('images/cumulative_wins_l.png', facecolor=fig.get_facecolor())
    # plt.show()
    return


def plot_cumulative_wins_dark(n):
    """
    Plot the number of cumulative wins for a Monty Hall simulation.

    Args:
        n: desired number of Monty Hall simulation rounds.
    Returns:
        Plot with cumulative wins under Switching and Sticking Strategies.
    """
    # original colors: ['#482677FF', '#29AF7FFF']
    staying_wins, switching_wins = simulate(n)
    cumsum_sticking = np.cumsum(staying_wins)
    cumsum_switching = np.cumsum(switching_wins)
    # plt.style.use('seaborn-whitegrid')
    bg_color = "#002038"
    fig = plt.figure(figsize=(10, 6), dpi=80, facecolor=bg_color)
    ax = fig.gca()
    ax.set_facecolor(bg_color)
    plt.rcParams["legend.facecolor"] = bg_color
    plt.plot(range(1, len(cumsum_switching) + 1), cumsum_switching,
             marker='o', ls="", label="Switching Strategy", color='#82c3c8')
    plt.plot(range(1, len(cumsum_sticking) + 1), cumsum_sticking,
             marker='v', ls="", label="Staying Strategy", color='#d39aeb')
    plt.xticks(np.arange(0, len(cumsum_sticking) + 1, 10))
    plt.title('Monty Hall Simulation - 100 Games', fontsize=18,
              color='w')
    ax.set_ylabel("Cumulative Wins", fontsize=16, style='italic', color='w')
    ax.set_xlabel("Trials", fontsize=16, style='italic', color='w')
    ax.tick_params(axis="x", labelsize=14, labelcolor="w", color="w")
    ax.tick_params(axis="y", labelsize=14, labelcolor="w", color="w")
    # spines
    ax.spines['bottom'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.spines['right'].set_color('w')
    ax.spines['left'].set_color('w')
    # legend
    leg = plt.legend()
    for text in leg.get_texts():
        text.set_color("w")
        text.set_fontsize(15)
    # for line, text in zip(l.get_lines(), l.get_texts()):
    #     text.set_color(line.get_color())
    #     text.set_fontsize(16)
    # grid
    ax.grid(axis="x", color="w", alpha=.3, linewidth=1, linestyle=":")
    ax.grid(axis="y", color="w", alpha=.3, linewidth=1, linestyle=":")
    plt.savefig('images/cumulative_wins.png', facecolor=fig.get_facecolor())
    # plt.show()
    return


def plot_lln(n):
    """
    Plot the cumulative probability wins to show the Law of Large Numbers.

    Args:
        n: desired number of Monty Hall simulation rounds.
    Returns:
        Plot with cumulative probability of winning under Switching and
        Sticking Strategies.
    """
    staying_wins, switching_wins = simulate(n)  # run the simulation
    # compute the cumulative wins
    cumsum_sticking = np.cumsum(staying_wins)
    cumsum_switching = np.cumsum(switching_wins)
    # compute the cumulative win probabilities
    cumprob_sticking = cumsum_sticking/np.arange(1, n + 1)
    cumprob_switching = cumsum_switching/np.arange(1, n + 1)
    # dark theme
    bg_color = "#002038"
    fig = plt.figure(figsize=(10, 6), dpi=80, facecolor=bg_color)
    ax = fig.gca()
    ax.set_facecolor(bg_color)
    plt.rcParams["legend.facecolor"] = bg_color
    plt.plot(range(1, len(cumprob_switching) + 1), cumprob_switching,
             marker='', ls="-", label="Switching Strategy", color='#82c3c8')
    plt.plot(range(1, len(cumprob_sticking) + 1), cumprob_sticking,
             marker='', ls="-", label="Staying Strategy", color='#d39aeb')
    # horizontal lines
    plt.axhline(1/3, lw=1, ls='--', color='w')
    plt.axhline(2/3, lw=1, ls='--', color='w')
    # plot and axes labels
    plt.title('Monty Hall Simulation - Law of Large Numbers',
              fontsize=18, color='w')
    ax.set_ylabel("Win Probability", fontsize=16, style='italic', color='w')
    ax.set_xlabel("Trials", fontsize=16, style='italic', color='w')
    ax.tick_params(axis="x", labelsize=14, labelcolor="w", color="w")
    ax.tick_params(axis="y", labelsize=14, labelcolor="w", color="w")
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # 2 decimals
    # plt.text(len(cumprob_switching)*0.95, 0.66+0.05, '2/3',
    #          style='italic', fontsize=13, color='w')
    plt.text(n*1.06, 0.66, '2/3', style='italic', fontsize=13, color='w')
    plt.text(n*1.06, 0.33, '1/3', style='italic', fontsize=13, color='w')
    # plt.legend(fontsize=14)
    # spines
    ax.spines['bottom'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.spines['right'].set_color('w')
    ax.spines['left'].set_color('w')
    # legend
    leg = plt.legend()
    for text in leg.get_texts():
        text.set_color("w")
        text.set_fontsize(15)
    # for line, text in zip(l.get_lines(), l.get_texts()):
    #     text.set_color(line.get_color())
    #     text.set_fontsize(16)
    # grid
    ax.grid(axis="x", color="w", alpha=.3, linewidth=1, linestyle=":")
    ax.grid(axis="y", color="w", alpha=.3, linewidth=1, linestyle=":")
    plt.savefig('images/lln.png', facecolor=fig.get_facecolor())
    # plt.show()
    return


if __name__ == "__main__":
    # interesting seeds: 50
    plot_cumulative_wins(100)
    plot_cumulative_wins_dark(100)
    plot_lln(1000)
