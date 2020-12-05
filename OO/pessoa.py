class Pessoa:
    def comprimentar(self):
        return 'Hello'


if __name__ == '__main__':
    p = Pessoa()
    Pessoa.comprimentar(p)
    print(p.comprimentar())
    xox = ''
