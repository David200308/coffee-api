# Coffee API

<img src="https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1024-512,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg" alt="How to tap into the health benefits of coffee" style="zoom:50%;" />

## { A query API for Coffee Content based on MongoDB }

### Coffee API Data Categories:
- Coffee Names
- Coffee Contents
- Coffee Making Times
- COffee Making Steps

---

### A. Programming Language:

- Python 3

### B. Library & Database Require:
#### a). Database: 

- MongoDB

#### b). Python Library:

- pymongo
- pandas
- matplotlib.font_manager
- flask
- json
- time

### C. Run Code:

```bash
git clone https://github.com/David200308/coffee-api.git
cd coffee-api
# import the JSON file to MongoDB, and open MongoDB
# check the port & URL
python3 api.py
```



### D. API Usage:

```
// For Run on Localhost or 127.0.0.1:
// For example to get Latte detail

http://127.0.0.1/coffee/?coffee=Latte

//return -->
{"State": "Request", "Coffee": "Latte", "Coffee Content": "Espresso + Steamed milk", "Timestamp": "Tue Aug 2 10:49:01 2022"}

```







