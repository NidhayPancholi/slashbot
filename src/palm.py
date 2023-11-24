import google.generativeai as palm

class PalmAPI():
    def __init__(self) -> None:
        self.api_key = "AIzaSyA4-4uG_3WeouTM9SU2yMaxZ8urq3FOKGE"
        palm.configure(api_key=self.api_key)
        
    def generate_text_response(self,message):
        prompt="""
        Welcome to SlashBot - a simple solution to track your expenses! 
        Here is a list of available commands, please enter a command of your choice so that I can assist you further: 
        /menu: Display this menu

        /add: Record/Add a new spending

        /display: Show sum of expenditure for the current day/month

        /history: Display spending history

        /delete: Clear/Erase all your records

        /edit: Edit/Change spending details

        /addMember: Record/Add a new member for spliting bills

        /memberList: List all members with associated email address

        /memberDelete: Delete a member

        /splitBill: Split a bill across members

        /deleteBill: Delete a specific bill

        /clearBill: Clear all previous bills to be splited

        /viewSplitBill: View the bills has been splited

        /emailBill: Sent email to the members of bills showing the needed transactions

        /budget: Set budget for the month

        /chart: See your expenditure in different charts

        /categoryAdd: Add a new custom category

        /categoryList: List all categories

        /categoryDelete: Delete a category

        /download: Download your history

        /displayDifferentCurrency: Display the sum of expenditures for the current day/month in another currency

        /sendEmail: Send an email with an attachment showing your history
        Provide appropriate response to user's message: {}
        """.format(message)
        response = palm.generate_text(prompt=prompt)
        return response.result