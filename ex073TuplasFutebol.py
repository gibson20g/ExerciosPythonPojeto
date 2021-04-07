times = ('Corinthians', 'palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atlético-PR', 'Bahia'
         'São Paulo', 'Fluminense', 'Sporrt Recife',
         'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Petra',
         'Atlético-GO')
print('Lista de Times')
for t in times:
	print(t)
print('='*15)
print(f'os 5 primeiros são {times[0:5]}')
print('='*15)
print(f'Os 4 ultimos são {times[-4:]}')
print('='*15)
print(f'Times em ordem Alfabetica{sorted(times)}')
print('='*15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}Posição')

