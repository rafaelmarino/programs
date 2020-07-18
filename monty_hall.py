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
    random.seed(42)
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
    staying_wins, switching_wins = simulate(n)
    cumsum_sticking = np.cumsum(staying_wins)
    cumsum_switching = np.cumsum(switching_wins)
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(range(1, len(cumsum_switching) + 1), cumsum_switching, \
        marker='o', ls="", label= "Switching Strategy", color='#482677FF')
    plt.plot(range(1, len(cumsum_sticking) + 1), cumsum_sticking, \
        marker='v', ls="", label= "Staying Strategy", color='#29AF7FFF')
    plt.title('Monty Hall Simulation - Cumulative Wins', fontsize=18)
    ax.set_ylabel("Cumulative Wins", fontsize=15, style='italic')
    ax.set_xlabel("Number of Trials", fontsize=15, style='italic')
    # plt.xticks(np.arange(1, len(cumsum_sticking), 9))
    # ax.get_xticks()
    plt.legend(fontsize=14)
    plt.savefig('images/cumulative_wins.png')
    plt.show()
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
    # extract the vector of binary win results
    staying_wins, switching_wins = simulate(n)
    # compute the cumulative wins
    cumsum_sticking = np.cumsum(staying_wins)
    cumsum_switching = np.cumsum(switching_wins)
    # compute the cumulative win probabilities
    cumprob_sticking = cumsum_sticking/np.arange(1, n + 1)
    cumprob_switching = cumsum_switching/np.arange(1, n + 1)
    # plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    # plt.style.use('dark_background')
    plt.plot(range(1, len(cumprob_switching) + 1), cumprob_switching, \
        marker='', ls="-", label= "Switching Strategy", color='#482677FF')
    plt.plot(range(1, len(cumprob_sticking) + 1), cumprob_sticking, \
        marker='', ls="-", label= "Staying Strategy", color='#29AF7FFF')
    # horizontal lines
    plt.axhline( 1/3, ls='--', color='black')
    plt.axhline( 2/3, ls='--', color='black')
    # plot and axes labels
    plt.title('Monty Hall Simulation - Law of Large Numbers', fontsize=18)
    ax.set_ylabel("Win Probability", fontsize=15, style='italic')
    ax.set_xlabel("Number of Trials", fontsize=15, style='italic')
    # two decimals on the y axis labels
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.text(len(cumprob_switching)*0.95, 0.66+0.05, '2/3', \
        style='italic', fontsize=12)
    plt.text(len(cumprob_sticking)*0.95, 0.33-0.05, '1/3', \
        style='italic', fontsize=12)
    plt.legend(fontsize=14)
    plt.savefig('images/lln.png')
    plt.show()
    return


if __name__ == "__main__":
    # interesting seeds: 50
    plot_cumulative_wins(100)
    plot_lln(1000)
