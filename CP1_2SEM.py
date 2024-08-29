import requests
import threading

def fuzzer(url, wordlist, num_threads):
    def fazer_requisicao(pasta):
        url_corrigida = url.rstrip('/')
        pasta_corrigida = pasta.lstrip('/')
        url_final = f"{url_corrigida}/{pasta_corrigida}"
        
        resposta = requests.get(url_final)
        if resposta.status_code == 200:
            print(f"Diretório encontrado: {url_final} - Status: {resposta.status_code}")
        else:
            pass

    with open(wordlist, 'r') as arquivo:
        pastas = arquivo.read().splitlines()

    threads = []
    for pasta in pastas:
        thread = threading.Thread(target=fazer_requisicao, args=(pasta,))
        threads.append(thread)
        thread.start()

        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

if __name__ == "__main__":
    url_alvo = input("Digite a URL alvo: ")
    caminho_wordlist = input("Digite o caminho da wordlist: ")
    numero_threads = int(input("Digite o número de threads: "))
    fuzzer(url_alvo, caminho_wordlist, numero_threads)