from genesis_full import GenesisMind

gm = GenesisMind()

while True:
    user = input("You > ")
    result = gm.run(user)

    print("\n--- GENESIS OUTPUT ---")
    for k, v in result.items():
        print(f"{k}: {v}")
    print("\n")
