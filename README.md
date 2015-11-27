# Dummy-Debug

**Dummy debug** é um package para sublime text 3.

## Porque

Mesmo não sendo o jeito mais adequado, as vezes eu prefiro colocar um ´console.log´ no meio do meu projeto para poder observar uma variavel, o jeito que eu constumava fazer era algo como:

```
console.log("var ->", var);
```

**32 TECLAS PRESSIONADAS**, isso é um absurdo, quando eu precisa fazer algo com mais variaveis eu aumentava ainda mais essa quantidade fazendo algo parecido com:

```
console.log("           ");
console.log("-----------");
console.log("var1 ->", var1);
console.log("var2 ->", var2);
console.log("-----------");
console.log("           ");
```

**UM ABSURDO DE TECLAS PRESSIONADAS**.

Se você faz algo parecido, talvez você possa tirar algum proveito desse plugin, quando você apertar as teclas ´crtl+alt+d´ aparecerá na sua tela o template desse nosso __debug__.

```
console.log("           ");
console.log("-----------");
console.log(" ->", );
console.log("-----------");
console.log("           ");
```

E se você tivar algum texto selecionado ele fará automaticamente.

```
// antes
var_to_debug 

// depois
console.log("           ");
console.log("-----------");
console.log("var_to_debug ->", var_to_debug);
console.log("-----------");
console.log("           ");
```

Apenas três teclas, baixe tambem seu **Dummy debugger** e seja __pro-programmer__.

This work is under (WTFPL)[https://en.wikipedia.org/wiki/WTFPL#Version_2] 	