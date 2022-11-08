from grequests import get
from grequests import request
# from requests import get
from fake_headers import Headers
from random import choice
from pprint import pprint

website = "https://www.avito.ru/moskva/kollektsionirovanie/voennye_veschi-ASgBAgICAUQchgE?cd=1&q=плитник"


def get_headers():
    headers = Headers(browser="chrome", os='win', headers=True)
    headers_list = [headers.generate() for _ in range(50)]
    for num, item in enumerate(headers_list):
        print(f"{num + 1} ----- {item}")
    return choice(headers_list)


# # with requests
# def main():
#     header = get_headers()
#     print(f"Random header: {header}")
#     response = get(url=website, headers=header)
#     pprint(response.content)
#     print(response.status_code)

# with grequests
def main():
    header = get_headers()
    response = request(method="GET", url=website, headers=header)
    pprint(response)


if __name__ == "__main__":
    main()

# run-command: time python3 main.py
# # with requests:
#     real
#     0
#     m4, 427
#     s
#     user
#     0
#     m0, 881
#     s
#     sys
#     0
#     m0, 179
#     s

# with grequests:
# real    0m0,370s
# user    0m0,334s
# sys     0m0,036s
