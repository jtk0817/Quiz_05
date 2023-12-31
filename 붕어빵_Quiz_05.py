class 붕어빵_타이쿤:
    def __init__(self, 요소, 가격):
        self.요소 = 요소
        self.가격 = 가격
        self.total = 0

    def sell(self):
        print(f"판매된 붕어빵: {self.요소}, 가격: {self.가격}원에 팔렸습니다.")
        self.total += self.가격

    def eat(self):
        print(f"먹는 붕어빵: {self.요소}을 먹었습니다.")

팥_붕어빵 = 붕어빵_타이쿤("팥", 300)
슈크림_붕어빵 = 붕어빵_타이쿤("슈크림", 400)
파인애플_붕어빵 = 붕어빵_타이쿤("파인애플", 1000)
딸기잼_붕어빵 = 붕어빵_타이쿤("딸기잼", 1000)
샥스핀_붕어빵 = 붕어빵_타이쿤("샥스핀", 30000)

슈크림_붕어빵.sell()
파인애플_붕어빵.sell()
딸기잼_붕어빵.sell()
샥스핀_붕어빵.sell()
파인애플_붕어빵.eat()
샥스핀_붕어빵.eat()

print(슈크림_붕어빵.total + 파인애플_붕어빵.total + 슈크림_붕어빵.total + 딸기잼_붕어빵.total + 샥스핀_붕어빵.total)
