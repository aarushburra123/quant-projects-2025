import random

def flip_coin():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

def analyze_flips(num_flips):
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        result = flip_coin()
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    return heads_percentage, tails_percentage

if __name__ == '__main__':
    total_flips = 1000
    heads_perc, tails_perc = analyze_flips(total_flips)
    print(f"After {total_flips} flips:")
    print(f"Heads: {heads_perc:.2f}%")
    print(f"Tails: {tails_perc:.2f}%")
