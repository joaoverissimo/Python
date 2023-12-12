#Projeto de calcular quantidade de finders automaticamente sem precisar de mesa próxima

#ITENS: onde encontrará os dados base / criar PACK e englobar os itens abaixo
finder = 10 #pack de finder que contém 10 unidades
gb = 2 #gold bar
mj = 26 #metal jaw
pn = 25 #pawn
bf = 20 #black fin
tb = 1 #tech ball
de = 20 #dog ear
ht = 29 #hyena tail
mw = 1 #mini wings

#Média de recompensas em gold bar obtidas em uma recompensa
finder_min = 5 #minimo de gold bars obtidos
finder_max = 10 #maximo de gold bars obtidos

#interação com usuário
quantidade = int(input('Informe a quantidade que deseja produzir: ')) #colocar mínimo de 1 e máximo de 1000

#cálculo de gold bars (recompensa a cada 5 finders): é possível conseguir de 5 a 10 gold bars por recompensa
media_min = 5 * quantidade
media_max = 8 * quantidade 


#cálculos ITENS: fazer função para englobar todos os cálculos??
final_finder = finder * quantidade #calculo de finder
final_gb = gb * quantidade #calculo de gold bar
final_mj = mj * quantidade #calculo de metal jaw
final_pn = pn * quantidade #calculo de pawn
final_bf = bf * quantidade #calculo de black fin
final_tb = tb * quantidade #calculo da tech ball
final_de = de * quantidade #calculo de dog ear
final_ht = ht * quantidade #calculo de hyena tail
final_mw = mw * quantidade #calculo de mini wings

#cálculo de lucro estimado
lucro_min = media_min - final_gb
lucro_max = media_max - final_gb

#retorno do programa
print('Serão produzidos {} finders do RANK A, para isso será necessário: '.format(final_finder))
print('{} gold bars'.format(final_gb))
print('{} metal jaws.'.format(final_mj))
print('{} pawns.'.format(final_pn))
print('{} black fins.'.format(final_bf))
print('{} tech balls.'.format(final_tb))
print('{} dog ears.'.format(final_de))
print('{} hyena tails.'.format(final_ht))
print('{} mini wings.'.format(final_mw))
print('Considerando conseguir uma recompensa usando até 5 finders, é possível obter de {} a {} gold bars!.'.format(media_min, media_max))
print('Seu lucro poderá ser de {} a {} gold bars!!'.format(lucro_min, lucro_max))