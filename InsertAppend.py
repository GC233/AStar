"""

作者：Szy
日期：2022年03月08日
"""
from typing import List
class orderList(list):
    def __init__(self,lst):
        super(orderList, self).__init__(lst)

    def insertAppend(self, item, keyIndex=0)->None:
        '''
        在数组中加入一个元素item，并移动其位置，使数组元素按keyIndex有序排列
        item:一个数组
        keyIndex:用于有序插入所依据的item[keyIndex]
        '''
        super(orderList, self).append(item)
        #print(type(self[0]))
        print(super(orderList, self).__getitem__(1))


if  __name__ == "__main__":
    #f=Field(3,3)
    # a=orderList([1,2,3])
    # a.insertAppend([1,2])
    b = [[1, 3], [2, 5], [3, 1]]
    print(sorted(b, key=lambda i: i[1]))
    print(b.sort(key=lambda i: i[1]))
    #print(a)



