import datetime

if __name__ == "__main__":
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out = open('data.txt', 'a+')
    out.write(date_time + '\n')
    out.close()
