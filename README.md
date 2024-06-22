# não uso mais excel , nem word , nem powerpoint

## Latex_project 


### usando create_tex.sh
#### premissão
chmod +x create_html.sh

#### comando terminal
./create_html.sh <nome_do_arquivo>

### compile_tex.sh
./compile_tex.sh <nome_do_arquivo>


### chatbot.py
#### O versionamento do codigo
Toda vez que eu compilava o codigo dava que a versão da biblioteca  era antiga
#### solução

##### reverter para a biblioteca antiga 
pip install openai==0.28.0


##### converter o codigo para versão nova
openai migrate
