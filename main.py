from agent.agent import create_agent


def run_application():
    
    print("Payment Intelligence System Started")
    print("Type 'exit' to stop\n")

    agent = create_agent()

    while True:
        user_input = input("Enter your query: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            print("Please enter a valid query.\n")
            continue

        try:
            response = agent.invoke({"input": user_input}, timeout=20)

            
            output = response.get("output", "No response generated.")

            print("\n" + "="*50)
            print("Result:\n")
            print(output)
            print("="*50 + "\n")

        except Exception as e:
            print("\nError:", str(e), "\n")


if __name__ == "__main__":
    run_application()