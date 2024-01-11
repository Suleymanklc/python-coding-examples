import random


class BlackJack:
    def deal_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(self):
        user_cards = []
        computer_cards = []
        user_score = 0
        computer_score = 0
        deal_card_user = False
        deal_card_computer = False
        for count in range(2):
            user_cards.append(self.deal_card())
            computer_cards.append(self.deal_card())
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        while user_score < 17:
            deal_card_user = input("Do you want new card? (y/n): ")
            if str(deal_card_user).lower() == "y":
                self.deal_card()
                user_cards.append(self.deal_card())
        while computer_score < 17:
            deal_card_computer = input("Do you want new card? (y/n): ")
            if str(deal_card_computer).lower() == "y":
                self.deal_card()
                computer_cards.append(self.deal_card())
        if user_score < computer_score < 21:
            print(f"user_score, computer_score: {user_score}, {computer_score}")
            print("opponent wins!")
        elif computer_score < user_score < 21:
            print("yourself wins!")
            print(f"user_score, computer_score: {user_score}, {computer_score}")
        elif computer_score == 21 and computer_score != 21:
            print("opponent wins!")
            print(f"user_score, computer_score: {user_score}, {computer_score}")
        elif user_score != 21 and computer_score == 21:
            print("yourself wins!")
            print(f"user_score, computer_score: {user_score}, {computer_score}")
        if computer_score > 21 and user_score < 21:
            print("yourself wins")
            print(f"user_score, computer_score: {user_score}, {computer_score}")
        elif computer_score < 21 and user_score > 21:
            print("yourself wins")
            print(f"user_score, computer_score: {user_score}, {computer_score}")
        elif computer_score == user_score:
            print("push, next game")
            print(f"user_score, computer_score: {user_score}, {computer_score}")

    def __main__(self):
        game_is_over = False
        calculate_score = self.calculate_score
        calculate_score()
