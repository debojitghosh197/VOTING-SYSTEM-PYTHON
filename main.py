def start_voting(candidates, population):
    votes = {candidate: 0 for candidate in candidates}
    for _ in range(population):
        vote = input("Enter the candidate name you want to vote for: ").upper()
        if vote in votes:
            votes[vote] += 1
        else:
            print("Invalid candidate name. Skipping vote.")
    return votes


def show_results(votes):
    print("Voting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")


def main():
    candidates = []
    population = 0
    votes = {}

    while True:
        print("\n-- Voting System Menu --")
        print("1. Start Voting")
        print("2. Show Results")
        print("3. View Number of Candidates and Population")
        print("4. Exit")

        option = int(input("Enter your choice (1-4): "))

        if option == 1:
            if not candidates:
                candidates = input("Enter the names of candidates (comma-separated): ").upper().split(",")
                population = int(input("Enter the number of voters: "))
                votes = start_voting(candidates, population)
                print("Voting completed.")
            else:
                print("Voting has already taken place.")
        elif option == 2:
            if votes:
                show_results(votes)
            else:
                print("Voting has not taken place yet.")
        elif option == 3:
            print(f"Number of Candidates: {len(candidates)}")
            print(f"Population: {population}")
        elif option == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

