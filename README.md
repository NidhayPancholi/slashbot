# :money_with_wings: SlashBot

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/github/languages/top/secheaper/slashbot?color=red&label=Python&logo=Python&logoColor=yellow)
![GitHub contributors](https://img.shields.io/github/contributors/NidhayPancholi/slashbot)
[![DOI](https://zenodo.org/badge/431190543.svg)](https://zenodo.org/badge/latestdoi/431190543)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
[![codecov](https://codecov.io/gh/secheaper/slashbot/branch/main/graph/badge.svg?token=YCKWZTHO7O)](https://codecov.io/gh/secheaper/slashbot)
[![Actions Status](https://github.com/mtkumar123/MyDollarBot/workflows/CI/badge.svg)](https://github.com/mtkumar123/MyDollarBot/actions)
![github workflow](https://github.com/mtkumar123/MyDollarBot/actions/workflows/black.yml/badge.svg)
![Discord](https://img.shields.io/discord/879343473940107264?color=blueviolet&label=Discord%20Discussion%20Chat)
![Lines of code](https://img.shields.io/tokei/lines/github/secheaper/slashbot?color=9cf)
![Version](https://img.shields.io/github/v/release/secheaper/slashbot?color=ff69b4&label=Version)
![GitHub issues](https://img.shields.io/github/issues/NidhayPancholi/slashbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/NidhayPancholi/slashbot)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/NidhayPancholi/slashbot)
![GitHub language count](https://img.shields.io/github/languages/count/NidhayPancholi/slashbot)
![GitHub top language](https://img.shields.io/github/languages/top/NidhayPancholi/slashbot)

<hr>

## Demo Video

https://www.youtube.com/watch?v=uIHnW8YmrsU

## About SlashBot

SlashBot, your friendly Telegram companion, is the effortlessly witty sidekick for recording your daily expenses on a local system. This clever bot brings a touch of humor to mundane tasks, allowing you to:

- **Add/Record new spending:** Because your expenses deserve a grand entrance!
- **Show daily/monthly expenditure:** Your financial status is delivered with a side of charm.
- **Display spending history:** A stroll down memory lane, expense-style.
- **Clear/Erase records:** Giving you a clean slate, with a dash of drama.
- **Edit/Change spending details:** Like a magician tweaking the details to keep things interesting.
- **Download expenditure history in CSV format:** Because spreadsheets are more fun when they come with a little flair.
- **Visualize spending with graphs/pie charts:** Turning your expenses into a visual masterpiece, one chart at a time.
- **Email history CSV file:** Sending your financial history with a touch of sophistication.
- **See total daily/monthly expenditure in different currencies:** Because money speaks many languages.
- **Add/Delete members:** Managing your squad with a sprinkle of organizational magic.
- **Display members:** A roll call of your financial confidantes.
- **Split bills across different members:** Dividing the financial pie, no math degree required.
- **Email split bills:** Sharing expenses with a touch of class.
- **Display split bills:** Showing off the art of financial collaboration.
- **Delete split bills:** Erasing the evidence, just like magic.

SlashBot, where Witt meets fiscal responsibility! 🎩💸✨
---
Sample demos are shown below. They are run on a local machine.

- [:information_desk_person: Sample Demos](#information_desk_person-Sample-Demos)


---

# :star: What's New

### Release Version 1.3.1

Divvy up expenses with flair using SlashBot's /splitBill command! Here's how you can make your financial life a breeze:

1. **Split a Bill (/split bill):**
   - Effortlessly divide expenses among different members using this nifty command.

2. **Email the Split Bill (/emailBill):**
   - Send out the divvied-up bill directly to the involved members using the /emailBill command.

3. **Display Bill History (/viewSplitBill):**
   - Curious about your past financial collaborations? Simply use /viewSplitBill to see the history.

4. **Delete a Bill (/deleteBill):**
   - Choose the bill you wish to erase by using /deleteBill, keeping your financial records as tidy as can be.

5. **Testing Requirements in README.md:**
   - Find all the details you need for testing in the README.md file. Testing made as easy as using the /splitBill command!

6. **Additional Test Cases:**
   - To ensure robust functionality, we've added more test cases to cover various scenarios. Because comprehensive testing is the key to a flawless financial experience!

With these commands and testing enhancements, SlashBot transforms bill splitting into a seamless and delightful experience. Financial harmony, one command at a time! 💸🤖✉️


### Release Version 1.3.0

- Add members using /addMember
- Delete the member by choosing the name of the member by using /memberDelete
- Display the member's list by using the /memberList
- Add more documents for the functions




<!-- [comment]: <> (## Demo) -->

<!-- [comment]: <> (https://user-images.githubusercontent.com/15325746/135395315-e234dc5e-d891-470a-b3f4-04aa1d11ed45.mp4) -->



# :rocket: Installation Guide

## 💻For developers 
Setting up your environment for MyDollarBot is a breeze! Just follow these steps:

1. **Install Python:**
   - Ensure you have at least Python3 installed on your system.

2. **Clone Repository:**
   - Clone this repository to a directory of your choice on your local system.

3. **Navigate and Install Dependencies:**
   - Open a terminal session, navigate to the cloned repository, and run:
     ```bash
     pip install -r requirements.txt
     ```

4. **Download Telegram Desktop App:**
   - Install the Telegram desktop application from [desktop.telegram.org](https://desktop.telegram.org/).

5. **Create a Telegram Bot:**
   - Search for "BotFather" in Telegram and follow the instructions to create a new bot.

6. **Set API_TOKEN Environment Variable:**
   - Create a new System Variable named "API_TOKEN" in your computer's environment variables and paste the token obtained from BotFather.

7. **Run the Bot:**
   - In the terminal, export the PYTHONPATH variable to the main project folder:
     ```bash
     python src/bot.py
     ```
     A successful run will display "TeleBot: Started polling."

8. **Test Your Bot:**
   - Search for your bot on Telegram and enter "/start" or "/menu" to begin tracking your expenses.

For details on deploying on Heroku and more developer tips, check out the documentation [here](https://github.com/mtkumar123/MyDollarBot/blob/main/CONTRIBUTING.md#more-tips-for-developers). Happy tracking! 📊💸🤖

## 💻For testing with Pytest
1. Some modules in testing require the CHAT_ID environment variable to be set.
2. This is the specific ID that is maintained for your chat with the Bot.
3. While running the bot.py, get this ID from line 72 and set it in your system environment variables.
4. This should ensure the effective running of all tests.


# :information_desk_person: Sample Demos

  ### Add member

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/addmember.png"></p>

1. Enter the `/addMember` command
2. Enter the new new member name
3. Enter the member email address


### Delete member

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/memberdelete.png"></p>

1. Enter the `/memberDelete` command
2. Chose the name of the member

### View memberList

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/viewmember.png"></p>

1. Enter the `/memberList` command

### Split a bill

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/splitbill.png"></p>


1. Enter the `/splitBill` command
2. Enter name of the bill
3. Enter amount of the bill
4. Chose Creditor
5. Chose Debtors

### View the split bill

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/viewsplitbill.png"></p>

1. Enter the `/viewSplitBill` command

### Email the split bill

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/emailbill.png"></p>

1. Enter the `/emailBill` command


### Delete a split bill

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/deletbill.png"></p>

1. Enter the `/deleteBill` command
2. Chose the name of the bill to delete

### Clear Bill History

I want to send myself an email for the monthly expenditure


<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/clearBill.png"></p>

1. Enter the `/clearBill›` command


:page_facing_up: License
---
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/secheaper/slashbot/blob/main/LICENSE) for more details.


### Score Card
---
#### Total Grade: 145

| Factor | Score | Notes |
| --- | --- | --- |
| Video | 3 | Link Updated (https://www.youtube.com/watch?v=HFh_ms9q0As) |
| Workload | 3 | Distributed |
| Number of commits | 3 | 20+ |
| Number of commits: by different people | 3 |  |
| Issues report: There are many | 2 |  |
| Issues are being closed | 2 |  |
| DOI badge | 3 |  |
| Docs: format | 3 |  |
| Docs: description  | 3 |  |
| Docs: short animated video | 2 |  |
| Docs: strong punchlines | 3 |  |
| Docs: mini tutorials | 3 |  |
| Use of version control tools | 2 |  |
| Use of style checkers | 3 |  |
| Use of code formatters. | 3 |  |
| Use of syntax checkers. | 3 |  |
| Use of code coverage | 3 |  |
| Other automated analysis tools | 2 |  |
| Test cases exist | 3 |  |
| Test cases are routinely executed | 2 |  |
| The files http://contributing.md/ lists coding standards and lots of tips | 3 |  |
| Issues are discussed before they are closed | 3 |  |
| Chat channel: exists | 3 |  |
| Test cases: a large proportion of the issues related to handling failing cases. | 2 |  |
| Evidence that the whole team is using the same tools | 3 |  |
| Evidence that the members of the team are working across multiple places in the code base | 2 |  |
| Short release cycles | 3 |  |
| Does your website and documentation provide a clear, high-level overview of your software? | 
3 |  |
| Does your website and documentation clearly describe the type of user who should use your software? | 3 |  |
| Do you publish case studies to show how your software has been used by yourself and others? | 3 |  |
| Is the name of your project/software unique? | 3 |  |
| Is your project/software name free from trademark violations? | 2 |  |
| Is your software available as a package that can be deployed without building it? | 3 |  |
| Is your software available for free? | 3 |  |
| Is your source code publicly available to download, either as a downloadable bundle or via access to a source code repository? | 3 |  |
| Is your software hosted in an established, third-party repository like GitHub? | 3 |  |
| Is your documentation clearly available on your website or within your software? | 3 |  |
| Does your documentation include a "quick start" guide, that provides a short overview of how to use your software with some basic examples of use? | 2 |  |
| If you provide more extensive documentation, does this provide clear, step-by-step instructions on how to deploy and use your software? | 3 |  |
| Do you provide a comprehensive guide to all your software’s commands, functions and options? | 3 |  |
| Do you provide troubleshooting information that describes the symptoms and step-by-step solutions for problems and error messages? | 3 |  |
| If your software can be used as a library, package or service by other software, do you provide comprehensive API documentation? | 3 |  |
| Do you store your documentation under revision control with your source code? | 2 |  |
| Do you publish your release history e.g. release data, version numbers, key features of each release etc. on your web site or in your documentation? | 3 |  |
| Does your software describe how a user can get help with using your software? | 3 |  |
| Does your website and documentation describe what support, if any, you provide to users and developers? | 3 |  |
| Does your project have an e-mail address or forum that is solely for supporting users? | 3 |  |
| Are e-mails to your support e-mail address received by more than one person? | 3 |  |
| Does your project have a ticketing system to manage bug reports and feature requests? | 2 |  |
| Is your project's ticketing system publicly visible to your users, so they can view bug reports and feature requests? | 3 |  |


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="https://github.com/WeizhiGao"><img src="https://avatars.githubusercontent.com/u/57804858?v=4" width="75px;" alt=""/><br /><sub><b>Weizhi Gao</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Itaru-Shin"><img src="https://avatars.githubusercontent.com/u/143905092?v=4" width="75px;" alt=""/><br /><sub><b>Fucheng Guo</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/KingBanshou"><img src="https://avatars.githubusercontent.com/u/143905049?v=4" width="75px;" alt=""/><br /><sub><b>Zikang Wang</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/token1029"><img src="https://avatars.githubusercontent.com/u/38797209?v=4" width="75px;" alt=""/><br /><sub><b>Dongming Wu</b></sub></a></td>
  </tr>

   <tr>
     <td> Modified Phase</td>
    <td align="center"><a href="https://github.com/NidhayPancholi"><img src="https://avatars.githubusercontent.com/u/52347410?v=4" width="100px;" alt=""/><br /><sub><b>Nidhay Pancholi</b></sub></a></td>
    <td align="center"><a href="https://github.com/AryanvGupta"><img src="https://avatars.githubusercontent.com/u/55129067?v=4" width="100px;" alt=""/><br /><sub><b>Aryan Gupta</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Lagani21"><img src="https://avatars.githubusercontent.com/u/143046933?v=4" width="100px;" alt=""/><br /><sub><b>Lagani Patel</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/aditigvarma"><img src="https://avatars.githubusercontent.com/u/78954407?v=4" width="100px;" alt=""/><br /><sub><b>Aditi Verma</b></sub></a><br /></td>
 </tr>
</table>



# :calling: Support

For any support, email us at lpatel@ncsu.edu
