# leadhit test-task

To run:
  ```bash
  git clone git@github.com:DziumovS/lh_test_task.git
  ```
  ```bash
  cd lh_test_task
  ```
  ```bash
  docker compose up -d
  ```

The tests are located in test_app.py.

If all tests pass successfully, the application container is deployed in the background on port 5000.

You can send test requests, for example, via Postman with content-type: x-www-form-urlencoded. Or use sending_test_requests.py.


---
<details>
  <summary>Oldschool</summary>
  
if you're an oldfag you also can use this: 
  
  ```bash
  git clone git@github.com:DziumovS/lh_test_task.git
  ```
  ```bash
  cd lh_test_task
  ```
  ```bash
  python -m venv venv
  ```
  ```bash
  source venv/bin/activate
  ```
  ```bash
  pip install -r requirements.txt
  ```
  ```bash
  python test_app.py
  ```
  ```bash
  python main.py
  ```
  
</details>
