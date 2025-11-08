from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount): ...

class PayPalPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"PayPal: {amount} ₸ төлем өңделді")

class StripePaymentService:
    def make_transaction(self, total_amount):
        print(f"Stripe: {total_amount} ₸ транзакция сәтті өтті")

class StripePaymentAdapter(IPaymentProcessor):
    def __init__(self, stripe_service):
        self.stripe_service = stripe_service
    def process_payment(self, amount):
        self.stripe_service.make_transaction(amount)

class KaspiPayService:
    def pay(self, sum_kzt):
        print(f"Kaspi Pay: {sum_kzt} ₸ төлем жіберілді")

class KaspiPaymentAdapter(IPaymentProcessor):
    def __init__(self, kaspi_service):
        self.kaspi_service = kaspi_service
    def process_payment(self, amount):
        self.kaspi_service.pay(amount)

def choose_processor():
    print("Төлем жүйесін таңдаңыз:")
    print("1) PayPal")
    print("2) Stripe")
    print("3) Kaspi Pay")
    x = input("Таңдау: ").strip()
    if x == "1":
        return PayPalPaymentProcessor()
    if x == "2":
        return StripePaymentAdapter(StripePaymentService())
    return KaspiPaymentAdapter(KaspiPayService())

def read_amount():
    s = input("Сома (₸): ").strip()
    try:
        return float(s)
    except:
        print("Қате сома, әдепкі 0")
        return 0.0

def main():
    proc = choose_processor()
    while True:
        print("\nМәзір:")
        print("1) Төлем жасау")
        print("2) Жүйені ауыстыру")
        print("0) Шығу")
        x = input("Таңдау: ").strip()
        if x == "1":
            amt = read_amount()
            proc.process_payment(amt)
        elif x == "2":
            proc = choose_processor()
        elif x == "0":
            print("Бағдарлама аяқталды")
            break
        else:
            print("Дұрыс емес енгізу")

if __name__ == "__main__":
    main()
