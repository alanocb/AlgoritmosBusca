
![IADE_Logotipo](https://github.com/alanocb/AlgoritmosBusca/assets/99679262/ec2d0dad-b541-48ef-936a-de170157ef48)

# Inteligência Artificial
## Análise Comparativa de Algoritmos de Busca: DFS, BFS, UCS e A*
## Mini Projeto: Algoritmos de Busca

**Autores:** Alano Baptista - 20190818 | Luquenia Galiano - 20210451 | 13/10/2023

### Detalhes
**Grafo A)**  
Foi utilizado o seguinte grafo, com o objetivo de começar no nó 0 e chegar ao nó 18. Nos gráficos a seguir, as seguintes cores representam:
- Verde: Nós que não foram abertos
- Amarelo: Nós abertos
- Vermelho: Nó final

  ![1](https://github.com/alanocb/AlgoritmosBusca/assets/99679262/0c1d7012-6fff-4711-a059-125650a06dd5)


### Busca em Largura (BFS)
*Com Verificação*
- **Tempo:** 0.007584810256958008 segundos
- **Memória:** 86016 bytes
- **Ordem de Nós Expandidos:** 0 -> 2 -> 1 -> 5 -> 6 -> 3 -> 4 -> 11 -> 12 -> 13 -> 14 -> 7 -> 8 -> 9 -> 10 -> 15 -> 16 -> 17 -> 18
- **Número de Estados Abertos:** 18
- **Custo Total:** 12

*Sem Verificação*
- **Tempo:** 0.003306865692138672 segundos
- **Memória:** 208896 bytes
- **Ordem de Nós Expandidos:** 0 -> 2 -> 1 -> 5 -> 6 -> 3 -> 4 -> 11 -> 12 -> 13 -> 14 -> 7 -> 8 -> 9 -> 10 -> 15 -> 16 -> 17 -> 18
- **Número de Estados Abertos:** 18
- **Custo Total:** 12
  
![2](https://github.com/alanocb/AlgoritmosBusca/assets/99679262/413eb922-9bb5-46f7-89e1-f5ef65457835)

### Busca em Profundidade (DFS)
*Com Verificação*
- **Tempo:** 0.00853109359741211 segundos
- **Memória:** 98304 bytes
- **Ordem de Nós Expandidos:** 0 -> 1 -> 4 -> 10 -> 9 -> 3 -> 8 -> 18
- **Número de Estados Abertos:** 7
- **Custo Total:** 14

*Sem Verificação*
- **Tempo:** 0.003306865692138672 segundos
- **Memória:** 335872 bytes
- **Ordem de Nós Expandidos:** 0 -> 1 -> 4 -> 10 -> 9 -> 3 -> 8 -> 18
- **Número de Estados Abertos:** 7
- **Custo Total:** 14
  
![3](https://github.com/alanocb/AlgoritmosBusca/assets/99679262/4f372036-28ad-44ab-a460-a286eea9a2f6)


### Busca de Custo Uniforme (UCS)
*Com Verificação*
- **Tempo:** 0.0012371540069580078 segundos
- **Memória:** 1167360 bytes
- **Ordem de Nós Expandidos:** 0 -> 2 -> 5 -> 1 -> 11 -> 6 -> 4 -> 12 -> 14 -> 7 -> 13 -> 3 -> 10 -> 15 -> 9 -> 16 -> 8 -> 18
- **Número de Estados Abertos:** 17
- **Custo Total:** 12

*Sem Verificação*
- **Tempo:** 0.007525920867919922 segundos
- **Memória:** 913408 bytes
- **Ordem de Nós Expandidos:** 0 -> 2 -> 5 -> 1 -> 11 -> 6 -> 4 -> 12 -> 14 -> 7 -> 13 -> 3 -> 10 -> 15 -> 9 -> 16 -> 8 -> 18
- **Número de Estados Abertos:** 17
- **Custo Total:** 12

  ![4](https://github.com/alanocb/AlgoritmosBusca/assets/99679262/06363f5f-349c-4476-af8d-3a03bf56bed7)


### A* (A-Estrela)
*Com Verificação*
- **Tempo:** 0.015568256378173828 segundos
- **Memória:** 126976 bytes
- **Ordem de Nós Expandidos:** 0 -> 1 -> 2 -> 5 -> 3 -> 4 -> 6 -> 7 -> 8 -> 11 -> 12 -> 18
- **Número de Estados Abertos:** 11
- **Custo Total:** 14

*Sem Verificação*
- **Tempo:** 0.004824161529541016 segundos
- **Memória:** 360448 bytes
- **Ordem de Nós Expandidos:** 0 -> 1 -> 2 -> 5 -> 3 -> 4 -> 6 -> 7 -> 8 -> 11 -> 12 -> 18
- **Número de Estados Abertos:** 11
- **Custo Total:** 14

  ![5](https://github.com/alanocb/AlgoritmosBusca/assets/99679262/104c47b1-cdcf-41ed-8b5f-77b003bfe612)


### Conclusão
- Para o grafo utilizado, a busca em largura sem verificação de estados repetidos tem o melhor desempenho em termos de tempo de execução e uso de memória.
- Se a prioridade for encontrar uma solução de custo mínimo, a Busca em Largura e a Busca de Custo Uniforme são as melhores escolhas, já que ambos obtiveram um custo total de 12. No entanto, a Busca de Custo Uniforme tem um estado aberto a menos do que a Busca em Largura.
- O algoritmo A* não obteve a melhor solução, pois a heurística fornecida para o exemplo do exercício pode não ser adequada para este caso específico, destacando a importância de escolher heurísticas apropriadas para diferentes problemas.
