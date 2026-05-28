import pandas as pd

data = [
    # FALSE URGENCY
    ("Only 3 left in stock!", "false_urgency"),
    ("Hurry! Sale ends in 10 minutes!", "false_urgency"),
    ("Only 1 item left at this price!", "false_urgency"),
    ("Limited time offer - ends tonight!", "false_urgency"),
    ("Flash sale! Only 2 hours remaining!", "false_urgency"),
    ("Just 5 seats left - book now!", "false_urgency"),
    ("Selling fast! Only 4 remaining!", "false_urgency"),
    ("Order in the next 30 minutes to get this deal!", "false_urgency"),
    ("Stock running low - grab yours now!", "false_urgency"),
    ("This offer expires in 15 minutes!", "false_urgency"),

    # CONFIRMSHAMING
    ("No thanks, I don't want to save money.", "confirmshaming"),
    ("No thanks, I hate good deals.", "confirmshaming"),
    ("I don't want free shipping.", "confirmshaming"),
    ("No thanks, I prefer paying full price.", "confirmshaming"),
    ("I'll pass, I don't care about my health.", "confirmshaming"),
    ("No thanks, I don't want to grow my business.", "confirmshaming"),
    ("I don't need more followers.", "confirmshaming"),
    ("No thanks, I enjoy missing out.", "confirmshaming"),
    ("I'll skip, success isn't for me.", "confirmshaming"),
    ("No thanks, I don't want to be smarter.", "confirmshaming"),

    # HIDDEN COSTS
    ("Service fee added at checkout.", "hidden_costs"),
    ("Taxes and fees calculated at the end.", "hidden_costs"),
    ("Processing fee: $4.99", "hidden_costs"),
    ("Booking fee applied at final step.", "hidden_costs"),
    ("Additional charges may apply.", "hidden_costs"),
    ("Resort fee not included in price shown.", "hidden_costs"),
    ("Shipping cost revealed at checkout.", "hidden_costs"),
    ("Final price includes mandatory handling fee.", "hidden_costs"),
    ("Small convenience fee added at payment.", "hidden_costs"),
    ("Price shown excludes applicable taxes.", "hidden_costs"),

    # TRICK QUESTIONS
    ("Uncheck this box if you do not want to not receive emails.", "trick_questions"),
    ("Check here to opt out of not receiving offers.", "trick_questions"),
    ("Leave unchecked if you don't want to unsubscribe.", "trick_questions"),
    ("Tick this box to avoid not getting promotional updates.", "trick_questions"),
    ("Check to opt out of receiving partner offers.", "trick_questions"),
    ("Uncheck if you wish to not be removed from our list.", "trick_questions"),
    ("Check this box if you do not want emails.", "trick_questions"),
    ("Leave blank to continue receiving special offers.", "trick_questions"),
    ("Deselect to stop not getting notifications.", "trick_questions"),
    ("Check here to disable promotional preferences.", "trick_questions"),

    # ROACH MOTEL
    ("Sign up in one click!", "roach_motel"),
    ("Cancellation requires calling our support line.", "roach_motel"),
    ("To cancel, mail a written request to our office.", "roach_motel"),
    ("Easy to join, call us to leave.", "roach_motel"),
    ("Unsubscribe by sending a letter to our headquarters.", "roach_motel"),
    ("Account deletion takes 30 business days.", "roach_motel"),
    ("To close your account, visit our office in person.", "roach_motel"),
    ("Cancellation only available by phone during business hours.", "roach_motel"),
    ("You can sign up online but must cancel in writing.", "roach_motel"),
    ("Membership cancellation requires 60 days notice.", "roach_motel"),

    # NOT A DARK PATTERN
    ("Free returns within 30 days.", "not_dark_pattern"),
    ("No hidden fees. Price shown is final.", "not_dark_pattern"),
    ("Cancel your subscription anytime online.", "not_dark_pattern"),
    ("We will never share your data with third parties.", "not_dark_pattern"),
    ("Transparent pricing - no surprises at checkout.", "not_dark_pattern"),
    ("Easy one-click cancellation available.", "not_dark_pattern"),
    ("Your privacy is our priority.", "not_dark_pattern"),
    ("Full refund guaranteed within 7 days.", "not_dark_pattern"),
    ("No subscription required.", "not_dark_pattern"),
    ("Opt in to emails only if you want to.", "not_dark_pattern"),
]

df = pd.DataFrame(data, columns=["text", "label"])
df.to_csv("darkpatterns.csv", index=False)
print(f"Dataset created! Total examples: {len(df)}")
print(df["label"].value_counts())