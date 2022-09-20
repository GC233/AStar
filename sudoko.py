"""

作者：Szy
日期：2022年03月09日
"""
from Cell import *
class SudokoCell(Cell):
    def __init__(self, text="4"):
        super().__init__()
        self.colorDict={"1":Qt.black,"2":Qt.blue,"3":Qt.red,
                        "4":Qt.white,"5":Qt.GlobalColor.darkMagenta,"6":Qt.yellow,
                        "7":Qt.green,"8":Qt.gray,"9":Qt.GlobalColor.darkRed}

        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.StrongFocus)
        self.grabKeyboard()
        self.setCellText(text)
        self.setCellColor(self.colorDict[self.getCellText()])

#算出一个数独解
class solveSudoko:

    def solve(board=[["." for i in range(9)] for i in range(9)]) -> List[List[str]]:
        #
        times=3
        result = 0
        def isRule(board, row: int, col: int, k: str) -> bool:
            # 检查行重复
            for i in range(0, 9):
                # 跳过自己那个
                if i == col:
                    continue
                if board[row][i] == k:
                    return False
            # 检查列重复
            for j in range(0, 9):
                if j == row:
                    continue
                if board[j][col] == k:
                    return False
            # 检查九宫格重复
            # 开始的行/列
            startRow = row // 3 * 3
            startCol = col // 3 * 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if i == row and j == col:
                        continue
                    elif board[i][j] == k:
                        return False
            return True

        def backTracing(board: List[List[str]]):
            flg = True
            for each in board:
                if "." in each:
                    flg = False
                    break
            if flg:
                #writeBoard(board, "./soduko.txt")
                global result
                print(result)
                result += 1
                if result ==times:
                    raise Exception
                return
            for i in range(0, 9):
                for j in range(0, 9):
                    # 如果有数则跳过
                    if not board[i][j] == ".":
                        continue
                    else:
                        for k in range(1, 10):
                            # 尝试在i,j处放入k
                            if isRule(board, i, j, str(k)):
                                board[i][j] = str(k)
                            else:
                                continue
                            # 如果获得了成功的返回值就退出
                            backTracing(board)
                            board[i][j] = "."
                        board[i][j] = "."
                        return
            return

        def writeBoard(board: List[List[str]], addr: str) -> None:
            f = open(addr, "a+")
            for i in range(0, 9):
                for j in range(0, 9):
                    f.write(board[i][j])
                f.write("\n")
            f.write("\n")
            f.close()
        try:
            backTracing(board)
        except:
            print(board)
            return(board)
        return board

if __name__ == '__main__':
    solveSudoko.solve(board=[["." for i in range(9)] for i in range(9)])
