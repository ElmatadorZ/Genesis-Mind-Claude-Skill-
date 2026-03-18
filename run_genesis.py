# run_genesis.py

from genesis_orchestrator import GenesisOrchestrator


if __name__ == "__main__":
    system = GenesisOrchestrator()

    while True:
        user_input = input("\n>> ")
        result = system.run(user_input)

        print("\n=== FINAL DECISION ===")
        print(result["final_decision"])

        print("\n=== SHADOW ===")
        print(result["shadow"])

        print("\n=== MULTI-SELF ===")
        for r in result["multi_self"]:
            print(r)
