"""
    Задача 3: Инкапсуляция
    Создайте класс BankAccount, который имеет защищенное свойство _balance и методы для депозита (deposit),
    снятия средств (withdraw) и получения текущего баланса (get_balance). Убедитесь, что невозможно снять больше, чем есть на счету.
"""

class BankAccount(object):
    """
   Представляет банковский счет с базовыми операциями, такими как депозит и снятие средств.

   Args:
       balance (float): Баланс банковского счета.
   """
    _baclance = float(0)

    def deposit(self, deposit: float) -> None:
        """
        Вносит указанную сумму на банковский счет.

        Args:
            deposit (float): Сумма для внесения.
        """
        self._baclance += deposit

    def withdraw(self, withdrawal: float) -> None:
        """
        Снимает указанную сумму с банковского счета, если достаточно средств.

        Args:
            withdrawal (float): Сумма для снятия.

        Raises:
            ValueError: Если сумма превышает доступный баланс.
        """
        if withdrawal <= 0:
            print("Неккоректный ввод суммы снятия. Должно быть положительное число")
            return
        if self._baclance < withdrawal:
            print("Недостаточно средств для снятия. Введите другую сумму")
            return
        self._baclance -= withdrawal

    def get_balance(self) -> None:
        """
        Выводит сообщение о текущем балансе на счете.
        """
        print(f"Баланс на счете: {self._baclance}")

if __name__ == "__main__":
    acc = BankAccount()
    acc.deposit(100)
    acc.get_balance()
    acc.withdraw(50)
    acc.get_balance()
    acc.withdraw(-100)
    acc.get_balance()