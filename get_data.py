from time import ctime, sleep
import threading

from api.huya import get_all_huya_data, huya_cate
from api.quanming import get_all_quanming_data, quanming_cate
from api.panda import get_all_panda_data, panda_cate
from api.douyu import get_all_douyu_data, douyu_cate
from api import con, anytv, TV

threads = []


def mul():
    print(ctime())
    t1 = threading.Thread(target=get_all_huya_data, args=(huya_cate,))
    threads.append(t1)
    t2 = threading.Thread(target=get_all_quanming_data, args=(quanming_cate,))
    threads.append(t2)
    t3 = threading.Thread(target=get_all_panda_data, args=(panda_cate,))
    threads.append(t3)
    t4 = threading.Thread(target=get_all_douyu_data, args=(douyu_cate,))
    threads.append(t4)
    print(threads)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    threads.clear()
    print('Done')
    print(ctime())
    sleep(60)
# con.drop_database(anytv)
# con.copy_database('anytv', 'TV')
if __name__ == "__main__":
    while True:
        try:
            con.drop_database(anytv)
            mul()
            con.drop_database(TV)
            con.copy_database('anytv', 'TV')
        except:
            pass
