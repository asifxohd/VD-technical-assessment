import time
import threading

class RateLimiter:
    """
    Limits the number of requests a user can make within a given time window
    """

    def __init__(self, max_requests=5, time_required=60):
        """
        Initialize the rate limiter with max requests and time window
        """
        self.max_requests = max_requests
        self.time_required = time_required
        self.requests = {}
        self.lock = threading.Lock()

    def allow_request(self, user_id):
        """
        Determine if a user is allowed to make a request
        """
        current_time = time.time()
        
        with self.lock:  
            if user_id not in self.requests:
                self.requests[user_id] = []

            valid_timestamps = []
            for t in self.requests[user_id]:
                if current_time - t < self.time_required:
                    valid_timestamps.append(t)
            self.requests[user_id] = valid_timestamps

            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            else:
                return False

def user_requests(user_id, rate_limiter):
    """
    Simulate user requests and log whether they are allowed or denied
    """
    for request_num in range(1, 11):  
        if rate_limiter.allow_request(user_id):
            print(f"{user_id} Request {request_num}: Allowed")
        else:
            print(f"{user_id} Request {request_num}: Denied")
        time.sleep(1) 

def test_rate_limiter():
    """
    Test the rate limiter with multiple users
    """
    rate_limiter = RateLimiter(max_requests=5, time_required=60)
    user_ids = ["user1", "user2", "user3", "user4"]
    
    threads = []
    
    for user_id in user_ids:
        thread = threading.Thread(target=user_requests, args=(user_id, rate_limiter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    test_rate_limiter()
