import random

n = random.randint(0, 99)

VERDE = '\033[32m'
AMARELO = '\033[33m'
RESET = '\033[m'
def jogar():
    palavras = [
    "AMIGO", "BRAVO", "CARTA", "DENTE", "FESTA", "GOSTO", "HOTEL", "IDEIA", "JOVEM", "LINDO",
    "MUNDO", "NOBRE", "OLHAR", "PEDRA", "QUASE", "RISCO", "SORTE", "TARDE", "UNIDO", "VERDE",
    "VINHO", "ZEBRA", "ARENA", "BARCO", "CAMPO", "DANOS", "ETAPA", "FALAR", "GARRA", "HONRA",
    "IGUAL", "JOGAR", "LARGO", "MANSO", "NUVEM", "OUSAR", "PODER", "QUEDA", "RIVAL", "SINAL",
    "TEMOR", "URANO", "VAPOR", "ZELAR", "ABRIR", "BOLSA", "CINTO", "DOIDO", "EXATO", "FIRME",
    "GIRAR", "HUMOR", "IRADO", "JUNHO", "LUTAR", "MORAR", "NADAR", "OPTAR", "PULAR", "RAMAL",
    "SABOR", "TOMAR", "USADO", "VIVER", "ANDAR", "BEIJO", "CALOR", "DIZER", "ERRAR", "FOCAR",
    "GRATO", "HAVER", "IMPOR", "JEITO", "LEVAR", "MATAR", "NASAL", "OUVIR", "PAGAR", "RAIVA",
    "SALTO", "TOCAR", "URGIR", "VALER", "ZELOS", "ANEXO", "BICHO", "COURO", "DUELO", "EXTRA",
    "FORNO", "GENTE", "HINOS", "ILHAS", "JUNTO", "LIMPO", "MARCA", "NOITE", "ORDEM", "PRATO",
    "RENDA", "SANTO", "TEMPO", "UNHAS", "VELHO", "AREIA", "BANHO", "CASAL", "DEVER", "ELITE",
    "FAIXA", "GANSO", "HASTE", "INATO", "LENTO", "METAL", "NINHO", "ONTEM", "PLANO", "RUBRO",
    "SULCO", "TROCA", "VASOS", "ACASO", "BANCO", "CABRA", "DADOS", "ECOAR", "FUNDO", "GRUPO",
    "HEROI", "IDEAL", "JUSTO", "LIVRO", "METRO", "NAVIO", "OBTER", "PRAIA", "RURAL", "SONHO",
    "TEXTO", "VAZIO", "AFETO", "BATER", "CLARO", "DENSO", "ESTAR", "FAZER", "GOLPE", "HORAS",
    "ITENS", "LAPSO", "MEIGO", "NORTE", "OUTRA", "PERTO", "REDOR", "SABER", "TENSO", "VIRAR",
    "AGORA", "BAIXO", "CEDER", "DURAR", "ETNIA", "FINAL", "GRADE", "IRMAS", "LUZES", "MISTO",
    "NEGAR", "OLHOS", "PONTO", "REGRA", "SUGAR", "TESTE", "VOTOS", "AJUDA", "BOMBA", "CHEIO",
    "DOBRO", "EXPOR", "FOLHA", "GEMER", "HOBBY", "INDIO", "LAZER", "MANIA", "NEGRO", "OPACO",
    "PASTO", "ROSTO", "SELVA", "TIGRE", "VOLTA", "ALUNO", "BORDA", "CERTO", "DIGNO", "FAUNA",
    "GERAL", "HOSTE", "IMUNE", "LEITO", "MESMO", "NIVEL", "PACTO", "RANGO", "SETOR", "TRIGO",
    "VENDA", "AMPLO", "BURRO", "CORAL", "DRAMA", "FATOR", "GLOBO", "IMPAR", "LOCAL", "MOVER",
    "NATAL", "PEITO", "RAZAO", "SEIVA", "TOTAL", "VIOLA", "BAZAR", "CESTA", "DORSO", "FROTA",
    "GANHO", "IDADE", "LOUSA", "MOLHO", "NERVO", "POMAR", "RISOS", "SOGRO", "TRAMA", "VULTO",
    "APELO", "BRISA", "CAVAR", "DORES", "FEIRA", "GENIO", "LETRA", "MAGRA", "PENTE", "ROSAS",
    "SOPRO", "TUMBA", "VORAZ", "ARAME", "BREVE", "CANTO", "DOSES", "FUGIR", "GURIA", "LENDA",
    "MAGIA", "NUNCA", "POEMA", "ROUPA", "SARAR", "TURNO", "VISTO", "ASTRO", "BRUTO", "CEDRO",
    "FARDA", "GRAUS", "LUGAR", "MASSA", "NACAO", "PILAR", "RUMOR", "TURMA", "VAGAR", "AVIAO"
]
    n = random.randint(0, 299)
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
                break
        else:
            print("A palavra precisa ter 5 letras... Escreva a próxima palavra:")
    if palpiteLetra != letras:
        print(f"{VERDE}VOCÊ PERDEU!!!{RESET}")
        print(f"A palavra era {palavra}")

while True:
    jogar()

    opcao = input("\nDeseja jogar novamente? (S/N): ").upper()

    if opcao != "S":
        print("Obrigado por jogar!")
        break
    