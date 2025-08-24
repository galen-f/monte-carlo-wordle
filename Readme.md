# 🎲 Monte Carlo Wordle
This project used the game wordle to explain one of the most important tools I learned in statistics and quantitative finance: **Monte Carlo** simulations.

<hr>

## What is Monte Carlo?
Named after the famous Monegasque casino, Monte Carlo is a way of simulating uncertainty. Take the principle that playing roulette 1000 times would start to reveal just how rigged the game is, we can play 1000 games of Wordle to figure out just how good our opener word is.

**Simply put** we can measure a slice of random events to get a reasonably accurate understanding of the odds of success and failure in an uncertain environment.

<hr>

## In Finance
Finance is *full* of uncertainty. Nobody knows how markets, interest rates, or economies will behave in the future. Monte Carlo simulations give us a way to explore infinite possibilities instead of pretending we know just one.

Here's what that looks like in practice:

- **Retirement planning:**
Instead of saying "I'll have $XX.xx at the age of 65", we simulate thousands of market paths (booms, crashes, etc.) to say *"In 80% of scenarios I have enough to retire at 65, in 20% I need to adjust"*

- **Risk Management:**
Banks use Monte Carlo to estimate how much they could lose in extreme cases. For instance answering questions like "What is the probability we lose more than $10 million in one day?"

- **Investment Strategy Testing:**
If a strategy only works in *perfect* scenarios but fails miserably in downturns, Monte Carlo reveals that.

<hr>

## Why does this matter to everyone?
Because Monte Carlo encourages you to think in probabilities, not certainties.
❌ "This will happen".
✅ "This *could* happen, and here is how likely it is".


## What's in this repo
- **Monte_Carlo_Wordle_Demo.ipynb** walks you through solving Wordle with a Monte Carlo engine.
- **Count_Letters.py** runs through all possible Wordle words and notes how often each letter appears and where.
- **Score_Words.ipynb** measures every possible word with how well it fits the frequency of letters, then assigns it a score.
- **Simulator.ipynb** simulates Wordle games for all top scoring words, producing a list of the best performers.

- **./data**
    - **answers.txt** is a list of all possible Wordle solutions.
    - **guesses.txt** is a list of all valid Wordle guesses.
    - **letter_count.txt** holds data outputted by count_letters.py
    - **top_words.txt** is a list of the top scoring words, produced by score_words
    - **results.csv** is a list of the top performers created by the simulator along with their stats.

## How to run
1. Clone the repo.
2. Open the notebook in Jupyter or VSCode.
3. Run all cells.

**You'll see:**
- The chance of solving in 6 or fewer guesses.
- The average number of guesses.