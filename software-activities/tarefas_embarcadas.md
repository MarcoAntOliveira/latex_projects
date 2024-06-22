## Competição

Pelo oque deu a entender dá competição, o nosso drone deverá percorrer uma trájetória e desviar de objetos, além de capturar imagens ao longo do percurso de animais. Analisando cada uma das ações que o drone deverá realizar e sugerindo soluções temos:

### Mapeamento da Trajetória
O mapeamento da trajetória é uma tarefa menos exigente em termos de consumo de energia. No entanto, devido à necessidade de comunicação constante com outros componentes eletrônicos, deve ser realizada de forma embarcada no drone.

### Desvio de Objetos
Essa tarefa envolve o mapeamento da área e a detecção de obstáculos no caminho, exigindo respostas rápidas. Devido à necessidade de comunicação com os componentes eletrônicos, essa tarefa também deve ser embarcada no drone.

### Identificação dos Animais ao Longo da Trajetória
A identificação de animais é a tarefa mais exigente em termos de energia e recursos computacionais, especialmente por envolver inteligência artificial. No entanto, não requer respostas rápidas, permitindo que seja realizada externamente para economizar energia a bordo.

### Conclusão
Para atender à exigência de eficiência energética e tempos de resposta rápidos, tarefas que necessitam de respostas imediatas, como o mapeamento da trajetória e o desvio de objetos, devem ser embarcadas. Já tarefas mais intensivas em recursos, como a identificação de animais, podem ser processadas externamente.