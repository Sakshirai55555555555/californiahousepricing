### california house pricing prediction

### Software And Tools Requirements
1) [Github account](https://github.com)
2) [Heroku Account](https://www.heroku.com/)
3) [VS Code IDE](https://code.visualstudio.com/)
4) [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment
```
   pip install virtualenv

   mkdir project-dir
   cd project-dir

   virtualenv venvironment
   or 
   py -3.12 -m venv myenv 

   venvironment\Scripts\activate
```

install library
```
py -3.12 -m pip install "C:\Users\Pramod Rai\Downloads\seaborn-0.13.0-py3-none-any.whl"
py -3.12 -m pip install "C:\Users\Pramod Rai\Downloads\matplotlib-3.8.2-cp312-cp312-win_amd64.whl"
py -3.12 -m pip install "C:\Users\Pramod Rai\Downloads\scikit_learn-1.3.2-cp312-cp312-win_amd64.whl"
py -3.12 -m pip install "C:\Users\Pramod Rai\Downloads\pandas-2.1.3-cp312-cp312-win_amd64.whl"
py -3.12 -m pip install "C:\Users\Pramod Rai\Downloads\flask-3.0.0-py3-none-any.whl"
```

#to host we will use render
```
pip install waitress
waitress-serve --port=8000 App:app
```