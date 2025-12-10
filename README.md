# Python-Projects
A collection of projects built while working through the 100 Days of Code challenge.

![Python-projects](https://github.com/user-attachments/assets/2d577658-6535-4f0b-97b2-4c60278ccee1)

---

## Projects Covered

| Project | Description |
|---------------------|-------------|
| [Birthday Wisher](./Birthday%20Wisher) | Automatically sends personalized birthday wishes using Python scripts. |
| [Coffee Machine](./Coffee%20Machine) | Simulates a coffee vending machine with menu, resource management, and payment handling. |
| [Damien Hirst - Spot Painting](./Damien%20Hirst%20-%20Spot%20Painting) | Generates colorful spot paintings inspired by Damien Hirst using the Turtle module. |
| [Etch-A-Sketch](./Etch-A-Sketch) | Recreates the classic Etch-A-Sketch drawing toy as a Python application. |
| [Flash Cards](./Flash%20Cards) | A flashcard app to help users study and memorize information interactively. |
| [Hangman](./Hangman) | Classic word-guessing game where players try to guess the word before the hangman is drawn. |
| [Higher or Lower](./Higher%20or%20Lower) | A guessing game where users decide if the next number or follower count is higher or lower. |
| [Is ISS Overhead](./Is%20ISS%20Overhead) | Notifies the user when the International Space Station is overhead their location. |
| [Kanye Quotes](./Kanye%20Quotes) | Displays random Kanye West quotes using a GUI and API requests. |
| [Mail Merge](./Mail%20Merge) | Automates sending personalized emails by merging templates with data sources. |
| [Motivational Quote Automated-Mail](./Motivational%20Quote%20Automated-Mail) | Sends automated motivational quotes to your email on a schedule. |
| [NATO-alphabet](./NATO-alphabet) | Converts words to their NATO phonetic alphabet equivalents using Pandas. |
| [Password Manager](./Password%20Manager) | Securely stores, generates, and manages passwords with encryption and a master password. |
| [Pomodoro](./Pomodoro) | Implements a Pomodoro timer to boost productivity with work and break intervals. |
| [Pong Game](./Pong%20Game) | Classic Pong game where players control paddles to bounce a ball and score points. |
| [Quiz Game](./Quiz%20Game) | Interactive quiz game with multiple-choice questions and score tracking. |
| [Snake Game](./Snake%20Game) | Classic Snake game where the player grows the snake by eating food and avoids collisions. |
| [Squirrel Census (Data Analysis)](./Squirrel%20Census%20(Data%20Analysis)) | Analyzes real-world squirrel census data using Pandas to generate insights. |
| [Turtle Crossing Game](./Turtle%20Crossing%20Game) | Guide a turtle across a busy road, avoiding cars, with increasing difficulty. |
| [Turtle Race Game](./Turtle%20Race%20Game) | Simulates a turtle racing game where users can bet on the winning turtle. |
| [US States Guessing Game](./US%20States%20Guessing%20Game) | Guess US state names and see them appear on a map as you get them right. |
| [Blackjack](./Blackjack) | A simple version of the card game Blackjack, played against the computer. |
| [Caesar Cipher](./Caesar%20Cipher) | Encodes and decodes messages using the Caesar cipher encryption method. |
| [Calculator](./Calculator) | Basic calculator that can perform arithmetic operations. |
| [Guess my number](./Guess%20my%20number) | Number guessing game where the player tries to guess a randomly chosen number. |
| [Miles to Km converter](./Miles%20to%20Km%20converter) | Converts distances from miles to kilometers. |
| [Rock Paper Scissors](./Rock%20Paper%20Scissors) | Classic Rock, Paper, Scissors game against the computer. |
| [The Secret Auction Program](./The%20Secret%20Auction%20Program) | Simulates a secret auction where users submit bids anonymously. |
| [Treasure Island](./Treasure%20Island) | A text-based adventure game where choices lead to different outcomes on a treasure hunt. |

---
## Setting Up the Python Environment

To set up a project that requires external libraries not pre-installed on your local machine, follow this guide to isolate and install your dependencies.

### 1. Prerequisite Check

Ensure you have Python and pip installed. Run the following in your terminal:

```bash
python --version
pip --version
```

> **Note:** If you are on macOS or Linux and see an error, try using `python3` and `pip3` instead.

If they are missing, download and install them from the [official Python website](https://www.python.org/downloads/).

---

### 2. Create and Activate a Virtual Environment (Recommended)

This step creates an isolated folder (sandbox) for your project's libraries, preventing conflicts with other projects or your global system settings.

**First, create the environment:**

```bash
python -m venv venv
```

**Next, activate it:**

* **On Windows (Command Prompt/PowerShell):**
  ```powershell
  venv\Scripts\activate
  ```

* **On macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

> *You will know it worked when you see `(venv)` appear at the start of your command line.*

---

### 3. Install Dependencies

**Option A: Install from a list**
If your project includes a `requirements.txt` file, install all listed versions at once:

```bash
pip install -r requirements.txt
```

**Option B: Install a specific package**
To install a single library manually (replace `package_name` with the actual name, e.g., `requests` or `numpy`):

```bash
pip install package_name
```

---

### 4. Verification

To verify that your packages installed correctly, you can list all installed libraries in the current environment:

```bash
pip list
```
---

You’re now ready to run the project!  
If you encounter any issues, please refer to the documentation for the specific library or open an issue in this repository.

