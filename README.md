# synusiaLookup
Ultra bàsic Lookup de isbn a partir de títol, autor i publisher, preparat per baixar i executar.
depen de googlebooks, per tan després de clonar tirar 
`git clone --recursive`
o si ja has fet clon fer:
`git submodule update --init --recursive`

## Usage
Entrada de fitxer csv:
```
$ cat titleAuthor.csv
author,title,publisher
Jack London, Martin Eden,akal
Alexander Berkman, El mito bolchevique,
```
Sortida a **titleAuthor-out.csv**

## Todo

- Afegir Oauth2 per ampliar ràtio de consultes
- Afegir arguments de fitxers in out.
