import random

def monte_carlo_simulation(deck_size, num_simulations):
    included_key_num = 0
    for _ in range(num_simulations):
        deck = [1] * deck_size + [0] * (40 - deck_size)
        hands = random.sample(deck, 3)
        if sum(hands) == 0:
            hands = random.sample(deck, 3)
        included_key_num += sum(hands)

    return included_key_num / num_simulations

def main():
    for key_num in range(1, 20):
        simulation_num = 100000
        probability = monte_carlo_simulation(key_num, simulation_num)
        print(f"キーカード数: {key_num}, 確率 {probability * 100:.2f}%")

if __name__ == "__main__":
    main()
# このようにリファクタリングすることで、コー