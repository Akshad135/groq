# Groq-Cli

## A Python CLI Package to use Groq API

### How to setup:

- Install the package using the command `pip install groq-cli`
- Run the cmd `grc` after installing the package.
- It will ask the Api key. (You can get the api key from [GroqCloud](https://console.groq.com/keys) after registering for free)
- After entering the Api Key, select the role and model in the later steps.

### Commands:

- `grc` : will prompt to enter your query.
- `grc <query>` : It will search for the entered query. <br>
  Note: If the query is of more than one line, use `grc "<query>"`
- `grc --api` : To change the api key.
- `grc --role` : To change the role.
- `grc --model` : To change the model.

<i> Note that the secrets are stored in a json file. <i>

_Thank you [apry8](https://github.com/arpy8) for helping me out_ :)
