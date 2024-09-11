import requests
import time
import json
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor

url = "https://jsonplaceholder.typicode.com/posts/"

# The first method programmers use often it needed 3.1 - 4.0 seconds to do the job(it may differ based on the processor)
# however the second method only needed 0.8 - 1.5 seconds. These results aren't final and may change on every
# start of the program but the main difference between of these two methods won't change, it will be almost the same.
# P.S I used the multiprocessing documentation, it helped me realise how this library works and using multiple processes
# I did the assigment.
# After that I tried the threading pool, and it got almost the same result as multiprocessing.

start_time1 = time.time()

posts = []
for i in range(1, 78):
    response = requests.get(url + str(i))
    posts.append(response.json())

with open('sequential_posts.json', 'w') as f:
    json.dump(posts, f, indent=4)

end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1
print(f"Execution time (sequential): {elapsed_time1:.5f} seconds")


def url_to_response(path):
    """This function takes a URL path and returns the response data."""
    final_response = requests.get(path)
    return final_response.json()


if __name__ == "__main__":
    # Measuring the time of the second method (using multiprocessing)
    start_time2 = time.time()

    with Pool(processes=5) as pool:
        # with the help of a map function I map my custom function to all urls I got from the API
        posts_parallel = pool.map(url_to_response, [(url + str(i)) for i in range(1, 78)])

    with open('parallel_posts.json', 'w') as f:
        json.dump(posts_parallel, f, indent=4)

    end_time2 = time.time()
    elapsed_time2 = end_time2 - start_time2
    print(f"Execution time (parallel): {elapsed_time2:.5f} seconds")

    # Threading solution using ThreadPoolExecutor
    def fetch_post_with_threading(post_id):
        """Fetches a post given its ID and returns the JSON response."""
        final_response = requests.get(url + str(post_id))
        return final_response.json()

    start_time3 = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        post_ids = range(1, 78)
        posts_threading = list(executor.map(fetch_post_with_threading, post_ids))

    with open('threading_posts.json', 'w') as f:
        json.dump(posts_threading, f, indent=4)

    end_time3 = time.time()
    elapsed_time3 = end_time3 - start_time3
    print(f"Execution time (threading): {elapsed_time3:.5f} seconds")
