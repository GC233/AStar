"""

作者：Szy
日期：2022年03月11日
"""
from typing import*
from math import *

class CellSlice:
    class CellAttribute:
        OBSTACLE=0

    def __init__(self, row, col, obstacle=False):
        self.row=row
        self.col=col
        self.obstacle=obstacle
class CellMaze:
    def __init__(self, row, col):
        self.maze = [[CellSlice(i, j) for j in range(col)] for i in range(row)]
    def setObstacle(self, i, j):
        self.maze[i][j].obstacle=True
    def getNeighbour(self, row:int, col:int)->List[CellSlice]:
        "返回p[row][col]周围<=8个邻居"
        if not self.maze:
            return []
        result=[]
        startCol=col-1
        startRow=row-1
        for i in range(startRow, startRow+3):
            for j in range(startCol, startCol+3):
                #跳过自己和越界访问
                if (i==row and j==col) or i>=len(self.maze) or j>=len(self.maze[0]) or i<0 or j<0 :
                    continue
                else:
                    result.append(self.maze[i][j])
        return result
    def getNeighbourCoordinate(self, row:int, col:int):
        if not self.maze:
            return []
        result=[]
        startCol=col-1
        startRow=row-1
        for i in range(startRow, startRow+3):
            for j in range(startCol, startCol+3):
                #跳过自己和越界访问
                if (i==row and j==col) or i>=len(self.maze) or j>=len(self.maze[0]) or i<0 or j<0 :
                    continue
                else:
                    result.append([self.maze[i][j].row, self.maze[i][j].col,
                                   sqrt((self.maze[i][j].row-self.maze[row][col].row)**2)+(self.maze[i][j].col-self.maze[row][col].col)**2])
        return result

    def setObstacle(self, i, j):
        self.maze[i][j].obstacle=True

if __name__ == '__main__':
    row=3
    col=3
    maze=CellMaze(row,col)
    maze.setObstacle(1, 1)
    maze.setObstacle(1, 2)
    startPoint=[0, 2, 0]
    endPoint=[2, 2]
    value=[[None for j in range(col)] for i in range(row)]
    Queue=[]          #队列
    Queue.append(startPoint)
    resultQueue=[]      #存储出队的元素
    while Queue:
        item=Queue.pop(0) #队头出队
        resultQueue.append(item.copy())
        value[item[0]][item[1]]=item[2]
        #result=maze.getNeighbour(item[0], item[1])
        result = maze.getNeighbour(item[0], item[1])
        for each in result:
            if each.obstacle:
                continue
            #point=[i, j, distance]
            point = [each.row, each.col, sqrt((each.row-item[0])**2+(each.col-item[1])**2)+item[2]]
            flg=True
            # 检测如果该坐标既不在结果中，也不在当前队列中，就加入队列
            for each2 in resultQueue:
                if point[0:2]==each2[0:2]:
                    flg=False
                    break
            for each3 in Queue:
                if point[0:2]==each3[0:2]:
                    flg=False
                    break
            if flg:
                Queue.append(point.copy())

    for each in resultQueue:
        print(each)
    #逆推法寻找路径
    pace=[]
    road=endPoint
    distance = 1000
    for each in value:
        print(each)
    while road!=startPoint[0:-1]:
        #获取邻居
        print(road)
        result=maze.getNeighbour(road[0], road[1])
        lastDis=0
        for each in result:
            if each.obstacle:
                continue
            #在reusltQueue中找到each点对应坐标所对应的路程
            last_Pace=None
            for each1 in resultQueue:
            #取得对应点距原点的距离
                if each.row==each1[0] and each.col==each1[1]:
                    lastDis=each1[2]
            if distance>lastDis+sqrt((each.row-endPoint[0])**2+(each.col-endPoint[1])**2):
                distance=lastDis+sqrt((each.row-endPoint[0])**2+(each.col-endPoint[1])**2)
                last_Pace=[each.row, each.col]
                road=last_Pace
                pace.append(last_Pace)
    print(pace)


