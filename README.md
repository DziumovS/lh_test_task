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

The container with the application is deployed in the background if all tests are successful.

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
