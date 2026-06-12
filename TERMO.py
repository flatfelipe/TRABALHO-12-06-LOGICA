import random
palavras = [
    "AMIGO", "CARTA", "LIVRO", "PRAIA", "VERDE", "PEDRA", "FESTA", "CINTO", "FOLHA", "PORTA",
    "PIANO", "TIGRE", "NUVEM", "FORNO", "LENTE", "TRIGO", "BANCO", "CAMPO", "MUNDO", "VENTO",
    "PONTE", "TINTA", "CAIXA", "SALTO", "ROCHA", "PAUTA", "LINHA", "CHAVE", "FUGIR", "ANDAR",
    "BEIJO", "CANTO", "DENTE", "ELITE", "FAROL", "GOSTO", "HONRA", "IDADE", "JOGAR", "LINDO",
    "MARCA", "NAVIO", "OUVIR", "PODER", "QUEDA", "SONHO", "TEMPO", "UNIAO", "VALOR", "VIGOR",
    "ZEBRA", "ABRIL", "BOLSA", "COURO", "DUELO", "ETAPA", "FRUTA", "GRITO", "HOTEL", "IMPAR",
    "JUNTO", "LAGOS", "MAGRO", "NOBRE", "OCASO", "PINGO", "QUASE", "RAIVA", "SABOR", "TERNO",
    "URGIR", "VASTO", "XAMPU", "ZELAR", "ARDOR", "BRISA", "CLARO", "DORSO", "EXAME", "FARDO",
    "GARRA", "HASTE", "ISCAS", "JUSTO", "LAPIS", "MORAL", "NIVEL", "OPERA", "PRADO", "QUILO",
    "RUIDO", "SORTE", "TRAMA", "VENDA", "BICHO", "CARGA", "DADOS", "SINAL", "TECLA", "VOLTA"
]

n = random.randint(0, 99)

VERDE = '\033[32m'
AMARELO = '\033[33m'
RESET = '\033[m'
def jogar():
    palpiteLetra = []
    palavra = palavras[n]
    letras = list(palavra)
    #letras = [T, E, R, M, O]

    #repetição palavras
    for _ in range(5):
    
        palpite = str(input())
        palpiteLetra = list(palpite)

        if len(palpiteLetra) == 5:
            for i in range(5):
                if palpiteLetra[i] == letras[i]:
                    print(f"{VERDE}[ {palpiteLetra[i]} ]{RESET}", end="")
                elif palpiteLetra[i] in letras:
                    print(f"{AMARELO}[ {palpiteLetra[i]} ] {RESET}", end="")
                else:
                    print(f"[ {palpiteLetra[i]} ]", end="")
            print()
            if palpiteLetra == letras:
                print(f"{VERDE}VOCE GANHOU!!!{RESET}")
        else:
            print("A palavra precisa ter 5 letras... Escreva a próxima palavra:")

    print(f"{VERDE}VOCÊ PERDEU!!!{RESET}")

while True:
    jogar()

    opcao = input("\nDeseja jogar novamente? (S/N): ").upper()

    if opcao != "S":
        print("Obrigado por jogar!")
        break
    