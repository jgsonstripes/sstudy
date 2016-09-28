import datetime


class Menu:
    def __init__(self, menu_name, price, production_cost):
        self.menuName = menu_name
        self.price = price
        self.productionCost = production_cost

    def print_info(self):
        print(self.menuName)
        print(self.price)
        print(self.productionCost)


class Sale:
    def __init__(self, sale_time, menu):
        self.sale_time = sale_time
        self.menu = menu

    def print_info(self):
        print(self.sale_time)
        print(self.menu)


def select_menu():
    select_list = ["--메뉴--", "메뉴입력", "메뉴삭제", "메뉴판", "판매", "매입", "일매출", "월매출", "종료"]
    return select_list


def add_menu_item(menu_list):
    menu = input("메뉴이름:")
    price = input("가격:")
    production_cost = input("원가:")
    menu_list.append(Menu(menu, price, production_cost))


def delete_menu_item(menu_list):
    name = input("삭제할 메뉴 : ")
    for i, menu in enumerate(menu_list):
        if menu.menuName == name:
            del menu_list[i]


def print_main_menu():
    for inx, val in enumerate(select_menu()):
        if inx == 0:
            print("{}".format(val))
        else:
            print("{}. {}".format(inx, val))
    return int(input("메뉴 선택:"))


def print_menu(arg):
    for i, menu in enumerate(arg):
        print("{}. 메뉴이름 : {},   가격 : {},    원가 : {}".format(i+1, menu.menuName, menu.price, menu.productionCost))


def sale_menu(menu_list, sale_list):
    print_menu(menu_list)
    print("메뉴로 돌아가기 - 0 입력")
    while 1:
        menu_num = int(input("판매할 메뉴를 선택해주세요."))-1
        sale = Sale(datetime.datetime.now().timetuple(), menu_list[menu_num])
        sale_list.append(sale)
        if menu_num == -1:
            break


def print_day_sales(sale_list):
    day = int(input("일을 입력:"))
    sale_today_total = 0
    for i, sale in enumerate(sale_list):
        if sale.sale_time.tm_mday == day:
            sale_today_total += int(sale.menu.price)
            print("{}, {}".format(sale.menu.menuName, sale.sale_time))
    print("일 매출 : {}".format(sale_today_total))


def print_month_sales(sale_list):
    month = int(input("달을 입력:"))
    sale_month_total = 0
    for i, sale in enumerate(sale_list):
        if sale.sale_time.tm_mon == month:
            sale_month_total += int(sale.menu.price)
            print("{}".format(sale.menu.menuName))
    print("월 매출 : {}".format(sale_month_total))


def main():
    menu_list = []
    sale_list = []
    datetime.datetime.now()
    while 1:
        menu = print_main_menu()
        if menu == 1:
            add_menu_item(menu_list)
        elif menu == 2:
            delete_menu_item(menu_list)
        elif menu == 3:
            print_menu(menu_list)
        elif menu == 4:
            sale_menu(menu_list, sale_list)
        elif menu == 6:
            print_day_sales(sale_list)
        elif menu == 7:
            print_month_sales(sale_list)
        elif menu == len(menu_list)-1:
            break


if __name__ == '__main__':
    main()
