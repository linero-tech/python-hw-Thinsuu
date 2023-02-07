from to_do import TODO


def task9():
    return """
    INPUT Show the user to put his/her bank card into the 
    green light case shown on the right side of the screen
    IF the card is both valid and pushed through properly 
    THEN proceed further to ask for pincode
    ELSE push out the card from the case
    INPUT Ask for the pincode of the user's bank card
    INPUT LET the user choose and click the following options:
    1) withdraw the money from the card,
    2) put the money into the card,
    3) check the balance amount of the card,
    4) change the pin code
    5) language setting
    IF the user choose the option no. 1 THEN proceed to ask user to 
    to type the desirable amount of withdrawal ELSE proceed ...
    INPUT Ask the user to click Ok to confirm the amount
    INPUT Start ATM's internal process to withdraw money from card
    and convert to cash
    INPUT Notify the ATM user by blinking and pushing out cash 
    under the screen
    OUTPUT Push the bank card out
    """