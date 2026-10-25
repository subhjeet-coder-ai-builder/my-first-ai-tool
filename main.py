# BBSR-OD AI Business Idea Generator PRO - by Subhjeet

print("=== BBSR-OD AI Business Generator ===")
name = input("Tera naam kya hai? ")
skill = input("Tujhe kya aata hai? (video editing, teaching, farming): ")
budget = int(input("Tere paas kitna budget hai? (rupaye me likh jaise 500): "))

print(f"\nHello {name}! Tera PRO AI idea ready hai:")

if "video" in skill.lower() or "editing" in skill.lower():
    idea = "YouTube Shorts + Reels Editing Agency"
    earning = "$200/month"
elif "teach" in skill.lower() or "study" in skill.lower():
    idea = "BBSR-OD Online Tuition App (Class 1-10)"
    earning = "$150/month"
else:
    idea = f"{skill} ki Service Website"
    earning = "$100/month"

print(f"IDEA: {idea}")
print(f"Budget: Rs {budget} me shuru ho jayega")
print(f"Earning: {earning} kama sakta hai!")

if budget < 1000:
    print("Tip: Bina paise ke Instagram se start kar, free hai!")
else:
    print("Tip: Thoda paisa domain + logo me laga, pro lagega!")

print("\nYe tool BBSR-OD se hi dollar kama sakta hai!")
print("Tu AI Builder ban gaya hai! Next level unlocked!")
