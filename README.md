
# Wompi Scaffolding  
Esta es una plantilla para realizar un backend sencillo en base a los eventos que envia Wompi por medio de su Webhook principalmente esta pensado para usarse en funciones Lambda de servicios en la nube pero puede extrapolarse a otros sectores en los cuales pueda ser beneficioso.  
  
## Signature  
Como se menciona en la documentación oficial de Wompi para verificar la validez de una transacción se usan los campos de `properties` que viajan dentro del cuerpo del Webhook como se ve [aquí](https://docs.wompi.co/docs/colombia/eventos/#paso-a-paso-verifica-la-autenticidad-de-un-evento). 
  
El archivo `signature.py` contiene la funcion `verify_event_checksum` la cual se encarga de verificar si el checksum de seguridad enviado coincide con la clave cryptografica que se tiene en confianza con los dos servidores (Wompi y nuestro servidor) esta devuelve un **True** o **False** dependiendo de el exito de la autenticidad.

### verify_event_checksum
Esta funcion esta construida de forma dinamica, así que si en un futuro las properties dejan de ser las que se especifican en la [documentación oficial de wompi](https://docs.wompi.co/docs/colombia/eventos/#paso-1-concatena-los-valores-de-los-datos-del-evento) la función seguiría trabajando de la misma manera sin ningun error en temas de verificación.

### Response dummies
Dentro de la ruta `./response_dummies` se encuentran tres archivos con los principales metodos de pago usados en Wompi Colombia que son `Nequi` `Boton Bancolombia` y `pse` aquí podras encontrar algunas diferencias en las respuestas segun el metodo. Para realizar pruebas usa la siguiente **llave de eventos**:

    test_events_lUhVs91SiSSyj6nREmimlM2jup9Z1BDy

## Web
Este archivo crea un pequeño endpoint con el cual puedes realizar pruebas en Wompi, idealmente se recomienda usar **[ngrok](https://ngrok.com/)** para poder tener un endpoint https que pueda ser consultado y permita a Wompi enviar la [actualización del estado de una transferencia](https://docs.wompi.co/docs/colombia/eventos/#tipos-de-eventos).
