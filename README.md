# Passenger Flight Count Analysis using MapReduce

## Intro
This project implements a MapReduce-like solution to analyze passenger flight data and identify the passengers with the highest number of flights. The solution uses multi-threading to speed up the mapping phase and generates a bar chart for visualization of the top 10 passengers by flight count.

## Tech Stack
- Python 3.12
- MapReduce-like implementation
- Multi-threading
- Matplotlib (for visualization)
- Pandas (for data handling)

## File Structure
├── data/

│ └── AComp_Passenger_data_no_error(1).csv # Raw passenger data file

├── output/

│ └── top10_passengers.png # Generated chart

├── mapper.py # Implementation for the Map phase

├── reducer.py # Implementation for the Reduce phase

├── utils.py # Helper functions for data reading, etc.

└── main.py # Main program

## Installation and Dependencies
### Installation
To run the project, first clone the repository:git clone https://github.com/911nobody/Cw_TaskB_WangRuixuan.git
### Dependencies
Install the required dependencies using pip:pip install -r requirements.txt

## Usage Instructions
### Usage
1. Place the raw data file `AComp_Passenger_data_no_error(1).csv` into the `data/` folder.
2. Run the main script:python main.py


3. The program will process the data and generate the following outputs:
- A bar chart image showing the top 10 passengers by flight count, saved in the `output/` folder as `top10_passengers.png`.

## Implementation Details
1. **Map Phase**:
- In the map phase, the data is split into chunks and processed concurrently using multi-threading. Each chunk is processed by a separate thread to count the number of flights for each passenger.

2. **Reduce Phase**:
- In the reduce phase, the results from all mappers are combined, and the passenger with the highest number of flights is identified.

3. **Visualization**:
- After processing, a bar chart showing the top 10 passengers with the most flights is generated using Matplotlib.

4. **File Handling**:
- The program handles large datasets by reading the data in chunks and efficiently combining the results.
