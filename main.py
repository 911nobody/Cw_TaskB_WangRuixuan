from mapper import map_passenger_counts
from reducer import reduce_passenger_counts
from utils import read_data
import threading
import matplotlib.pyplot as plt
from collections import Counter
import os

INPUT_FILE = r'data/AComp_Passenger_data_no_error(1).csv'
CHUNK_SIZE = 10000
OUTPUT_IMG = 'output/top10_passengers.png'

def generate_bar_chart(reduced_counts):
    top_10 = Counter(reduced_counts).most_common(10)
    ids = [item[0] for item in top_10]
    counts = [item[1] for item in top_10]

    plt.figure(figsize=(10, 6))
    plt.bar(ids, counts, color='steelblue')
    plt.xlabel("Passenger ID")
    plt.ylabel("Number of Flights")
    plt.title("Top 10 Passengers by Flight Count")
    plt.tight_layout()

    os.makedirs("output", exist_ok=True)
    plt.savefig(OUTPUT_IMG)
    plt.close()
    print(f"Image saved to {OUTPUT_IMG}")

def main():
    all_lines = read_data(INPUT_FILE)

    # Multithreaded Map phase: split the data into chunks for multithreading
    chunks = [all_lines[i:i + CHUNK_SIZE] for i in range(0, len(all_lines), CHUNK_SIZE)]
    mapped_results = [] # To store map results from each thread
    threads = [] # List to hold thread objects

    # Wrapper function for the map operation
    def map_wrapper(chunk):
        mapped_results.append(map_passenger_counts(chunk))

    # Create and start a thread for each chunk
    for chunk in chunks:
        t = threading.Thread(target=map_wrapper, args=(chunk,))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Merge the output of mapper
    combined = {}
    for partial_result in mapped_results:
        for pid, count in partial_result.items():
            combined[pid] = combined.get(pid, 0) + count

    # Reduce phase
    top_passenger, max_flights = reduce_passenger_counts(combined)

    print(f"Top Passenger(s): {top_passenger} with {max_flights} flights.")

    generate_bar_chart(combined)

if __name__ == "__main__":
    main()
