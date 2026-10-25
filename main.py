# BBSR-OD AI Business Idea Generator - by Subhjeet

name = input("Tera naam kya hai? ")
skill = input("Tujhe kya aata hai? (jaise: video editing, teaching, farming): ")

print(f"\nHello {name}! Sun mera AI idea tere liye:")

if "video" in skill.lower() or "editing" in skill.lower():
    print("IDEA: Tu YouTube Shorts editing service shuru kar, $50/month per client!")
elif "teach" in skill.lower() or "study" in skill.lower():
    print("IDEA: Tu online tuition ka tool bana, gaon ke baccho ko padha!")
else:
    print(f"IDEA: Tu '{skill}' pe ek simple website bana aur Instagram pe bech!")
    print("Ye tool BBSR-OD se hi dollar kama sakta hai!")

print("\nTu AI Builder ban gaya hai! Next level unlocked!")
