# Consumir API REST: curl y python
## Ricardo Pinete

Empezando por "los curl" ps tuve unos problemillas en ponerlo en el cmd, lo ordenaba mal yo jaja, este no me da nada sobre el tiempo al parecer

La poke api, fue copiar el codigo y verlo, basicamente me da la info que pido sobre la url que va al pokemon en este caso pikachu, se usa el datos=json para ir a la parte de "abilities" y escoje las habilidades, ya despues se imprimen junto con el tiempo
https://pokeapi.co/api/v2/pokemon/pikachu metodo GET 200 292 ms 300521 bytes

esta ahora el pronostico de Valles, estuvo dificil de entender, se debe sacar la llave registrandote en la pagina una vez con ella en un archivo .env lo guardas como apikey= "la llave" luego en el otro poner la libreria dotenv para que lo leyera (eso lo aprendi a las malas me tarde mucho) luego en el codigo pongo que busque la que yo llame apikey para cuando la pida podamos entrar, lo demas es masomenos igual al poke api
https://api.openweathermap.org/data/2.5/forecast metodo GET 200 396 ms 17113 bytes

ahora los errores, yo solo me fui a la pokeapi para hacerlos ahi los errores no me daban los bytes o tiempo
el 404 lo provocaba poniendo mal algo en la url por ejemplo yo le quite el picachu y le puse claudiasheimbaun eso no lo encontro por que no existe y ahi el error
el 401 es cuando pide una key api pero no se la dan y puse en el codigo de la poke api la url de weather map ese pide la apikey y como no estaba ahi no deja entrar y da error 401

la respuestas que me daban eran concretas y buenas ya que me daban lo que yo les especificara y si tuviera que decir algo de los bytes podria decir que si no especificas arroja un monton de informacion innecesaria aunque no podria saber la cantidad que solo ocupo en verdad y cuanto "se pierde" o es innecesario


