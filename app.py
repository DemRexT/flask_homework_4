import requests
import time 
import sys
import multiprocessing
import asyncio
import threading

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def download_file_threading(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        filename = url.split('/')[-1]
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Программа download_file_threading завершила работу за {time.time() - start_time} секунд')


def download_file_processing(urls):
    start_time = time.time()
    process = []
    for url in urls:
        filename = url.split('/')[-1]
        p = multiprocessing.Process(target=download_file, args=(url, filename))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print(f'Программа download_file_threading завершила работу за {time.time() - start_time} секунд')


async def download_file_async(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


async def download_files_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        filename = url.split('/')[-1]
        task = asyncio.create_task(download_file_async(url, filename))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print(f'Программа download_file_async выполнила работу за {time.time() - start_time} секунд')



if __name__ == "__main__":
    urls = sys.argv[1:]
    
    download_file_threading(urls)
    download_file_processing(urls)
    asyncio.run(download_files_async(urls))