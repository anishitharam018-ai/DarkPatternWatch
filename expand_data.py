import pandas as pd

extra_data = [
    ("Only seconds left on this deal!", "false_urgency"),
    ("No thanks, I enjoy being left behind.", "confirmshaming"),
    ("Convenience charge added at payment.", "hidden_costs"),
    ("Check to not disable deal notifications.", "trick_questions"),
    ("Instant access, cancellation requires written appeal.", "roach_motel"),
    ("We show all costs upfront, always.", "not_dark_pattern"),
    ("Selling out fast, order immediately!", "false_urgency"),
    ("No thanks, struggling is my preference.", "confirmshaming"),
    ("Handling fee revealed only at final step.", "hidden_costs"),
    ("One click to join, one click to leave.", "not_dark_pattern"),
]

original = pd.read_csv("darkpatterns.csv")
extra_df = pd.DataFrame(extra_data, columns=["text", "label"])
full_df = pd.concat([original, extra_df], ignore_index=True)
full_df.to_csv("darkpatterns.csv", index=False)
print(f"Dataset expanded! Total examples: {len(full_df)}")
print(full_df["label"].value_counts())