### 베스킨라빈스 31 ###

class BaskinRobbins:
    def __init__(self):
        self.is_playing = True
        self.currentNumList = [0]
        self.now_turn = 1

    # 게임 시작
    def game_start(self):
        self.is_playing = True

        print("--------------------------------")
        print("[!] 베스킨라빈스 31 게임을 시작합니다.")
        print("[!] p1 부터 시작하세요.")
        print("--------------------------------")

    # 게임 오버
    def game_over(self):
        self.is_playing = False

    # 재시작
    def restart(self):
        self.currentNumList = [0]
        self.now_turn = 1
        self.game_start()
        self.inGame()

    # 턴 바꾸기 - p1 -> p2, p2 -> p1
    def changeTurn(self):
        self.now_turn = 2 if self.now_turn == 1 else 1

    # 숫자 입력받기, 최대 3개, 띄어쓰기 기준
    # 리턴 : 마지막 숫자
    def numInput(self):
        isCurrntNum, isInvalidNum = False, False

        while isCurrntNum is False:
            numList = list(map(int, input(f"p{self.now_turn} 차례 : ").split()))

            for i, num in enumerate(numList):
                if i == len(numList) - 1:
                    break

                if numList[i] + 1 != numList[i+1]:
                    print(f"[!] p{self.now_turn}, 숫자를 순서대로 입력하세요.")
                    isInvalidNum = True
                    break

            if isInvalidNum is True:
                isInvalidNum = False
                continue

            if len(numList) >= 4:
                print(f"[!] p{self.now_turn}, 최대 3개까지만 입력할 수 있습니다.")
                continue

            if numList[-1] >= 32:
                print(f"[!] p{self.now_turn}, 31까지 입력할 수 있습니다.")
                continue

            if numList[0] - 1 != self.currentNumList[-1]:
                print(f"[!] p{self.now_turn}, {self.currentNumList[-1] + 1}부터 시작해야 합니다.")
                continue

            self.currentNumList += numList
            isCurrntNum = True

        return self.currentNumList[-1]

    def inGame(self):
        while self.is_playing:
            latestNum = self.numInput()

            # p1 패배, p2 승리
            if latestNum == 31 and self.now_turn == 1:
                print("--------------------------------")
                print("[!] Game Over")
                print("[!] Winner : p2")
                print("--------------------------------")

                self.is_playing = False

            # p2 패배, p1 승리
            elif latestNum == 31 and self.now_turn == 2:
                print("--------------------------------")
                print("[!] Game Over")
                print("[!] Winner : p1")
                print("--------------------------------")

                self.is_playing = False

            self.changeTurn()

        restart = str(input("[!] 다시 시작하시겠습니까? (y/n) : "))

        if restart.lower() == "y":
            print("[!] 게임을 다시 시작합니다.")
            self.restart()

        else:
            print("[!] 프로그램을 종료합니다.")

game = BaskinRobbins()
game.game_start()
game.inGame()