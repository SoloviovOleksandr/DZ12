import concurrent.futures
import time
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
        return res
numbers_for_factorials = [i for i in range(1,11)]
result = {}
with concurrent.futures.ProcessPoolExecutor() as executor:
    started_at = time.time()
    for number, fact in zip(numbers_for_factorials, executor.map(factorial, numbers_for_factorials)):
      print(f'The {number} factorial is :{fact}')
      t1 = time.time() - started_at
      result['ProcessPoolExecutor'] = t1
      print(f"Time in  ProcessPoolExecutor:{t1}")
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    started_at = time.time()
    f = {executor.submit(factorial, number): number for  number in numbers_for_factorials}
    for future in concurrent.futures.as_completed(f):
        number = f[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f"exc")
        else:
            print(f"The {number} factorial is:{data}")
        t2 = time.time() - started_at
        result['ThreadPoolExecutor'] = t2
        print(f"Time in ThreadPoolExecutor:{t2}")
fast = min(result, key = result.get)
print(f"{fast} is faster")

