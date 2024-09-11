# Parallel API Requests in Python

This project demonstrates how to make multiple API requests in parallel using different methods: sequential execution, multiprocessing, and multithreading. The goal is to fetch posts from a public API (`jsonplaceholder.typicode.com`) and store the results in JSON files, measuring the time taken by each approach.

## Table of Contents
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Technologies

This project is built using:
- Python 3
- `requests` library for making HTTP requests
- `multiprocessing.Pool` for parallelizing tasks using multiple processes
- `concurrent.futures.ThreadPoolExecutor` for multithreading

## Project Structure


- main.py # Main Python script with sequential, multiprocessing, and threading approaches 
- sequential_posts.json # Output of the sequential method 
- parallel_posts.json # Output of the multiprocessing method 
- threading_posts.json # Output of the threading method 


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gegasnake/threads_with_python_tbc.git
2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
   - pip install -r requirements.txt
  
## Usage
1. Run the script:
    python main.py
2. The script will perform three different types of API requests:

      Sequential requests: Fetch posts one by one.
      Multiprocessing requests: Fetch posts using multiple processes (parallel).
      Multithreading requests: Fetch posts using multiple threads (parallel).

3. The results will be saved into three different JSON files:

      sequential_posts.json: Posts fetched sequentially.
      parallel_posts.json: Posts fetched using multiprocessing.
      threading_posts.json: Posts fetched using threading.
4. The script will also print the execution time for each approach.

## Results
On average, the execution time results can be:

    Sequential Execution: 3.1 to 4.0 seconds
    Multiprocessing Execution: 0.8 to 1.5 seconds
    Threading Execution: 0.9 to 1.6 seconds



### Explanation:

- **Technologies**: Lists the key libraries used.
- **Project Structure**: Provides a quick overview of the project's structure.
- **Installation**: Instructions on how to set up the environment and install the necessary dependencies.
- **Usage**: Explains how to run the script, what to expect, and the output files.
- **Results**: Provides a summary of typical execution times for different methods.

