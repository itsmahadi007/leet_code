class Solution:
    def calculateToll(self, vechile: int, discount: int) -> float:

        return vechile - ((vechile / 100) * discount)


def main():
    # motorcycle = int(input("Enter an Integer a: "))
    # buss = int(input("Enter an Integer r: "))
    # truck = int(input("Enter an Integer p: "))
    # car = int(input("Enter an Integer n: "))

    motorcycle = 30
    buss = 40
    truck = 50
    car = 35

    platinum = 10
    gold = 8
    silver = 5
    gov_vechile_ = 0
    gov_vechile_personal = 2

    s = Solution()
    total_toll = 0
    while True:
        print("motorcycle : 1")
        print("buss : 2")
        print("truck : 3")
        print("car : 4")
        print("Gov Vehicle : 5")

        vechile = int(input("Which Vechile a: "))
        discount = int(input("Has Discount (1 or 0) "))
        discount_per = 0
        if discount:
            print("platinum : 1")
            print("gold : 2")
            print("silver : 3")
            print("Gov Vehicle Personal : 4")
            which_discount = int(input("Which Discount: "))
            if which_discount == 1:
                discount_per = platinum
            elif which_discount == 2:
                discount_per = gold
            elif which_discount == 3:
                discount_per = silver
            elif which_discount == 4:
                discount_per = gov_vechile_personal
        if vechile == 1:
            total_toll += s.calculateToll(motorcycle, discount_per)
        elif vechile == 2:
            total_toll += s.calculateToll(buss, discount_per)
        elif vechile == 3:
            total_toll += s.calculateToll(truck, discount_per)
        elif vechile == 4:
            total_toll += s.calculateToll(car, discount_per)
        elif vechile == 5:
            total_toll += s.calculateToll(0, discount_per)

        print("\nToll Collected", total_toll, "\n\n")


main()
