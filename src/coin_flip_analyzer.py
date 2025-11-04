import random

def flip_coin():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

def find_50_50_split():
    heads_count = 0
    tails_count = 0
    total_flips = 0

    while True:
        total_flips += 1
        result = flip_coin()
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

        if total_flips >= 1000:
            heads_percentage = (heads_count / total_flips) * 100
            if 49.99 < heads_percentage < 50.01:
                break
    
    tails_percentage = (tails_count / total_flips) * 100
    return total_flips, heads_percentage, tails_percentage

if __name__ == '__main__':
    total_flips, heads_perc, tails_perc = find_50_50_split()
    print(f"It took {total_flips} flips to get a near 50-50 split.")
    print(f"Final percentages:")
    print(f"Heads: {heads_perc:.4f}%")
    print(f"Tails: {tails_perc:.4f}%")
