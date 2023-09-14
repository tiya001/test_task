import re
import requests
import socket
from bs4 import BeautifulSoup


def get_request(url):
    """Получение статуса"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Website is working.")
    except requests.exceptions.RequestException as e:
        print(f"Website is not working. Error: {str(e)}")
    return response.status_code


def get_ip_address(host_name):
    """Получение ip адреса"""
    try:
        ip_address = socket.gethostbyname(host_name)
        print(f"IP address of {host_name}: {ip_address}")
    except socket.gaierror:
        print(f"Could not retrieve IP address for {host_name}")
    return ip_address


def get_phone_number(url):
    """Получение номера с сайта"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    phone_number = soup.find('div', class_='phone-number')
    phone = phone_number.get_text()
    return phone


def validate_phone_number(phone_number):
    """Валидация номера телефона"""
    pattern = r'^(\+\d{1,3})?\(\d{1,}\)\d{1,}-\d{2,}-\d{2,}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def change_phone_number(phone_number):
    """Изменение номера в нужный формат"""
    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]
    phone_number = phone_number.replace(' ', '')
    return phone_number


if __name__ == "__main__":
    url = "http://sstmk.ru/"
    phone_number = get_phone_number(url)
    if validate_phone_number(phone_number) is False:
        phone_number = change_phone_number(phone_number)
    print(phone_number)
