# 

### add dependecies remember to add "--save-exact"
`pdm add --save-exact fastapi`


### run script
`pdm run app/initial_data.py`


### run for ruff

`pdm run ruff check . --fix`

`pdm run ruff format . `

### dev

`pdm run fastapi dev app/main.py`

### prod

`pdm run fastapi run app/main.py`


* do CamelCase response from backend https://medium.com/analytics-vidhya/camel-case-models-with-fast-api-and-pydantic-5a8acb6c0eee
* 
