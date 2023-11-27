# Contributing to SlashBot

Follow the set of guidelines below to contribute to SlashBot!

## Code of Conduct

Participation in this project requires adherence to this code. If you encounter any behavior that is deemed unacceptable, please report it to lpatel@ncsu.edu.

Following are the prerequisites for engaging in this project include:

1. Enrollment in NC State University's graduate program.
2. Fall 2023 enrolment in the software engineering course.
3. Completion of this project requires Python proficiency.

## How can I Contribute -
Fork first, and merge with permission.
 
### Reporting Bugs

This section outlines the steps for filing a bug report for SlashBot. Following these recommendations makes it easier for maintainers and the community to understand your complaint, reproduce the problem, and find related reports.

Before submitting a bug report:

1. Review the debugging guide.
2. Look through the forum's FAQs for a list of frequently asked queries and problems.
3. Determine which repository is best for reporting the issue.
4.  Start by doing a quick search to see if the issue has been reported before.
   
## How Do I Submit A (Good) Bug Report?

To facilitate efficient issue resolution, please adhere to the following guidelines:

1. **Title:** Use a clear and descriptive title that succinctly identifies the problem.

2. **Reproduction Steps:** Provide a detailed account of the exact steps that lead to the problem. Include specific examples to illustrate these steps.

3. **Observed Behavior:** Describe the behavior you witnessed after following the steps, emphasizing the specific issue.

4. **Expected Behavior:** Clearly state the behavior you anticipated and explain why. This helps in understanding the deviation from expected outcomes.

5. **Visual Aids:** Include screenshots and animated GIFs that visually depict you following the described steps, highlighting the problem.

6. **Performance or Memory Issues:** If the problem pertains to performance or memory, include a CPU profile capture with your report.

By adhering to these guidelines, you contribute to a more effective understanding and resolution of the reported issue.

## Pull Requests

The outlined process serves multiple objectives:

1. **Maintain Project Quality:** Ensure the ongoing quality of the project by addressing and resolving issues and concerns.

2. **Prioritize User Needs:** Focus on fixing problems that hold significance for users, thereby enhancing the overall user experience.

3. **Sustain Contribution Review:** Establish and maintain a sustainable system that enables project maintainers to effectively review and incorporate contributions from the community.
   
## Tips to Extend

To contribute to the project, follow these steps:

1. **Check TO-DO List:**
   - Examine the TO-DO list by selecting the Projects tab.
   - Choose a feature that catches your attention.

2. **Branch and Implementation:**
  - For the feature you have chosen, create a new branch.
  - Use the Telegram bot to implement the feature in Python.
  - To make sure the implementation is functioning, test it locally.

3. **Write Test Cases:**
   - Create relevant test cases to ensure the new functionality is not disruptive with the current setup.
   
4. **Create Pull Request:**
   - Start a pull request and describe the modifications you made.
   - Request project maintainers to provide a comprehensive code review.

5. **Code Review and Approval:**
   - Engage in the code review process, addressing any feedback.
   - Once the pull request is approved, proceed to the next step.

6. **Merge to Main:**
   - Merge the approved changes into the main branch.

7. **Suggestions and TO-DO List:**
   - Encourage contributors to provide suggestions for bot improvement.
   - Add any valuable suggestions to the TO-DO list for consideration and future implementation.

## More tips for developers
### Heroku deployment
The bot is deployed on [Heroku](https://www.heroku.com/), a website used to host source code and apps.

Quoted directly from their page:

"Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud."


#### Why this is useful

Previously, users needed to download the source code, insert their Telegram API key manually, and then execute the Python file. This process posed the risk of both user error and potential issues within the source code. By deploying the bot on Heroku, the code becomes accessible from any location, at any time, eliminating the need for users to download files and simplifying the overall user experience.

#### How we created the bot

1. A heroku account was created with the shared mydollarbot@gmail.com credentials
2. A new app was created called my_dollar_bot. 
3. Within github, we added a [new action](.github/workflows/deploy.yml) to deploy to the heroku bot
4. For every push, the source code is deployed to heroku, and python code/bot.py is executed, starting the bot

This way, if users want to use the bot without developing, they can simply use this bot instead of having to run the
application locally.

#### How to develop the heroku bot server

- Follow steps 1-3 above, except replace with your own email. Install Heroku cli [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
- Within github, add a secret for the heroku api key.
- Create a new CI/CD pipeline (refer our yaml file [here](.github/workflows/deploy.yml)) and set up github actions.
- Create a new Procfile and add `worker: python code/bot.py`. Refer ours [here](https://github.com/mtkumar123/MyDollarBot/blob/main/Procfile)
- Within your heroku dashboard, you can view logs for the bot to understand well the deployment is running. You can also run the command `heroku logs` or `heroku logs -t`
