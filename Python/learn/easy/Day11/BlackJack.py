# Black Jack game!!

"""
규칙
:
0. 일반적인 블랙잭 게임과 룰이 조금 다르므로 규칙을 읽을 필요가 있다!
1. 처음에 사용자는 카드 두개 딜러는 카드 한개를 받는다.
2. 첫 배팅의 경우, 사용자는 무조건 참여해야 게임 진행이 가능하다.
3. 이후 배팅에서, 사용자는 추가 카드를 받을 수 있고. 이후 게임을 더 진행할 지 결과를 확인할 지를 결정한다.
4. 결과 확인 선택 전까지 딜러의 카드는 추가 배팅 이후 그전 딜러의 카드를 볼 수 있다.
"""
import random
import sys

# 카드 생성 함수
def deal_card():
    cards = [1, 2, 3, 4, 5]
    return random.choice(cards)

# 카드 점수 계산 함수 21이 넘는 경우에 블랙잭임을 알리고 끝냄
def calculate_score_user(cards_score):
    result = sum(cards_score)
    if result > 21:
        print("OH no Black Jack!!")
        sys.exit("GO back to your home!")

def calculate_score_dealer(cards_score):
    result = sum(cards_score)
    if result > 21:
        print("OH no Dealer Black Jack!!")
        sys.exit("You win!")

# 점수 비교 함수
def compare(user, dealer):
    sum_dealer = sum(dealer)
    sum_user = sum(user)
    if sum_dealer > 21:
        sys.exit("You win Good!")
    elif sum_dealer == sum_user:
        sys.exit("Same!")
    else:
        sys.exit("You win Good!")

# 잘 가세요 함수
def Bye():
    print("GOOD BYE! DO not Bet again!")
    sys.exit("GG")

# 시작 지점, 게임 여부 물어봄
user_answer = input("Do you want to play a game of Blackjack?? Type 'y' or 'n : \n")

if user_answer == 'y':
    # 카드 생성
    user_card = []
    user_card.append(deal_card())
    user_card.append(deal_card())
    dealer_card = []
    dealer_card.append(deal_card())

    # 생성 결과 알려주기
    print(f"Your cards are [{user_card[0]}, {user_card[1]}]")
    print(f"Your score is now : {sum(user_card)}")
    print(f"And dealer card is [{dealer_card[0]}]")
    print(f"Dealer score is now : {sum(dealer_card)}")

    # 추가 배팅 물어보기
    user_hit = input('Do you want to "hit" or "no"??\n')
    if user_hit == 'hit':
        # 카드 추가 생성 및 값 알려주기
        user_card.append(deal_card())
        print(f"Your new card is {user_card[-1]}")
        calculate_score_user(user_card)
        dealer_card.append(deal_card())
        print(f"Your score is now : {sum(user_card)}")
        # 점수 계산
        calculate_score_dealer(dealer_card)
        # 반복문 시작
        money = True
        while money is True:
            # 베팅 물어보기
            user_hit = str(input('Do you want to bet?? yes : "hit" no : "no" \n'))
            # 배팅을 하는 경우
            if user_hit == 'no':
                compare(user_card, dealer_card)
            elif user_hit == 'hit':
                print(f"Last time's Dealer card is {dealer_card[-1]}")
                print(f"Last Dealer score is now : {sum(dealer_card)}")
                calculate_score_dealer(dealer_card)
                user_card.append(deal_card())
                print(f"Your new card is {user_card[-1]}")
                calculate_score_user(user_card)
                dealer_card.append(deal_card())
                print(f"Your score is now : {sum(user_card)}")
                calculate_score_dealer(dealer_card)
    else:
        Bye()

else:
    Bye()
