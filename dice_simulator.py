import random
import matplotlib.pyplot as plt
import csv

def roll_dice(num_dice, sides, rolls, mode):
    results = []
    for _ in range(rolls):
        dice = [random.randint(1, sides) for _ in range(num_dice)]
        if mode == "each":
            results.extend(dice)
        else:
            results.append(sum(dice))
    return results

def display_histogram(results):
    plt.figure(figsize=(10, 5))
    plt.hist(results, bins=range(min(results), max(results)+2), 
             color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Dice Roll Frequency Distribution")
    plt.xlabel("Dice Result")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def save_to_csv(results):
    filename = "dice_results.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Result"])
        for i, result in enumerate(results, start=1):
            writer.writerow([i, result])
    print(f"\n✅ Results exported successfully to {filename}")

# Main Program
print("🎲 Dice Rolling Simulator 🎲")
num_dice = int(input("Enter number of dice: "))
sides = int(input("Enter number of sides per die: "))
rolls = int(input("Enter number of rolls: "))
mode = input("Mode (sum/each)? [default=sum]: ").strip().lower()
if mode not in ["sum", "each"]:
    mode = "sum"

results = roll_dice(num_dice, sides, rolls, mode)

# Results Preview
print("\n📌 Results Preview:")
for i, result in enumerate(results, start=1):
    print(f"Roll {i}: {result}")

# Frequency Table
print("\n📊 Frequency Table:")
frequency = {}
for result in results:
    frequency[result] = frequency.get(result, 0) + 1
for value, count in sorted(frequency.items()):
    print(f"{value}: {count} times")

# Ask for CSV Export
choice = input("\nDo you want to export results to CSV? (y/n): ").strip().lower()
if choice == "y":
    save_to_csv(results)
else:
    print("❌ CSV export skipped.")

# Show Histogram
display_histogram(results)
