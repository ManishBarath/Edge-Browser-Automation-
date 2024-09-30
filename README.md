#Bing Search Automation Script
Got tired by searching daily in microsoft edge browser for getting microsoft rewords.....I got you!
This project automates Bing Rewards search tasks using Playwright. The script logs into a Bing account, navigates to the rewards page, and performs a series of searches based on a predefined list of anime titles and games.

#Features
Automates Bing sign-in.
Performs search tasks from a predefined list of anime and games.
Interacts with the Bing rewards page and tracks search completions.

#Prerequisites

Before running the script, ensure you have the following installed on your system:

Python 3.7+
Playwright (for Python)
Microsoft Edge (Chromium) (optional, used in the script for browser automation)

#Installation
Clone the repository:
git clone https://github.com/yourusername/bing-search-automation.git
cd bing-search-automation

Install dependencies:

Install Playwright and its dependencies by running:

pip install playwright
Install Playwright browsers:

After installing the Playwright package, you need to install the required browsers:

playwright install
Environment Variables
Create a .env file (or export environment variables) in the root of the project to store your Bing login credentials:

BING_EMAIL=your_email@example.com
BING_PASSWORD=your_password
Alternatively, you can define them directly in the script or as environment variables in your terminal session.

#Usage
Run the script:

To run the script, execute the following command:
python bing_search_automation.py
#Script Flow:

The browser will launch and navigate to the Bing Rewards page.
It will prompt you to log in using your Bing email and password.
The script will then automate a series of searches for predefined anime and game titles to collect Bing rewards.
Search Terms
The script searches for a predefined set of terms related to anime and games, such as:

Anime: "Naruto", "Bleach", "One Piece", "Hunter x Hunter", etc.
Games: "The Legend of Zelda: Breath of the Wild", "Red Dead Redemption 2", "Minecraft", etc.
You can modify the search terms by editing the search_terms and games lists in the script.
I got back up search terms in case of any difficulties

Contributing
Feel free to submit a pull request or open an issue if you find bugs or have suggestions for improvements.
